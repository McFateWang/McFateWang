import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
resp = requests.get('http://pm.weakcn.com/uploadfile/gx02/180728/dd01.jpg', headers=headers)
print(resp.content)  # 二进制文件使用content
# 保存图片
with open('logo.gif', 'wb') as f:
    f.write(resp.content)
    print('Ok')
resp.close()