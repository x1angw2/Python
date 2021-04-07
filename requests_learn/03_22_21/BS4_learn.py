from bs4 import BeautifulSoup
import lxml

# Soup = BeautifulSoup(open('index.html'))

# print(Soup)
# print(Soup.get_text())

# print(Soup.div['class'])

# print(Soup.find_all('div',class_='lbbox_n'))
# print(type(Soup.find_all('div',class_='lbbox_n')))


with open('index.html','rt',encoding='utf-8') as f:
    html_data = f.read()
    # print(type(html_data))
    # print(html_data)

    Soup = BeautifulSoup(html_data,'lxml')
    print(type(Soup))
    title_link = Soup.find_all('div',class_='lbbox_n')
    print(type(title_link))
    title_link.find_all('a')
