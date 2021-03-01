shop_list_dic_3c = {
        '0': {'name':'Apple - iPhone','price':'8888'},
        '1': {'name':'XiaoMi - Phone','price':'6666'},
        '2': {'name':'XiaoMi - 扫地机器人','price':'1999'},
        '3': {'name':'Happy Hacking Keyboard','price':'2333'},
        '4': {'name':'Nintendo Switch','price':'2000'},
        '5': {'name':'Apple - Macbook Pro','price':'10000'},
        '6': {'name':'Amazon - Kindle','price':'999'},
        '7': {'name':'PC','price':'3000'},
        '8': {'name':'XiaoMi - Power Bank','price':'200'},
        '9': {'name':'XiaoMi - Headset','price':'299'},
        '10': {'name':'Sony - PlayStation','price':'1999'}
        }


shop_list_dic_book = {
        '0': {'name': '编码','price': '88'},
        '1': {'name': '计算机原理','price': '90'},
        '2': {'name': '数学家讲解小学数学','price': '80'},
        '3': {'name': '经济学原理','price': '120'},
        '4': {'name': '棉花帝国','price': '88'},
        '5': {'name': 'VIM实用技巧','price': '45'},
        '6': {'name': '中国历代政治得失','price': '99'},
        '7': {'name': '三体','price': '120'},
        '8': {'name': '中苏关系史纲','price': '99'},
        '9': {'name': '围城','price': '35'},
        '10': {'name': '中国国家治理的制度逻辑','price': '25'}
        }

def shopping():
    import json
    from conf import settings
    with open(settings.ChanPin1,'wt',encoding='utf-8') as f:
        f_3c_json = json.dumps(shop_list_dic_3c,ensure_ascii=False)
        book_json = json.dumps(shop_list_dic_book,ensure_ascii=False)
        f.write(f_3c_json)
        f.write(book_json)
        print(f)


shopping()



