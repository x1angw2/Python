#! /usr/bin/env python3

import requests
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?'
dizhi = input("请输入需要查询的地址：")
pageIndex = input("页码")
keyword = {
    'cname': '',
    'pid': '',
    'keyword': dizhi,
    'pageIndex': pageIndex,
    'pageSize': '10',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
}

resonse = requests.get(url=url,params=keyword,headers=headers)
list_data = resonse.text()

fp = open('./kfc','w',encoding='utf-8')
fp.write(fp,encoding='utf-8')
print('DONE')

