import requests
import time
import re

login_url = 'http://183.64.133.160:6186/Function/Login/login.html'


post_url = 'http://183.64.133.160:6186/Function/ADataAshx/Login.ashx'


requestsHeaders = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
        }

mwAbB13yCulnqUAqB+FWCtBoM95AG8VhOF4gB1Y79k0HjQnlU9vq41U8Xr4oJPKgQFAd6P+uRhVxiTYOpiPWERB2ZmkiZ6aDqbqdhts30zbzvQDzPd1a6DxLmREdxMeoZ4FUpURgWDlZ/A00wPwMCyevvzfbmJrjg0g2UhnI28s=



data = {'action': 'CheckUserLogin',
        'userName': 'xuu2/C7++bMPixp7AC3ISnkMkwtCYPtBltifkNvwIqzxFJII7iDLlwOzJTmzpNw7aMy3tnFpA1sfZ9b/IVipP1MSIAJdUQWwJA9tXnsGqNkUZQ72Za/SqNfkQP1GUGxMH+HWZJF+WcSUaclSRpSVTBrc2GLh5ORg/Msg4d0fWWM=',
        'userPwd': 'oOjhTIVHNf+3O7mxxehQRw11F9FHwQwcokAN2Cgo9/NGmvPC/31lXASZSeAcR+ChrFHwEuOagCwBz8YZ/nUDtqph3d0JCl3UV+kMdGAE+P+ILchzDo4XpUHp7enJNtgJ3sVUxoDI6mIH6wXvN+HQbeGkhIchy1GmDLJ5M0sk/k0=',
        'code': 'epxx',
        'appid': '2436c88f-8c3b-4478-95c0-5dd7581eceab'
        }
        

def get_login(url):
    s = requests.Session()
    s.post(url)

http://183.64.133.160:19003/Home/HomeMain
