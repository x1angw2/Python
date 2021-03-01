# 注册
'''
def register():
    while True:
        username = input('请输入用户名: ').strip()
        password = input('请输入密码: ').strip()
        re_password = input('请确认密码: ').strip()

        if password == re_password:
            import json
            from conf import settings
            import os 

            user_path = os.path.join(settings.USER_DATA_PATH,f'{username}.json')

            if os.path.exists(user_path):   #   如果文件存在

                with open(user_path,'r',encoding='utf-8') as f:
                    user_dic = json.load(f)
                if user_dic:
                    print('用户已经存在,请重新输入!')
                    continue

            else:
                user_dict = {
                        'username': username,
                        'password': password,
                        'balance': 15000,
                        'flow': [], # 记录用户流水的列表
                        'shop_car': {}, # 购物车 
                        'locked': False
                        }
                with open(user_path,'w',encoding='utf-8') as f:
                    json.dump(user_dict,f,ensure_ascii=False)

'''

