# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import csv
import time

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    # 输入
    df = pd.read_csv('result.csv',dtype=object,header=0,sep=',',encoding='UTF-8')
    # print(df)
    head = df.columns
    # print(head)
    stockList = df['code'].values.tolist()
    # print(stockList)

    urlBase = 'http://pinggu.stock.hexun.com/StockTotal.aspx?code='
    # for i in range(0, len(stockList)):
    for i in range(0, 187):
        # 休眠
        time.sleep(2)

        code = stockList[i]
        print(code)
        url = urlBase + code
        # print(url)
        # 抓取
        req = requests.get(url, headers=headers)
        req = requests.get(url, headers=headers)
        req.encoding = 'GBK'
        html = req.text 
        # 美丽汤
        try:
            bf = BeautifulSoup(html, features='html.parser')
            tr = bf.find_all('div', id = 'caiwupingguCnt1')[0].table.find_all('tr')

            for j in range(2,9):
                name = tr[j].find_all('td')[0].text
                score = tr[j].find_all('td')[1].text
                # print(name, score)
                df.iloc[i, j] = score
        except:
            for j in range(2,9):
                df.iloc[i, j] = 'null'
    # 输出
    df.to_csv('result.csv',index=False) 
    print('finished.')