# selenium天气网站爬虫实战

日期：2020-06-14

源码地址：[代码](https://github.com/fanzhuanjun/geek/tree/master/pyfile/weather即时写入版.py)

之前我们做过 [https://www.wunderground.com/](https://www.wunderground.com/) 网页的简单爬虫方法，直接获取 json 数据。没看过的童鞋可以看一下之前的文章：[wunderground数据爬虫](scrape\数据爬虫.md)。至于 `selenium` 的基本使用方法还不知道的童鞋，可以查看一下我的另一篇文章：[selenium的安装和使用](scrape\selenium的安装和使用.md)，这篇文章告诉你怎么下载和使用。

这次用 selenium 库的爬虫方法可能比较复杂，是我在过去想的一个笨方法，但是也可以作为一个练习的材料来使用。 selenium 库来爬虫比较万能，因为有时候网页直接 `requests.get` 会被拒绝，这时候模拟打开可能是另一条好的途径。

## 1. 模板导入

因为我们之前已经分析过网站了，所以这次不再做网站分析。我们直接开干吧。首先导入所需的模板

```python
from selenium.webdriver import Chrome
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import csv
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from multiprocessing import Pool
```

我们还是依照惯例，将爬虫流程分为两大函数，一个是网页源代码获取并解析的函数 `get_page` ，另一个是定位表格并合并函数 `parse` 。



## 2. get_page 函数

首先我们看看 `get_page` 函数一块

```python
def get_page(date):
    try:
        options = Options()
        options.add_argument('headless')
        driver = Chrome(options=options)
        driver.get('https://www.wunderground.com/history/daily/ZSPD/date/'+date)
        # 方法一、显性等待
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'observation-table')))
        # 方法二、隐性等待
        # driver.implicitly_wait(5)
        html = driver.page_source
        driver.close()
        bs = BeautifulSoup(html, 'html.parser')
        return bs
    except Exception as e:
        print(f'在时间{date}出错啦，不过爬虫还在继续！', e)
        return None
```

这里涉及一个延时等待。在 Selenium 中，get() 方法会在网页框架加载结束后结束执行，此时如果获取 page_source，可能并不是浏览器完全加载完成的页面，如果某些页面有额外的 Ajax 请求，我们在网页源代码中也不一定能成功获取到。所以，这里需要延时等待一定时间，确保节点已经加载出来。

这里等待的方式有两种：一种是隐式等待，一种是显式等待。

### 隐式等待

当使用隐式等待执行测试的时候，如果 Selenium 没有在 DOM 中找到节点，将继续等待，超出设定时间后，则抛出找不到节点的异常。换句话说，当查找节点而节点并没有立即出现的时候，隐式等待将等待一段时间再查找 DOM，默认的时间是 0。示例如下：

```python
from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://www.zhihu.com/explore')
input = browser.find_element_by_class_name('zu-top-add-question')
print(input)
```

在这里我们用 `implicitly_wait()` 方法实现了隐式等待。

### 显式等待

隐式等待的效果其实并没有那么好，因为我们只规定了一个固定时间，而页面的加载时间会受到网络条件的影响。

这里还有一种更合适的显式等待方法，它指定要查找的节点，然后指定一个最长等待时间。如果在规定时间内加载出来了这个节点，就返回查找的节点；如果到了规定时间依然没有加载出该节点，则抛出超时异常。示例如下：

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(input, button)
```

这里首先引入 WebDriverWait 这个对象，指定最长等待时间，然后调用它的 `until()` 方法，传入要等待条件 `expected_conditions`。比如，这里传入了 `presence_of_element_located` 这个条件，代表节点出现的意思，其参数是节点的定位元组，也就是 ID 为 q 的节点搜索框。

这样可以做到的效果就是，在 10 秒内如果 ID 为 q 的节点（即搜索框）成功加载出来，就返回该节点；如果超过 10 秒还没有加载出来，就抛出异常。

对于按钮，可以更改一下等待条件，比如改为 `element_to_be_clickable`，也就是可点击，所以查找按钮时查找 CSS 选择器为 `.btn-search` 的按钮，如果 10 秒内它是可点击的，也就是成功加载出来了，就返回这个按钮节点；如果超过 10 秒还不可点击，也就是没有加载出来，就抛出异常。

运行代码，在网速较佳的情况下是可以成功加载出来的。

关于延时等待的更多内容可以参考崔庆才的书[《python3网络爬虫开发实战》的7.1节](https://python3webspider.cuiqingcai.com/7.1selenium-de-shi-yong)



## 3. parse 函数

我先贴一下代码。

```python
def parse(bs, date):
    if bs != None:
        try:
            table = bs.find('table', {'class': 'mat-table cdk-table mat-sort ng-star-inserted'})
            table_ss = str(table)
            df = pd.read_html(table_ss)[0]
            colName = df.columns.tolist()
            colName.insert(0, 'date')
            df = df.reindex(columns=colName)
            df['date'] = date
            df.to_csv('c:/pwork/scrape/weatherJishi.csv', mode='a', header=False)
            print(f'写入{date}啦！')
        except Exception as e:
            print('写入失败!', e)
```

在这里，关于 `bs.find()` 的内容比较简单，不再赘述。还不太懂的童鞋可以看一下[《Python网络爬虫权威指南（第2版）》](https://www.ituring.com.cn/book/1980) 的前三章。

这里用到 pandas 库一个比较巧妙的函数 `pd.read_html()` ，我不得不说这是一个非常好用的函数。可以直接定位 html 文本的表格，并转化为 pd 的表格格式。这里用两个语句实现。

```python
table_ss = str(table)
df = pd.read_html(table_ss)[0]
```

下面主要是为了将 `date` 变量置于第一行，所以重新改变了特征顺序（特征即变量，在机器学习里面一般用“特征”这个名词）。

```python
colName = df.columns.tolist()
colName.insert(0, 'date')
df = df.reindex(columns=colName)
df['date'] = date
```

关于 `pd.read_html()` 更多信息，可以查询 pandas 的官方文档：[https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_html.html](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_html.html) 。

最后是一个写入函数，值得注意的是 `mode` ，是每行写入的方式。

```python
df.to_csv('c:/pwork/scrape/weatherJishi.csv', mode='a', header=False)
```

在这里，由于我爬取了一整年的数据，数据量实在太多，一次性运行的话可能要几个小时，而且中途不能中断程序，因此，我写了一个 txt 文本，用于记录已经写入的日期，这样即使程序终端，还是可以中途往下运行。只需要在读取日期时先确认一下文本里是否存在该日期，如果已经存在，那么就不爬取该日期。

代码如下，一个为写入函数，一个为读取函数。

```python
    def write_txt(self, result):
        if result:
            with open('c:/pwork/scrape/weatherLog.txt', 'a') as txtfile:
                txtfile.write(result+' ')

    def readTxt(self):
        with open('c:/pwork/scrape/weatherLog.txt') as file:
            dateList = file.read().split()
            return dateList
```



## 4. 整合为weather类

我们可以将上面所有函数整合至一个类里。在这里要注意我们所需的库包括了selenium、lxml、pandas。记得先 pip 下载相应的库。

```
>pip install selenium lxml pandas
```

完整代码下入

```python
from selenium.webdriver import Chrome
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import csv
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from multiprocessing import Pool

class Weather:
    def __init__(self):
        self.weatherLog = self.readTxt()

    def write_txt(self, result):
        if result:
            with open('c:/pwork/scrape/weatherLog.txt', 'a') as txtfile:
                txtfile.write(result+' ')

    def readTxt(self):
        with open('c:/pwork/scrape/weatherLog.txt') as file:
            dateList = file.read().split()
            return dateList

    def get_page(self, date):
        if (date not in self.weatherLog):
            try:
                options = Options()
                options.add_argument('headless')
                driver = Chrome(options=options)
                driver.get('https://www.wunderground.com/history/daily/ZSPD/date/'+date)
                wait = WebDriverWait(driver, 10)
                wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'observation-table')))
                # time.sleep(5)
                html = driver.page_source
                driver.close()
                bs = BeautifulSoup(html, 'html.parser')
                return bs
            except Exception:
                print(f'在时间{date}出错啦，不过爬虫还在继续！')
                return None
        else:
            print(f'{date}已经爬取。')
            return None

    def parse(self, bs, date):
        if bs != None:
            try:
                table = bs.find('table', {'class': 'mat-table cdk-table mat-sort ng-star-inserted'})
                table_ss = str(table)
                df = pd.read_html(table_ss)[0]
                colName = df.columns.tolist()
                colName.insert(0, 'date')
                df = df.reindex(columns=colName)
                df['date'] = date
                df.to_csv('c:/pwork/scrape/weatherJishi.csv', mode='a', header=False)
                print(f'写入{date}啦！')
                self.weatherLog.append(date)
                self.write_txt(date)
            except Exception as e:
                print('写入失败!', e)


def main(date):
    weather = Weather()
    bs = weather.get_page(date)
    weather.parse(bs, date)

startDate = '2019-01-01'
endDate = '2019-12-31'

if __name__ == "__main__":
    pool = Pool(10)
    date = pd.date_range(startDate, endDate)
    dates = [str(d)[:10] for d in date]
    pool.map(main, dates)
    pool.close()
    pool.join()

    print(f'样本数为: {len(date) * 48}。')
```

这样，我们启动一下，看看眼前飘过的代码，喝一杯茶，等一等吧。这次写的过于粗糙，老是引用别人的文档，下次注意。

<img src="https://github.com/fanzhuanjun/fanzhuanjun.github.io/raw/master/myimages/image-20200615113415132.png" alt="image-20200615113415132" style="zoom:80%;" />

