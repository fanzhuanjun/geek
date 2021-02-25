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
