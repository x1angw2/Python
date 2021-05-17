import requests
from bs4 import BeautifulSoup

login_url = 'http://183.64.133.160:6186/Function/Login/login.html'
# login_url = 'http://183.64.133.160:6186/'



header = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': '_login_error=overdue; ASP.NET_SessionId=13ix5jewchbhlkpm5v305w2b',
'Host': '183.64.133.160:6186',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
}
s = requests.Session()

r = s.get(url=login_url,headers=header)

r.encoding = 'utf-8'
print(r.status_code)
print(r.text)

with open('login.html','wt',encoding='utf-8') as f:
    f.write(r.text)
