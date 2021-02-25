# javbus 训练报告

## 1. 获取数据


```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import csv
import math
import matplotlib.pyplot as plt
```


```python
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)
```


```python
headers = {
        'cookie': "__cfduid=dbdea6928f6c3fa077b6e458f8a951c491611465364; PHPSESSID=jch5s7l5a8pmqa2apvh7l8pst4; 4fJN_2132_saltkey=JmZexOLO; 4fJN_2132_lastvisit=1611463102; 4fJN_2132_sid=LyMX1M; 4fJN_2132_seccode=6892.722b23c2aa10ba2f13; 4fJN_2132_ulastactivity=8182U5jViC%2FjAygOwaukJKQ8g7UiG86%2FGS96lhemAWD19teibmMu; 4fJN_2132_creditnotice=0D1D1D0D0D0D0D0D0D274141; 4fJN_2132_creditbase=0D123D123D0D0D0D0D0D0; 4fJN_2132_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E9%8C%84; 4fJN_2132_lastcheckfeed=274141%7C1611466706; 4fJN_2132_lip=118.238.224.134%2C1610783192; 4fJN_2132_auth=b7d3HqmeDb824IZRpDh4XFLrg9SrOZGXYIg%2BPWlv0LTolMDkq1wzgvKYthiHg78eSrogmjrZj3mls2rSafM0qump7qI; bus_auth=745daR2mKij98hXhSWih9fCatSXNd9vaneFgs8oEULzb4vR0XBimL9nvU6s; 4fJN_2132_lastact=1611466707%09misc.php%09seccode; existmag=all",
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
}

def getPage(url):
    """
    获取网页内容
    """
    try:
        req = requests.get(url=url, headers = headers)
        bs = BeautifulSoup(req.text, 'html.parser')
        return bs
    except Exception as e:
        print('getPage error', e)
        
def get_de_url(url):
    """
    获取单个页面的网站链接
    """
    try:
        bs = getPage(url)
        links = [i.attrs['href'] for i in bs.findAll('a', {'class': 'movie-box'})]
        return links
    except Exception as e:
        print('get_de_url error', e)
```


```python
def get_pages_url(url):
    """
    获取所有页面内获取具体的网站链接
    """
    detailLinks = []
    bs = getPage(url)
    num = bs.select('#resultshowall')[0].text.strip().split()[-1]
    pages = math.ceil(int(num)/30)
    links = [url + '/' + str(i) for i in range(1, pages+1)]
    for i in links:
        detailLinks.extend(get_de_url(i))
    return detailLinks
```


```python
# def resize(info):
#     """
#     爬虫内容标准化
#     """
#     for i in range(len(info)):
#         if ":" in info[i]:
#             info[i] = info[i].split(":")[1].strip()
#     if len(info) == 7:
#         info.insert(3, np.nan)
#         info.insert(6, np.nan)
#         return info
#     elif len(info) == 8:
#         info.insert(-3, np.nan)
#         return info
#     else:
#         return info

# def scrapy(link):
#     """
#     页码内容爬虫
#     输出变量: 'url', 'title', 'pic', 'code', 'date', 'Play time', '導演', '製作商', '發行商', 'series', '類別', 'actress'
#     """
#     try:
#         bs = getPage(link)
#         num = len(bs.find("div", {"class": "col-md-3 info"}).findAll("p"))
#         if num >= 9:
#             info1 = [link, bs.h3.text, bs.find("a", {"class": "bigImage"}).attrs['href']]
#             info2 = []
#             for i in range(num):
#                 info2.append(bs.find("div", {"class": "col-md-3 info"}).findAll("p")[i].text.strip())

#             for i in ['演員:', '類別:']:
#                 info2.remove(i)
#             info2 = resize(info2)
#             info = [*info1, *info2]
#             return pd.Series(info, index=['url', 'title', 'pic', 'code', 'date', 'Play time', '導演', '製作商', '發行商', 'series', '類別', 'actress'])
#         else:
#             return pd.Series([link], index=['url'])
#     except Exception as e:
#         print("scrape error", e)
#         return pd.Series([link], index=['url'])
```

```python
def scrapy(link):
    """
    页码内容爬虫
    输出变量: 'url', 'title', 'pic', 'code', 'date', 'Play time', '導演', '製作商', '發行商', 'series', '類別', 'actress'
    """
    try:
        bs = getPage(link)
        info1 = {'url': link, 'title': bs.h3.text, 'pic': bs.find("a", {"class": "bigImage"}).attrs['href']}
        _ = [i.text.strip() for i in bs.find("div", {"class": "col-md-3 info"}).findAll("p")]
        info_list = []
        for i in range(len(_)):
            if (_[i][-1] != ':') and (":" in _[i]):
                info_list.append(_[i])
            elif _[i][-1] == ':':
                if i != len(_)-1:
                    info_list.append(_[i]+" "+_[i+1])
                else:
                    info_list.append(_[i]+" np.nan")
        for ii in info_list:
            name, inf = ii.split(": ")
            # name, inf = ii.split(":")
            info1[name] = inf.strip()
        return pd.Series(info1)
    except Exception as e:
        # print(link)
        print("scrape error", e)
        return pd.Series([link], index=['url'])
```


```python
from multiprocessing import Pool
import tqdm
import time

def get_data(url, num=None):
    """
    获取某个明星或有关页面的数据
    """
    links = get_pages_url(url)
    if num != None:
        links = links[:num]
    mm = map(scrapy, tqdm.tqdm(links))
    df = pd.DataFrame(mm)
    return df
```


```python
# 读取图片的两种方式

# 方式一：
from PIL import Image
import urllib.request
from io import BytesIO
from IPython.display import display

def readImg(url):
    req = urllib.request.Request(url=url, headers=headers)
    fd = urllib.request.urlopen(req)
    image_file = BytesIO(fd.read())
    im = Image.open(image_file)
    display(im)
    
# 方式二：   
from skimage import io
def readImg2(img_src):
    image = io.imread(img_src)
    io.imshow(image)
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    io.show()
```


```python
def look_pic(url, readType=1):
    if readType ==1:
        f = readImg
    else:
        f = readImg2
    
    bs = getPage(url)
    print("url", url)
    print(bs.h3.text)
    try:
        png = [i.attrs['href'] for i in bs.find("div", {"id": "sample-waterfall"}).findAll('a')]
        for i in png:
            f(i)
    except:
        print("无图片！")
```


```python
from selenium.webdriver import Chrome
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def getPage2(url):
    try:
        options = Options()
        options.add_argument('headless')
        driver = Chrome(options=options)
        driver.get(url)
        # 方法一、显性等待
#         wait = WebDriverWait(driver, 10)
#         wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'observation-table')))
        # 方法二、隐性等待
#         driver.implicitly_wait(3)
        html = driver.page_source
        driver.close()
        bs = BeautifulSoup(html, 'html.parser')
        return bs
    except Exception as e:
        print("getPage2 error")
        return None
    
def get_magnet(url):
    bs = getPage2(url)
    try:
        a = bs.find("table", {"id": "magnet-table"})
        table = pd.read_html(str(a))[0].iloc[:, :3]
        table.columns = table.loc[0].values
        table = table.drop(0, axis=0)
        table = table[~table.磁力名稱.str.contains("審核中")]
        magnet = list(set([i.attrs['href'] for i in a.findAll("a") if 'href' in i.attrs.keys()]))
        table['magnet'] = magnet
        return table
    except Exception as e:
        print("无下载链接", e)
```

## 2. 数据分析


```python
url = "https://www.javbus.com/star/92l"
# url = "https://www.javbus.com/star/p13"
df = get_data(url)
```

      0%|                                                                                         | 0/1502 [00:00<?, ?it/s]
    
    网页获取完毕!
    总共有1502条链接!


    100%|██████████████████████████████████████████████████████████████████████████████| 1502/1502 [08:25<00:00,  2.97it/s]
    
    数据加载完毕!


​    
​    


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 1502 entries, 0 to 1501
    Data columns (total 12 columns):
     #   Column     Non-Null Count  Dtype 
    ---  ------     --------------  ----- 
     0   url        1502 non-null   object
     1   title      1502 non-null   object
     2   pic        1502 non-null   object
     3   code       1502 non-null   object
     4   date       1502 non-null   object
     5   Play time  1502 non-null   object
     6   導演         968 non-null    object
     7   製作商        1502 non-null   object
     8   發行商        835 non-null    object
     9   series     968 non-null    object
     10  類別         1502 non-null   object
     11  actress    1502 non-null   object
    dtypes: object(12)
    memory usage: 140.9+ KB



```python
df['類別'].head(5)
```




    0    高畫質\nDMM獨家\n連褲襪\n巨乳\n出軌\n單體作品\n已婚婦女\n數位馬賽克\n成熟的女人
    1    單體作品\n巨尻\n纪录片\nキス・接吻\n成熟的女人\n數位馬賽克\n巨乳\nDMM獨家\...
    2                        其他戀物癖\n汗だく\n蕩婦\n中出\n合集\nDMM獨家
    3                               巨乳\n合集\n苗條\n美少女\nDMM獨家
    4                合集\n巨尻\n蕩婦\n中出\n女上位\n屁股\n數位馬賽克\nDMM獨家
    Name: 類別, dtype: object




```python
df_chugui = df[(df['類別'].str.contains("出軌")) & (df['actress'] == "水野朝陽")]
```


```python
df_chugui.shape
```




    (28, 12)




```python
for i in df_chugui.index:
    title = df.loc[i].title
    url = df.loc[i].url
    pic = df.loc[i].pic
    
    print(url)
#     print(title)
#     readImg(pic)
```

    https://www.javbus.com/JUL-442
    https://www.javbus.com/CEAD-315
    https://www.javbus.com/MRSS-066
    https://www.javbus.com/JUY-771
    https://www.javbus.com/HJMO-398
    https://www.javbus.com/JUY-610
    https://www.javbus.com/XVSR-378
    https://www.javbus.com/JUY-479
    https://www.javbus.com/NACS-004
    https://www.javbus.com/PRED-011
    https://www.javbus.com/ADN-135
    https://www.javbus.com/FAB-002
    https://www.javbus.com/CESD-410
    https://www.javbus.com/DASD-383
    https://www.javbus.com/JUY-171
    https://www.javbus.com/YPAA-002
    https://www.javbus.com/DVDMS-105
    https://www.javbus.com/CEAD-214
    https://www.javbus.com/NGOD-040
    https://www.javbus.com/CJOD-067
    https://www.javbus.com/JUY-052
    https://www.javbus.com/HZGD-009
    https://www.javbus.com/MIAD-917
    https://www.javbus.com/MEYD-139
    https://www.javbus.com/WANZ-429
    https://www.javbus.com/SERO-267_2015-01-23
    https://www.javbus.com/JUX-405
    https://www.javbus.com/FTR-001



```python
df_keywords = df[df['actress'] == "水野朝陽"]
df_keywords_keywords = df_keywords[(df_keywords['title'].str.contains("妻")) | (df_keywords['title'].str.contains("彼女"))]
df_keywords_keywords.shape
```




    (38, 12)




```python
for i in df_keywords_keywords.index:
    title = df.loc[i].title
    url = df.loc[i].url
    pic = df.loc[i].pic
    
    print(url)
#     print(title)
#     readImg(pic)
```

    https://www.javbus.com/MRSS-066
    https://www.javbus.com/SERO-267_2019-04-12
    https://www.javbus.com/JUFE-036
    https://www.javbus.com/JUY-771
    https://www.javbus.com/HJMO-398
    https://www.javbus.com/JUY-610
    https://www.javbus.com/XVSR-378
    https://www.javbus.com/WWK-026
    https://www.javbus.com/HIGH-135
    https://www.javbus.com/NACS-004
    https://www.javbus.com/HIGH-122
    https://www.javbus.com/KMVR-283
    https://www.javbus.com/JUY-171
    https://www.javbus.com/YPAA-002
    https://www.javbus.com/SERO-267_2017-05-03
    https://www.javbus.com/DVDMS-105
    https://www.javbus.com/CEAD-214
    https://www.javbus.com/NGOD-040
    https://www.javbus.com/HQIS-021
    https://www.javbus.com/WLT-003
    https://www.javbus.com/PPPD-537
    https://www.javbus.com/PPPD-508
    https://www.javbus.com/MIGD-741
    https://www.javbus.com/HMBL-005
    https://www.javbus.com/PPPD-481
    https://www.javbus.com/MIAD-917
    https://www.javbus.com/JUX-848
    https://www.javbus.com/MEYD-139
    https://www.javbus.com/JUFD-581
    https://www.javbus.com/MVSD-290
    https://www.javbus.com/NIMA-005
    https://www.javbus.com/SOAV-012
    https://www.javbus.com/JUFD-475
    https://www.javbus.com/TAMO-004
    https://www.javbus.com/SERO-267_2015-01-23
    https://www.javbus.com/MRSS-009
    https://www.javbus.com/KOID-012
    https://www.javbus.com/FTR-001



```python
target_list = ["https://www.javbus.com/MIAD-917", "https://www.javbus.com/FTR-001"]
```


```python
get_magnet(target_list[0]).head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>磁力名稱</th>
      <th>檔案大小</th>
      <th>分享日期</th>
      <th>magnet</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>miad-917-C 高清 字幕</td>
      <td>6.4GB</td>
      <td>2020-10-03</td>
      <td>magnet:?xt=urn:btih:B533797C59CF683E4B654DBC11...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>miad-917 高清</td>
      <td>6.35GB</td>
      <td>2019-12-19</td>
      <td>magnet:?xt=urn:btih:3CEC5DA8C17D684DCC10CDE488...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>MIAD-917.avi</td>
      <td>1.41GB</td>
      <td>2019-01-17</td>
      <td>magnet:?xt=urn:btih:A6AB8F7C178580F87E3C70D8D6...</td>
    </tr>
  </tbody>
</table>
</div>




```python
get_magnet(target_list[1])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>磁力名稱</th>
      <th>檔案大小</th>
      <th>分享日期</th>
      <th>magnet</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>FTR001MP4</td>
      <td>1.29GB</td>
      <td>2020-10-09</td>
      <td>magnet:?xt=urn:btih:C67843FCDBF89155A288F22228...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>FTR001MP4</td>
      <td>1.21GB</td>
      <td>2019-09-26</td>
      <td>magnet:?xt=urn:btih:A0691C9270171AA3B0516C9D8E...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>FTR-001</td>
      <td>1.5GB</td>
      <td>2017-12-06</td>
      <td>magnet:?xt=urn:btih:EFEEEEBA12B44D1C33818F2D64...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>FTR-001-AVI</td>
      <td>1.5GB</td>
      <td>2017-04-17</td>
      <td>magnet:?xt=urn:btih:CBE1E8BBE7B9F38B5CF96D28F0...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>FTR-001</td>
      <td>973.42MB</td>
      <td>2014-08-04</td>
      <td>magnet:?xt=urn:btih:A1AB49F4B3C3238B28891BB446...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>im-520@SIS001@FTR-001</td>
      <td>400MB</td>
      <td>2014-01-23</td>
      <td>magnet:?xt=urn:btih:4822CE401384CC6C2D6B416D36...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>FTR-001</td>
      <td>910.94MB</td>
      <td>2013-09-12</td>
      <td>magnet:?xt=urn:btih:E32B74977E97CB2E382865B8D0...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>[FTR-001] I Wanted to See a Side of My Wife I ...</td>
      <td>973MB</td>
      <td>2013-07-19</td>
      <td>magnet:?xt=urn:btih:87D914EA7136755DC39429B837...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>FTR-001-AVI</td>
      <td>979.81MB</td>
      <td>2013-06-13</td>
      <td>magnet:?xt=urn:btih:3E7A8D5A8FA44C6D518035CE6A...</td>
    </tr>
    <tr>
      <th>10</th>
      <td>FTR-001-AV.wmv</td>
      <td>910.67MB</td>
      <td>2013-06-13</td>
      <td>magnet:?xt=urn:btih:D6AF8A00CE6FA4DEC389E603E3...</td>
    </tr>
  </tbody>
</table>
</div>




```python
# look_pic(target_list[0], readType=1)
```


```python

```
