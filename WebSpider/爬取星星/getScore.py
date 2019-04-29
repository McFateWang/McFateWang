# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import csv
import time

if __name__ == '__main__':
    # 输入
    df = pd.read_csv('result.csv',dtype=object,header=0,sep=',',encoding='UTF-8')
    print(df)
    # head = df.columns
    # print(head)
    # stockList = df['code'].values.tolist()
    # print(stockList)

    df = df.replace('★★★★★', 5)
    df = df.replace('★★★★☆', 4.5)
    df = df.replace('★★★★', 4)
    df = df.replace('★★★☆', 3.5)
    df = df.replace('★★★', 3)
    df = df.replace('★★☆', 2.5)
    df = df.replace('★★', 2)
    df = df.replace('★☆', 1.5)
    df = df.replace('★', 1)
    df = df.replace('☆', 0.5)

    # 输出
    df.to_csv('result_score.csv',index=False) 
    print('finished.')