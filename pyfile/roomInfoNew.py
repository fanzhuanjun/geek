import requests
from bs4 import BeautifulSoup
import pandas as pd
from itertools import chain
import re
import csv
from multiprocessing import Pool


def getPage(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    }
    try:
        req = requests.get(url=url, headers = headers)
        bs = BeautifulSoup(req.text, 'html.parser')
        return bs
    except Exception as e:
        print('getPage error', e)

def getLinks(offset):
    url = f'https://bj.lianjia.com/ershoufang/pg{offset}/'
    links = []
    try:
        bs = getPage(url)
        infos = bs.findAll('a', {'class': 'noresultRecommend img LOGCLICKDATA'})
        for info in infos:    
            links.append(info.attrs['href'])
        return links
    except Exception as e:
        print('getLink error', e)

def validateTitle(title):
    rstr = r"[\n ]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "", title)  # 替换为下划线
    return new_title

def write_result(result):
    if result:
        with open('c:/pwork/ershoufang.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(result)


def parse(bs):
    if bs:
        try:
            h1 = bs.h1.text
            unitprice = bs.find('span', {'class': 'unitPriceValue'}).text
            price = bs.find('span', {'class': 'total'}).text + bs.find('span', {'class': 'unit'}).text
            room_mainInfo = bs.find('div', {'class': 'houseInfo'}).find('div', {'class': 'room'}).find('div', {'class': 'mainInfo'}).text
            room_subInfo = bs.find('div', {'class': 'houseInfo'}).find('div', {'class': 'room'}).find('div', {'class': 'subInfo'}).text
            type_mainInfo = bs.find('div', {'class': 'houseInfo'}).find('div', {'class': 'type'}).find('div', {'class': 'mainInfo'}).text
            type_subInfo = bs.find('div', {'class': 'houseInfo'}).find('div', {'class': 'type'}).find('div', {'class': 'subInfo'}).text
            # type_mainInfo, type_subInfo
            area_mainInfo = bs.find('div', {'class': 'houseInfo'}).find('div', {'class': 'area'}).find('div', {'class': 'mainInfo'}).text
            area_subInfo = bs.find('div', {'class': 'houseInfo'}).find('div', {'class': 'area'}).find('div', {'class': 'subInfo'}).text
            # area_mainInfo,area_subInfo
            communityName = bs.find('div', {'class': 'communityName'}).find('a', {'class': 'info'}).text
            areaName = bs.find('div', {'class': 'areaName'}).text.split('\xa0')
            baseinfo = bs.find('div', {'class': 'base'}).findAll('li')
            content = [info.text for info in baseinfo]
            transactioninfo = bs.find('div', {'class': 'transaction'}).findAll('li')
            transaction = [validateTitle(info.text) for info in transactioninfo]
            b = [
                h1, price, unitprice,
                room_mainInfo, room_subInfo,
                type_mainInfo, type_subInfo,
                area_mainInfo, area_subInfo,
                communityName, *areaName,
            ]
            a = [b, content, transaction]
            result = list(chain(*a))
            write_result(result)
            print(result)
            print('---------------')
        except Exception as e:
            print("parse error!", e)

startpage = 1
endpage = 100

def main(link):
    bs = getPage(link)
    parse(bs)

if __name__ == "__main__":
    pool = Pool(3)
    sumLinks = []
    for page in range(startpage, endpage+1):
        links = getLinks(page)
        print(links)
        sumLinks.extend(getLinks(page))
    pool.map(main, sumLinks)
    pool.close()
    pool.join()
    print('done!')