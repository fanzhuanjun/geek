# fanza-search

代码如下

```python
from bs4 import BeautifulSoup
import requests
from multiprocessing import Pool

def getPage(url):
    headers = {
        # 'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        # 'accept-encoding':'gzip, deflate, br',
        # 'accept-language':'zh-CN,zh;q=0.9,ja;q=0.8',
        # 'cache-control':'max-age=0',
        'cookie':'i3_ab=5291; __utma=125690133.164440750.1598834757.1598834757.1598834757.1; __utmz=125690133.1598834757.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmc=125690133; app_uid=ygb1XV9MSEHBi41rQUKgAg==; cX_S=kehsxmr3ov6mwt3p; cX_P=kehsxmrlxhq4x3ln; AMP_TOKEN=%24NOT_FOUND; _dga=GA1.3.164440750.1598834757; _dga_gid=GA1.3.1693828570.1598834758; age_check_done=1; adpf_uid=syckZKYfiqyDveaO; _ts_yjad=1598834761228; _ga=GA1.3.164440750.1598834757; _gid=GA1.3.487109396.1598834763; dtm_id=bt64gi1oj0frnh591o5g; bypass_auid=53703472-c6ff-62a0-7b91-9f6800888ee4; adr_id=pYzwxGErs3qA5y3MOQxAARgKVm4knRJznmiR78dfs6vBQPFR; i3_recommend_ab=91; _tdim=f8292c23-c64a-45d9-e5cd-7e41669a7c43; _im_ses.1003537=1; LSS_SESID=A1lRXE9CCQJYQTR6d0cKEF9WAFkQOVRIcGEICSQlcycjIiEzBUtRUiMiIHJhRwoQX1EOQWE1JWJtFl1YX1UHW1pbUVIDBgMKEVlYCREpYjA6N3EweyVGC1gOVQseFwhbWEEOB0dFbEINERURCBYLVF9GRgJcCg1eXhZdQl9TCEAGCgUPQFBfE1kQWwQJR0MCCw9dDVVDX0MDAFwTEw1XFUBYEVwECxETWR4c; age_check_searched=1; list_condition=%7B%22digital%22%3A%7B%22limit%22%3Anull%2C%22sort%22%3Anull%2C%22view%22%3Anull%7D%7D; __utmt=1; _im_id.1003537=5562e8bfeb4b5302.1598834768.1.1598836313.1598834768.; ckcy=1; dmm_service=BFsCAx1FWwQCR0JdUkQFX0NeVwwEAx9KWFsNREEAVkIGCUNNFBRaQQJUAwIRch5lAiNwVXdvE2Y9QAwVCFANEgkIXVASFFpbAlYBA0AMUg1DE19TRxtfSlhVDURCBFRbBAZVG11FWwYCR0JXQUJEDBJfAQwSSwVXCQtZARBeSkNfVwobBVkMX1cLEwNSDFcNGhYMAgobF1YQFhVdQV8DCkcFUU0DFFpPRQ__; mbox=session#1598834756941-647531#1598838539|check#true#1598836739; __utmb=125690133.75.9.1598836219145',
        # 'sec-fetch-dest':'document',
        # 'sec-fetch-mode':'navigate',
        # 'sec-fetch-site':'none',
        # 'sec-fetch-user':'?1',
        # 'upgrade-insecure-requests':'1',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    }
    try:
        req = requests.get(url=url, headers = headers)
        bs = BeautifulSoup(req.text, 'html.parser')
        return bs
    except Exception as e:
        print('getPage error', e)

def write_txt(result):
    if result:
        with open('c:/pwork/fanza项目/fanzaLink按时间.txt', 'a') as txtfile:
            txtfile.write(result+' ')

def main(offset):
    print(f'正在爬取第{offset}页')
    # url = f'https://www.dmm.co.jp/mono/dvd/-/list/=/list_type=release/sort=ranking/page=/'
    url = f'https://www.dmm.co.jp/mono/dvd/-/list/=/list_type=release/sort=date/page={offset}/'
    
    try:
        bs = getPage(url)
        links = [i.a.attrs['href'] for i in bs.findAll('p', {'class': 'tmb'})]
        [write_txt(l) for l in links]
    except Exception as e:
        print('main error', e)

# req = requests.get(url, headers=headers)
# req.text
# bs = getPage(url)
# bs.findAll('p', {'class': 'tmb'})[0].a.attrs['href']
# links = [i.a.attrs['href'] for i in bs.findAll('p', {'class': 'tmb'})]

# main(218)

# def readTxt():
#     with open('c:/pwork/fanza项目/fanzaList.txt') as file:
#         dateList = file.read().split()
#         return dateList

startPage = 1
endPage = 410
pages = [i for i in range(startPage, endPage+1)]

if __name__ == "__main__":
    pool = Pool(10)
    pool.map(main, pages)
    pool.close()
    pool.join()
    print('done!')
```



# fanza-scrape

代码如下

```python
from bs4 import BeautifulSoup
import requests
from multiprocessing import Pool
import pandas as pd
import numpy as np
import csv

def errorlog(result):
    if result:
        with open('c:/pwork/fanza项目/errorlog.txt', 'a') as txtfile:
            txtfile.write(result+' ')

def write_result(result):
    if result:
        with open('c:/pwork/fanza项目/DVD生数据.csv', 'a', newline='', encoding='utf_8_sig') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(result)

def getPage(url):
    headers = {
        # 'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        # 'accept-encoding':'gzip, deflate, br',
        # 'accept-language':'zh-CN,zh;q=0.9,ja;q=0.8',
        # 'cache-control':'max-age=0',
        'cookie':'i3_ab=5291; __utma=125690133.164440750.1598834757.1598834757.1598834757.1; __utmz=125690133.1598834757.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmc=125690133; app_uid=ygb1XV9MSEHBi41rQUKgAg==; cX_S=kehsxmr3ov6mwt3p; cX_P=kehsxmrlxhq4x3ln; AMP_TOKEN=%24NOT_FOUND; _dga=GA1.3.164440750.1598834757; _dga_gid=GA1.3.1693828570.1598834758; age_check_done=1; adpf_uid=syckZKYfiqyDveaO; _ts_yjad=1598834761228; _ga=GA1.3.164440750.1598834757; _gid=GA1.3.487109396.1598834763; dtm_id=bt64gi1oj0frnh591o5g; bypass_auid=53703472-c6ff-62a0-7b91-9f6800888ee4; adr_id=pYzwxGErs3qA5y3MOQxAARgKVm4knRJznmiR78dfs6vBQPFR; i3_recommend_ab=91; _tdim=f8292c23-c64a-45d9-e5cd-7e41669a7c43; _im_ses.1003537=1; LSS_SESID=A1lRXE9CCQJYQTR6d0cKEF9WAFkQOVRIcGEICSQlcycjIiEzBUtRUiMiIHJhRwoQX1EOQWE1JWJtFl1YX1UHW1pbUVIDBgMKEVlYCREpYjA6N3EweyVGC1gOVQseFwhbWEEOB0dFbEINERURCBYLVF9GRgJcCg1eXhZdQl9TCEAGCgUPQFBfE1kQWwQJR0MCCw9dDVVDX0MDAFwTEw1XFUBYEVwECxETWR4c; age_check_searched=1; list_condition=%7B%22digital%22%3A%7B%22limit%22%3Anull%2C%22sort%22%3Anull%2C%22view%22%3Anull%7D%7D; __utmt=1; _im_id.1003537=5562e8bfeb4b5302.1598834768.1.1598836313.1598834768.; ckcy=1; dmm_service=BFsCAx1FWwQCR0JdUkQFX0NeVwwEAx9KWFsNREEAVkIGCUNNFBRaQQJUAwIRch5lAiNwVXdvE2Y9QAwVCFANEgkIXVASFFpbAlYBA0AMUg1DE19TRxtfSlhVDURCBFRbBAZVG11FWwYCR0JXQUJEDBJfAQwSSwVXCQtZARBeSkNfVwobBVkMX1cLEwNSDFcNGhYMAgobF1YQFhVdQV8DCkcFUU0DFFpPRQ__; mbox=session#1598834756941-647531#1598838539|check#true#1598836739; __utmb=125690133.75.9.1598836219145',
        # 'sec-fetch-dest':'document',
        # 'sec-fetch-mode':'navigate',
        # 'sec-fetch-site':'none',
        # 'sec-fetch-user':'?1',
        # 'upgrade-insecure-requests':'1',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    }
    try:
        req = requests.get(url=url, headers = headers)
        bs = BeautifulSoup(req.text, 'html.parser')
        return bs
    except Exception as e:
        print('getPage error', e)
        errorlog(url)

def readTxt():
    with open('c:/pwork/fanza项目/fanzaLink按时间.txt') as file:
        a = file.read().split()
        urllinks = [i for i in a if "https://" in i]
        return urllinks

def main(link):
    bs = getPage(link)
    info1 = []
    for i in range(10):
        try:
            info1.append(bs.find('table', {'class': 'mg-b20'}).findAll('td', {"width": "100%"})[i].text.strip())
        except Exception as e:
            info1.append(np.nan)
            print('info1 error', e)

    info2 = []
    info2_code = [
        r"""bs.h1.text""", #title
        r"""bs.find('span', {'class': 'txt-price-discount'}).text""", #price
        r"""bs.find('img', {"class": 'tdmm'}).attrs['src']""", #img
        r"""bs.find('p', {"class": 'mg-b20'}).text.strip()""", #简介
        r"""bs.find('div', {'class': 'd-review__points'}).findAll('strong')[0].text""", #平均分
        r"""bs.find('div', {'class': 'd-review__points'}).findAll('strong')[1].text""", #评分数
    ]

    for c in info2_code:
        try:
            info2.append(eval(c))
        except Exception as e:
            info2.append(np.nan)
            # print('info2 error', e)

    info = [link, *info1, *info2]
    write_result(info)
    print(f'已完成一页')


if __name__ == "__main__":
    links = readTxt()
    pool = Pool(10)
    pool.map(main, links)
    pool.close()
    pool.join()
    print('done!')

```

