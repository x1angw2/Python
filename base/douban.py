#! /usr/bin/env python3

import requests
import json
url = 'https://movie.douban.com/j/chart/top_list'
cs = {
    'type': '11',
    'interval_id': '100:90',
    'action': '',
    'start': '0', # 从数据库中第几部中去取
    'limit': '10', # 取多少部
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
}

resonse = requests.get(url=url,params=cs,headers=headers)
list_data = resonse.json()

fp = open('./db.json','w',encoding='utf-8')
json.dump(list_data,fp=fp,ensure_ascii=False)
print('DONE')

