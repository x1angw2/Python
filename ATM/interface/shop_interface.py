# 购物商场接口
from interface import bank_interface
from db import db_handler



# 商品准备结算接口
def shopping_interface(login_user,shopping_car):
    cost = 0
    for value in shopping_car.values():
        price,number = value

        cost += (price * number)

    res = bank_interface.pay_interface(login_user,cost)
    if res:
        return True,'支付成功,准备发货!'
    return False,'支付失败.余额不足!'

# 购物车添加接口
def add_shop_car_interface(login_user,shopping_car):
    user_dict = db_handler.select(login_user)

    shop_car = user_dict.get('shop_car')

    # shopping_car ==> {'商品名称':['单价',数量']}
    for shop_name,price_number in shopping_car.items():
        number = price_number[1]

        if shop_name in shop_car:
            user_dict['shop_car'][shop_name][1] += number
        else:
            user_dict['shop_car'].update(
                    {shop_name:price_number}
                    )

    db_handler.save(user_dict)

    return True,'添加购物车成功!'

def check_shop_cat(username):
    user_dict = db_handler.select(username)
    return user_dict.get('shop_car')
