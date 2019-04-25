# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    url = 'http://pinggu.stock.hexun.com/StockTotal.aspx?code=000001'
    req = requests.get(url, headers=headers)
    req.encoding = 'GBK'
    html = req.text 
    # result = html
    # print(result)

    bf = BeautifulSoup(html, features='html.parser')
    texts = bf.find_all('div', id = 'caiwupingguCnt1')
    print(texts)
    # result = texts[0].text.replace('\xa0'*8,'\n')

    # with open('result.txt', 'w') as f:
    #         f.write(result)

    # print('finished.')

    # 'http://pinggu.stock.hexun.com/StockTotal.aspx?code=000001'
    # 'http://www.biqukan.com/1_1094/5403177.html'