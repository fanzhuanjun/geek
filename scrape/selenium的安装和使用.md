# selenium的安装和使用

Selenium 本来是为**web浏览器的自动化测试**而用的，后来也用来做网页的爬虫。



## 1. 下载和安装

我们在使用 `selenium` 爬虫的时候，不仅要在 python 安装 `selenium` 库，也应该下载对应的 WebDriver。这样才能通过命令行来打开浏览器。而不同的浏览器有各自的 WebDriver。我的浏览器是 Chrome，所以用的是谷歌浏览器的 [ChromeDriver](https://chromedriver.chromium.org/) ，下载地址为：[https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads) 。

<img src="https://github.com/fanzhuanjun/fanzhuanjun.github.io/raw/master/myimages/image-20200615084333492.png" alt="image-20200615084333492" style="zoom:80%;" />

在这里选择相应的版本的 ChromeDriver 安装。至于版本的查询，可以在设置里面找到。我的版本是83的，所以就下载对应的83的ChromeDriver，下载下来是一个zip的压缩文件，要解压出来，拿到 `chromedriver.exe`。

<img src="https://github.com/fanzhuanjun/fanzhuanjun.github.io/raw/master/myimages/image-20200615084933104.png" alt="image-20200615084933104" style="zoom:80%;" />

接下来还没完成，ChromeDriver的运行是需要设置环境变量的，为了方便你可以把它放在python的目录下，我的python的下载在 `C:\Users\用户名\AppData\Local\Programs\Python\Python38-32\`，直接放在这个文件夹下即可；或者你也可以自己创建一个文件夹，然后设置新的环境变量。

我们可以试验一下 ChromeDriver 是否可以使用，打开命令行终端。

```
>pip install selenium #先下载selenium库
>python
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>from selenium import webdriver
>>>driver = webdriver.Chrome()
```

如果自动弹出空白的网页，证明我们成功了。



## 2. 基本使用方法

我可以使用 ChromeDriver 打开任意网站，我们尝试自动打开百度

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
```

<img src="https://github.com/fanzhuanjun/fanzhuanjun.github.io/raw/master/myimages/image-20200615090649860.png" alt="image-20200615090649860" style="zoom:80%;" />

然后获取它的源代码，如下

```python
from selenium import webdriver

...

page = driver.page_source #获取源代码
page
```

我们也可以关闭浏览器，使用

```python
driver.close()
```



- **无头浏览器**

我们在爬虫的时候会不断的打开浏览器、获取信息、关闭浏览器、打开新的浏览器。。。所以，我们一般希望在后台打开，而不总是弹出来窗口，这时候需要用到 `headless` 参数，使用方法如下

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_option = Options()
chrome_option.add_argument('headless')
driver = webdriver.Chrome(options=chrome_option)
driver.get('https://www.baidu.com')
```

我们同样打开的百度，但是可以发现，并没有出现弹窗，这是因为我们加入了 `headless` 参数。很简单吧？掌握了这个，我们就可以开始去尝试用 `webdriver.Chrome()` 函数来爬虫啦。 

我自己尝试用 `selenium` 库爬了一个天气数据的网站 ：

[https://www.wunderground.com/history/daily/ZSPD/date](https://www.wunderground.com/history/daily/ZSPD/date)



请移步观看 [wunderground的selenium爬虫](scrape\selenium天气网站爬虫实战.md)

