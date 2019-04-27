import requests # 导入requests库，需要安装
 
# 模拟成浏览器访问的头
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
resp = requests.get('http://www.lfossh.com/',headers=headers)
print(resp.text) # 打印出网页源代码
print(resp.status_code) # 打印出状态码