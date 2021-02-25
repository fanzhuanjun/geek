# 图片爬虫(xsnvshen.com)

日期: 2020-06-14

源码地址：[代码](https://github.com/fanzhuanjun/geek/tree/master/pyfile/xsnvshen.py)

闲来无事，为了防止手生，找一个网站练习一下爬虫。我选择一个比较有诱惑力的网站来爬虫，叫[秀色女神](https://www.xsnvshen.com/)。



## 1. 网页分析

图片的爬虫其实比较简单，只要能解析网站，定位到所在的图片地址，然后用一个python自带库 `urllib.request` 的 `urlretrieve` 函数即可。如果函数出现错误，比如 403等问题，这时候可能需要自定义一个保存文件的函数，这次的练习就出现了这个情况。

网站是这样的：

<img src="https://github.com/fanzhuanjun/fanzhuanjun.github.io/raw/master/myimages/image-20200614195545852.png" alt="image-20200614195545852" style="zoom:80%;" />

我们随便打开一个图集，比如我打开了这个地址 https://www.xsnvshen.com/album/33028

<img src="https://github.com/fanzhuanjun/fanzhuanjun.github.io/raw/master/myimages/image-20200614195656976.png" alt="image-20200614195656976" style="zoom:80%;" />

接下来打开网页源代码，定位图片地址。我用的是chrome浏览器，如下图

<img src="https://github.com/fanzhuanjun/fanzhuanjun.github.io/raw/master/myimages/image-20200614195901160.png" alt="image-20200614195901160" style="zoom:80%;" />

我们可以发现图片地址是 `//img.xsnvshen.com/album/27910/33028/000.jpg` 这是一个相对网址，我们在前面加上 `https:` 才能打开，即 http://img.xsnvshen.com/album/27910/33028/000.jpg 。所以我们可以用 `bs.find('img', {'id': 'bigImg'}).attrs['src'][:-7]` 来定位这个地址。

然后我们用鼠标点开下一张图片，发现只有末位数字发生改变。

<img src="https://github.com/fanzhuanjun/fanzhuanjun.github.io/raw/master/myimages/image-20200614200140916.png" alt="image-20200614200140916" style="zoom:80%;" />

所以，我们只需要改变一下该地址的末位数字，不断循环保存图片，就能把整个图集下载到文件夹下。



当然，这里要注意一个问题，因为我们是自动化爬虫，所以你得先知道这个图集有多少张图片，才能借此建立 `range(numbers)` 函数。图片数量也在图片上方有显示，

<img src="https://github.com/fanzhuanjun/fanzhuanjun.github.io/raw/master/myimages/image-20200614200506404.png" alt="image-20200614200506404" style="zoom:80%;" />

所以我们需要通过 `bs.find('span', {'style': 'font-size: 13px; color:#bf382b'}).text.split()[1]` 找到它，我写这串代码有点过长，其实不是一个好的写法，暂时也想不到更好的，先这样吧。

## 2. 爬虫流程

爬虫流程其实很简单，我们主要建立2个函数，分别是 `getPage(url)` 和 `parse(bs)` 。前者主要是获取网页内容并用 `bs4` 库中的 `BeautifulSoup` 函数解析；后者是定位地址并保存图片。

当然也需要另外的 2 个函数辅助，一个是 `validateTitle(title)` 为了防止命名的各种特殊符号而出现错误；另一个是保存文件函数 `down_pic(url, path)`，我们刚刚也说了，因为在这个网站中，直接用 `urlretrieve` 函数出现了 403 错误，所以我们用一个传统的打开文件写入的方式。



## 3. 代码示例

必备库有 `bs4`、`requests` 。

```
> pip install bs4 requests
```

全部代码如下

```python
# encoding:utf-8
from bs4 import BeautifulSoup
import requests
from urllib.request import urlretrieve
from urllib.request import Request
from urllib.request import urlopen
import os
import re

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Referer': 'https://www.xsnvshen.com/album/hd/',
}

def getPage(url):
    try:
        req = requests.get(url=url, headers = headers, verify=False)
        bs = BeautifulSoup(req.text, 'html.parser')
        return bs
    except Exception as e:
        print(e)

def down_pic(url, path):
    try:
        req = Request(url, headers=headers)
        data = urlopen(req).read()
        with open(path, 'wb') as f:
            f.write(data)
            f.close()
    except Exception as e:
        print(str(e))

def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "", title)  # 替换为下划线
    return new_title

def parse(bs):
    try:
        title = validateTitle(bs.h1.text)
        pageNumbers = bs.find('span', {'style': 'font-size: 13px; color:#bf382b'}).text.split()[1]
        path = f'C:/Images/{title}'
        if not os.path.exists(path):
            os.mkdir(path)
        pic = bs.find('img', {'id': 'bigImg'}).attrs['src'][:-7]
        links = [('https:'+ pic +'%03d'%i + '.jpg', path + '/' + '%03d'%i + '.jpg') for i in range(int(pageNumbers))]
        for link in links:
            print(f'正在下载: {link[1]}')
            down_pic(*link)
        print('done')
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print('请先在C盘创建文件夹Images')
    url = input('请输入链接(无需引号):')
    bs = getPage(url)
    parse(bs)

```



## 4. 运用实例

我们用了一个 `input` 函数，运行时输入想要爬取的网址即可。**注意要先在C盘创建文件夹Images**。

<img src="https://github.com/fanzhuanjun/fanzhuanjun.github.io/raw/master/myimages/image-20200614201711553.png" alt="image-20200614201711553" style="zoom:80%;" />

我们随便输入一个地址，就用刚才的地址吧。https://www.xsnvshen.com/album/33028

<img src="https://github.com/fanzhuanjun/fanzhuanjun.github.io/raw/master/myimages/image-20200614201759270.png" alt="image-20200614201759270" style="zoom:80%;" />

开始自动下载，最后出现 done，即为完成。

我们打开目标的文件夹，就可以发现图片已经下载到硬盘里了。

<img src="https://github.com/fanzhuanjun/fanzhuanjun.github.io/raw/master/myimages/image-20200615083250728.png" alt="image-20200615083250728" style="zoom:80%;" />