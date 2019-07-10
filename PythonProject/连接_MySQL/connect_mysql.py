# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 19:18:39 2018

@author: 14403
"""

import pymysql 
pymysql.install_as_MySQLdb() 
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='test') #这里写上面设置的密码  
cursor = conn.cursor()  
cursor.execute("SELECT VERSION()")  
row = cursor.fetchone()  
print("MySQL server version:", row[0])  
cursor.close()  
conn.close()  