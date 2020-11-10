#! /usr/bin/env python3

import requests
import re
import os

# 导入库
#       requests：http客户端库
#       re：正则表达式库
#       os：系统库

if not os.path.exists('./wallpaper/people'):
        os.mkdir('./wallpaper/people')
# 调用os系统库，如果./wallpaper不存在则创建


url = 'http://www.obzhi.com/category/renwubizhi'
#url = 'http://www.obzhi.com/category/fengjingbizhi/page/2'
# 指定需要下载的网站地址
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
        }
# 指定请求的系统及浏览器信息

page_text = requests.get(url=url,headers=headers).text
# 把主页的文件以文本的形式下载下来

#<div class="thumbnail">
#<a href="http://www.obzhi.com/4193.html" class="zoom" rel="bookmark" target="_blank" title="蓝色棕榈树">
#<img src="http://www.obzhi.com/wp-content/themes/Loostrive2/timthumb.php?src=http://www.obzhi.com/wp-content/uploads/2020/10/zonglv.jpg&amp;h=200&amp;w=300&amp;zc=1" width="300" height="200" alt="蓝色棕榈树">
#<div class="zoomOverlay"></div>
#</a>
#</div>

zz1 = '<div class="thumbnail">.*?src=".*?src=(.*?)&amp.*?</div>'
# 调用正则库分析实际图片地址
img_src_list = re.findall(zz1,page_text,re.S)
# 利用正则工具把图片实际地址保存为列表

for src in img_src_list:
        img_deta = requests.get(url=src,headers=headers).content
        img_name = src.split('/')[-1]
        img_path = './wallpaper/people/'+img_name
        with open(img_path,'wb') as fp:
                fp.write(img_deta)
                print(img_name,'下载成功')
# 循环把img_src_list中的图片地址下载下来
