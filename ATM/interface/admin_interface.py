from db import db_handler

def change_balance_interface(username,money):
    user_dict = db_handler.select(username) 

    if user_dict:
        user_dict['balance'] = int(money)

        db_handler.save(user_dict)


        return True,'额度修改成功!'

    return False,'用户不存在'

def lock_user_interface(username):
    user_dict = db_handler.select(username)

    if user_dict:
        user_dict['locked'] = True

        db_handler.save(user_dict)
        
        return True,f'用户 {username} 冻结成功!'

    return False,'用户不存在,请重新输入'
