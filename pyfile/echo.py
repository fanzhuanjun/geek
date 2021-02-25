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
    echo.login('你的用户名', '你的密码')
    pool = Pool(10)
    pool.map(echo.parse, pages)
    pool.close()
    pool.join()