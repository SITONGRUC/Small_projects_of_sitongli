import requests
import re
import json
import numpy as np
import pandas as pd
import datetime
def get_year_data(stock_code,freq,start,end,fq):
    headers = {"User-Agent": 'ozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
    end_date = datetime.datetime.strptime(end,'%Y-%m-%d')
    start_date = datetime.datetime.strptime(start,'%Y-%m-%d')
    vol = (end_date-start_date).days
    link = "https://proxy.finance.qq.com/ifzqgtimg/appstock/app/newfqkline/get?_var=kline_day"+fq+"&param="+stock_code+","+freq+","+start+","+end+","+str(vol)+","+fq
    response = requests.get(link,headers = headers)
    data = response.text
    data = json.loads(re.sub("kline_day"+fq+"=",'',data))
    data = pd.DataFrame(data['data'][stock_code][fq+'day'])
    data = data[[0,1,2,3,4,5]].copy()
    data.columns = ['日期','开盘价','收盘价','最高价','最低价','交易量']
    data['日期']=pd.to_datetime(data['日期'])
    data = data[data['日期']>=start_date].copy()
    for i in ['开盘价','收盘价','最高价','最低价','交易量']:
        data[i] = data[i].apply(lambda x:float(x))
    return data

#Example

if __name__ == '__main__':
    sh601919 = get_year_data('sh601919','day','2021-01-01','2021-12-31','qfq')
    sh601919.to_excel('ex.xlsx')

