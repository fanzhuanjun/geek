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
endDate = '2019-01-02'

if __name__ == "__main__":
    pool = Pool(10)
    date = pd.date_range(startDate, endDate)
    dates = [str(d)[:10] for d in date]
    pool.map(main, dates)
    pool.close()
    pool.join()

    print(f'样本数为: {len(date) * 48}。')