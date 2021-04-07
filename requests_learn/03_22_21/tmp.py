import requests

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"

headers = {'user-agent':user_agent}
r = requests.get('http://www.hc.gov.cn/xxgk/gggs/index.html',headers = headers)

# print(r.content.decode('utf-8'))
print(r.request.headers)
# print(r.request.headers)
