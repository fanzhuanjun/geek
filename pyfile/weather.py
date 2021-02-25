import requests
import pandas as pd
from urllib.parse import urlencode

def getData(startdate):
    url = 'https://api.weather.com/v1/location/ZSPD:9:CN/observations/historical.json?apiKey=6532d6454b8aa370768e63d6ba5a832e&units=e&startDate=' + startdate
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    }
    try:
        req = requests.get(url, headers=headers)
        data = pd.DataFrame(req.json()['observations'])
        colName = data.columns.tolist()
        colName.insert(0, 'date')
        data = data.reindex(columns=colName)
        data['date'] = startdate
        return data        
    except Exception as e:
        print(e)

startdate = '20200101'
enddate = '20200601'


def main():
    dateRange = pd.date_range(start=startdate, end=enddate, freq='D')
    date = [date for date in dateRange.strftime('%Y%m%d')]
    mapList = map(getData, date)
    df = pd.concat(mapList, axis=0)
    df.to_csv('c:/pwork/weather.csv')
    print(f'done!总列数为{df.shape}')

if __name__ == "__main__":
    main()