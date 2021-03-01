# 逻辑接口层
# 用户逻辑
from db import db_handler
from lib import common

# 注册接口
def register_interface(username,password,balance=15000):
    user_dict = db_handler.select(username)
        
    if user_dict:
        return False,'用户名已存在,请重新输入!'
    
    # 密码加密
    password = common.get_pwd_md5(password)

    user_dict = {
            'username': username,
            'password': password,
            'balance': balance,
            'flow': [], # 记录用户流水的列表
            'shop_car': {}, # 购物车 
            'locked': False
            }
    db_handler.save(user_dict)
    return True,f'{username}注册成功!'

#  登录接口
def login_interface(username,password):
    user_dict = db_handler.select(username)
    
    if user_dict.get('locked'):
        return False,'当前用户已被锁定'

    if user_dict:
        password = common.get_pwd_md5(password)
        if password == user_dict.get('password'):
            return True,f'用户:[{username}]登录成功!'
        else:
            return False,'密码错误'
    return False,'用户不存在,请重新输入!'

# 查看余额接口
def check_bal_interface(username):
    user_dict = db_handler.select(username)

    return user_dict['balance']
