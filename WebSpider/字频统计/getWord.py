import urllib
from urllib.request import urlopen
import requests
import re

headers = {
    'Cookie': 'JSESSIONID=0000l3JAGT0gnf9-LSI3Bwy19Dx:1923sjkib; wzws_cid=1e005b421662f6f5cbea9eb23eb783aea00f080d41997026e190ea1a862ec74938a4120f6b4b7b896e906ea6107a640fba02bdad1a98db59b1945a9ae9ed19010355142800add52839cdff88c78a3a81',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
}

url = 'http://wzdt.pbc.gov.cn:8080/eportal/ui?struts.portlet.action=/app/interviewFront!getLiveInfo.action&pageId=134250&moduleId=20447&themeId=cb71af78972a4cb9bb0b79bc2903f8a9'
word = '企业'
r = requests.get(url, headers=headers)
r.encoding = 'utf-8'
html = r.text
print('网页信息： \n', html, '\n')

wordlist = re.findall(re.compile(word),html)
print('word is : ', word, ' number is : ', len(wordlist))