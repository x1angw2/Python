import requests
import time
from bs4 import BeautifulSoup
import lxml

url_default = 'http://www.hc.gov.cn/xxgk/gggs/index.html'
url_number = 'http://www.hc.gov.cn/xxgk/gggs/index_1.html'
url = []

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
Connection = 'close'   # 不持久连接
headers = {'user_agent':user_agent,'Connection':Connection}

# 获取URL
def get_url(url_link):
    for i in range(1,25):
        new_url = url_link.replace('1',str(i))
        url.append(new_url)
def get_article(url,title_link):
    url.split[0:30]

# 获取页面数据
def get_url_data(url):
    requests.adapters.DEFAULT_RETRIES = 5
    try:
        response_index = requests.get(url,headers=headers)
        return response_index
    except requests.exceptions.ProxyError:
        response_index = requests.get(url,headers=headers)
        return response_index

# 解析页面数据
# 1) 分析每页文章地址及标题
def index_soup(html_data):
    soup = BeautifulSoup(html_data,'lxml')
    article_title_and_link =  soup.find_all('div',class_='lbbox_n')
    get_article(url_default,article_title_and_link)


# 保存数据
def save_data(data,url):
    url_list = url.split('/')
    with open(url_list[-1],'wb') as f:
        data = data.content
        f.write(data)

if __name__ == '__main__':
    # 添加第0页url地址到url列表
    url.append(url_default)
    # 添加剩余的url地址到url列表
    get_url(url_number)
    for i in url:
        index_data = get_url_data(i)
        print('%s 获取成功!'%i)
        time.sleep(3)
        save_data(index_data,i)
