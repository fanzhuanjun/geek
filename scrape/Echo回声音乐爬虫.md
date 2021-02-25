# 模拟登录网页爬虫（echo app）

源代码：[代码](https://github.com/fanzhuanjun/geek/tree/master/pyfile/echo.py)

这是我过去很喜欢的一个听音乐 app，后来虽然不怎么听了。突然有一天发现这个 app 还有网站，索性来试试看这个网站的爬虫。这是一个很好的模拟登录例子。是之前没有写过的。我们可以通过 `requests` 库的 Session 模块来实现。这个文档是通过崔庆才的模拟登录 `github` 的例子的实践。大家可以先看看崔大佬的 blog 或书的相关章节。





代码

```python
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import csv
from urllib.request import urlretrieve
import os

class Echo:
    def __init__(self):
        self.session = requests.Session()
        self.loginUrl = 'https://www.app-echo.com/#/user/login?'
        self.postUrl = 'https://www.app-echo.com/user/ajax-login'
        self.headers = {
            'origin': 'https://www.app-echo.com',
            'referer': 'https://www.app-echo.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

    def getCsrf(self):
        req = self.session.get(self.loginUrl, headers=self.headers)
        bs = BeautifulSoup(req.text, 'lxml')
        csrf = bs.find('meta', {'name': 'csrf-token'}).attrs['content']
        return csrf
    
    def writeCsv(self, result):
        if result:
            with open('c:/pwork/picture/music.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(result)

    def savefile(self, url, name):
        path = f'c:/pwork/picture/{name}.mp3'
        if not os.path.isfile(path):
            urlretrieve(url, path)
        else:
            print(f'{name}已经存在！')

    def parse(self, page):
        musicUrl = f'https://www.app-echo.com/api/user/sound-likes?uid=6660141&page={page}&limit=20'
        req = self.session.get(musicUrl, headers=self.headers)
        for item in req.json().get('lists'):
            name = item.get('name')
            channel_id = item.get('channel_id')
            source = item.get('source')
            like_count = item.get('like_count')
            self.savefile(source, name)
            self.writeCsv((name, channel_id, source, like_count))
            print(f'{name}下载完成！')

    def login(self, tele, password):
        self.postData = {
            'login_form[name]': tele,
            'login_form[password]': password,
            'login_form[area-code]': '+86',
            '_csrf': self.getCsrf(),
        }
        self.session.post(self.postUrl, data=self.postData, headers=self.headers)

startPage = 1
endPage = 16

if __name__ == "__main__":
    pages = [i for i in range(startPage, endPage + 1)]
    echo = Echo()
    echo.login('用户名', '密码')
    pool = Pool(10)
    pool.map(echo.parse, pages)
    pool.close()
    pool.join()
```

