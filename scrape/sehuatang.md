# sehuatang 检索结果展示

这是一个检索结果展示。

```python
import requests
from bs4 import BeautifulSoup
# from urllib.parse import urlencode
import re
import numpy as np
import csv
import os

# def encode_url(kw):
#     # kw 为文字字符串
#     url = 'https://sehuatang.org/search.php?mod=forum&searchid=13908&orderby=lastpost&ascdesc=desc&searchsubmit=yes'
#     my_query = {'kw': kw}
#     return url + '&' + urlencode(my_query)

def getPage(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    }
    try:
        req = requests.get(url=url, headers = headers)
        if '对不起，没有找到匹配结果' in req.text:
            return None
        else:
            bs = BeautifulSoup(req.text, 'html.parser')
            return bs
    except Exception as e:
        return None
        print(e)

def searchPage(url):
    bs = getPage(url)
    try:
        page = bs.label.find("span").text.split()[1]
        # page = 300 if page > 300 else page
        return [f'{url}&page={i}' for i in range(1, int(page)+1)]
    except Exception:
        return [f'{url}&page=1']

def scrape(url):
    bs = getPage(url)
    if bs:
        base_url = 'https://sehuatang.org/'
        info = []
        soup = bs.findAll("li", {"class":"pbw"})
        scrape_code = [
            r"""subsoup.a.text""",
            r"""base_url + subsoup.a.attrs['href']""",
            r"""re.findall(r"\d+\.?\d*", subsoup.find("p", {"class": "xg1"}).text)[0]""",
            r"""re.findall(r"\d+\.?\d*", subsoup.find("p", {"class": "xg1"}).text)[1]""",
            r"""subsoup.span.text""",
            r"""subsoup.findAll("a", {"target":"_blank"})[-1].text""",
            r"""subsoup.findAll("a", {"target":"_blank"})[-2].text""",
        ]
        # print(len(soup))
        for subsoup in soup:
            for i in scrape_code:
                try:
                    info.append(eval(i))
                except Exception as e:
                    info.append(np.nan)
            write_result(info)
            info = []

def write_result(result):
    if result:
        with open('c:/pwork/生据.csv', 'a', newline='', encoding='utf_8_sig') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(result)

link = 'https://sehuatang.org/search.php?mod=forum&searchid=25867&orderby=lastpost&ascdesc=desc&searchsubmit=yes&kw=%E8%80%81%E5%A9%86'

if __name__ == "__main__":
    # link = str(input("请输入你要检索的网页："))
    links = searchPage(link)
    # 如果存在该文件，则删除该文件。
    if os.path.exists("c:/pwork/生据.csv"):
        os.remove("c:/pwork/生据.csv")
    # 创建表头
    write_result(['title', 'url', 'comment', 'views', 'date', 'section', 'author'])
    # 开始搜集
    for id, i in enumerate(links):
        scrape(i)
        print(f"已完成 {round(id/len(links)*100, 2)}%。")
    print("done")
```



- 初稿

```python
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import re
import numpy as np
import csv

# def encode_url(kw):
#     # kw 为文字字符串
#     url = 'https://sehuatang.org/search.php?mod=forum&searchid=13908&orderby=lastpost&ascdesc=desc&searchsubmit=yes'
#     my_query = {'kw': kw}
#     return url + '&' + urlencode(my_query)

def getPage(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    }
    try:
        req = requests.get(url=url, headers = headers)
        if '对不起，没有找到匹配结果' in req.text:
            return None
        else:
            bs = BeautifulSoup(req.text, 'html.parser')
            return bs
    except Exception as e:
        return None
        print(e)

def searchPage(url):
    bs = getPage(url)
    try:
        page = bs.label.find("span").text.split()[1]
        # page = 300 if page > 300 else page
        return [f'{url}&page={i}' for i in range(1, int(page)+1)]
    except Exception:
        return [f'{url}&page=1']

def scrape(url):
    bs = getPage(url)
    if bs:
        base_url = 'https://sehuatang.org/'
        info = []
        soup = bs.findAll("li", {"class":"pbw"})
        scrape_code = [
            r"""subsoup.a.text""",
            r"""base_url + subsoup.a.attrs['href']""",
            r"""re.findall(r"\d+\.?\d*", subsoup.find("p", {"class": "xg1"}).text)[0]""",
            r"""re.findall(r"\d+\.?\d*", subsoup.find("p", {"class": "xg1"}).text)[1]""",
            r"""subsoup.span.text""",
            r"""subsoup.findAll("a", {"target":"_blank"})[-1].text""",
            r"""subsoup.findAll("a", {"target":"_blank"})[-2].text""",
        ]
        # print(len(soup))
        for subsoup in soup:
            for i in scrape_code:
                try:
                    info.append(eval(i))
                except Exception as e:
                    info.append(np.nan)
            write_result(info)
            info = []

def write_result(result):
    if result:
        with open('c:/pwork/生据.csv', 'a', newline='', encoding='utf_8_sig') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(result)

if __name__ == "__main__":
    link = str(input("请输入你要检索的网页："))
    links = searchPage(link)
    write_result(['title', 'url', 'comment', 'views', 'date', 'section', 'author'])
    for id, i in enumerate(links):
        scrape(i)
        print(f"已完成 {round(id/len(links)*100, 2)}%。")
    print("done")


```

