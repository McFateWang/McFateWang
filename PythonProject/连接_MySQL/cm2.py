# -*- coding: utf-8 -*-

import mysql.connector
conn = mysql.connector.connect(user='root', password='', database='mysql')
cursor = conn.cursor()
cursor.execute('select * from user')
values = cursor.fetchall()
print(values)
