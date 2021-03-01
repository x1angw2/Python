# 用户视图层
from interface import user_interface
from interface import bank_interface
from lib import common
from interface import shop_interface

#  全局变量,记录用户是否登录
login_user = None

# 1. 注册功能
def register():
    while True:
        username = input('请输入用户名: ').strip()
        password = input('请输入密码: ').strip()
        re_password = input('请确认密码: ').strip()

        if password == re_password:
            flag,msg = user_interface.register_interface(username,password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码输入不一致,请重新输入!')

# 2. 登录功能
def login():
    while True:
        username = input('请输入用户名: ').strip()
        password = input('请输入密码: ').strip()

        flag,msg = user_interface.login_interface(username,password)
        if flag:
            print(msg)
            global login_user
            login_user = username

            break
        else:
            print(msg)

@common.login_auth
# 3. 查看余额
def check_balance():
    balance = user_interface.check_bal_interface(login_user)
    print(f'{login_user} 您好!你的账户余额为:{balance}元.')

@common.login_auth
# 4. 提现功能
def withdraw():
    while True:
        input_money = input('请输入提现金额:').strip()

        if not input_money.isdigit():
            print('请输入数字!')
            continue
        flag,msg = bank_interface.withdraw_interface(login_user,input_money)
        if flag:
            print(msg)
            break
        else:
            print(msg)

@common.login_auth
# 5. 还款功能
def repay():
    while True:
        input_money = input('请输入需要还款的金额: ').strip()

        if not input_money.isdigit():
            print('请输入正确的金额!')
            continue
        input_money = int(input_money)

        if input_money > 0:
            flag,msg = bank_interface.repay_interface(login_user,input_money)

            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('输入的金额不能小于0')

@common.login_auth
# 6. 转账功能
def transfer():
    while True:
    # 1. 输入 金额
    # 2. 输入 转账目标用户
        money = input('请输入转账金额: ').strip()
        to_user = input('请输入需要转出的用户: ').strip()

        # 判断用户输入金额为数字和大于0
        if not money.isdigit():
            print('请输入数字!')
            continue
        money = int(money)

        if money > 0:
            flag,msg = bank_interface.transfer_interface(login_user,to_user,money)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('您的输入有误,请重新输入!')

@common.login_auth
# 7. 查看流水
def check_flow():
    flow_list = bank_interface.check_flow_interface(login_user)

    if flow_list:
        for i in flow_list:
            print(i)
    else:
        print('当前用户没有流水!')

@common.login_auth
# 8. 购物功能
def shopping():
    # 从文件中读取商品信息
    # 不从文件中读取商品信息,直接写入
    shop_list = [
            ['麻辣牛肉',30],
            ['衣服',500],
            ['手机',3000],
            ['自行车',9000],
            ['Macbook',12000]
            ]

    # 初始化购物车
    shopping_car = {}

    while True:
        #打印商品信息
        for index,shop in enumerate(shop_list):
            shop_name,shop_price = shop
            print(f'商品编号:[{index}]',f'商品名称:[{shop_name}]',f'商品单价:[{shop_price}]元')

        # 让用户根据商品编号选择商品
        choice = input('请输入商品编号(输入y结账或者输入n添加购物车): ').strip()


        if choice == 'y':
            if not shopping_car:
                print('购物车为空,不能结账.请重新输入.')
                continue

            flag,msg = shop_interface.shopping_interface(login_user,shopping_car)
            if flag:
                print(msg)
                break
            else:
                print(msg)

        elif choice == 'n':
            if not shopping_car:
                print('购物车为空,不能添加到数据库.请重新输入.')
                continue
            flag,msg = shop_interface.add_shop_car_interface(login_user,shopping_car)
            if flag:
                print(msg)
                break


        # 判断用户是否输入数字
        if not choice.isdigit():
            print('请输入正确的编号!')
            continue

        choice = int(choice)
        # len(shop_list) == 5  range(5) = 4,3,2,1,0
        if choice not in range(len(shop_list)):
            print('请输入正确的编号!')
            continue

        # 拿到商品名称和商品单价
        shop_name,shop_price = shop_list[choice]

        #  加入购车之前先在接口层拿到购物车
        # 判断用户的购车车是否有数据,有则数据+1 没有则新填一条
        if shop_name in shopping_car:
            shopping_car[shop_name][1] += 1
            pass
        else:
            shopping_car[shop_name] = [shop_price,1]

        print('当前购物车: ',shopping_car)

@common.login_auth
# 9. 查看购物车
def check_shop_cat():
    shopping_car =  shop_interface.check_shop_cat(login_user)
    print(shopping_car)

@common.login_auth
# 10. 管理员功能
def admin():
    from core import admin
    admin.admin_run()

func_dict = {
        '1': register,
        '2': login,
        '3': check_balance,
        '4': withdraw,
        '5': repay,
        '6': transfer,
        '7': check_flow,
        '8': shopping,
        '9': check_shop_cat,
        '10': admin
        }

def run():
    while True:
        print('''
        ****** ATM + 购物车 ******
            1. 注册功能
            2. 登录功能
            3. 查看余额
            4. 提现功能
            5. 还款功能
            6. 转账功能
            7. 查看流水
            8. 购物功能
            9. 查看购物车
            10. 管理员功能
        ***************************
        ''')

        choice = input('请输入对应功能的编号: ').strip()

        if choice not in func_dict:
            print('您的输入有误,请从新输入编号!')
            continue

        func_dict.get(choice)()
