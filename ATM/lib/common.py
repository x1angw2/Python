# 存放公共方法
import hashlib

# 密码加密
def get_pwd_md5(password):
    md5_obj = hashlib.md5()
    md5_obj.update(password.encode('utf-8'))
    salt = '苍茫的天涯是我的爱!'
    md5_obj.update(salt.encode('utf-8'))

    return md5_obj.hexdigest()

# 登录认证装饰器
def login_auth(func):
    from core import src
    def inner(*args,**kwargs):
        if src.login_user:
            res =func(*args,**kwargs)
            return res
        else:
            print('您还没有登录,请登录后操作!')
            src.login()
    return inner


