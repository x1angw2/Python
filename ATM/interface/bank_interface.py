# 银行相关业务接口
from db import db_handler

# 提现接口
def withdraw_interface(username,money):
    # 1.先获取用户字典,用于校验余额是否满足提现
    user_dict = db_handler.select(username)
    
    balance = int(user_dict.get('balance'))
    money2 = int(money) * 1.05

    # 2. 修改用户字典的金额
    if balance >= money2:
        balance -= money2
        user_dict['balance'] = balance

        # 记录流水
        flow = f'用户{username}提现{money}元,手续费{money2 - float(money)}元.余额{balance}元.'
        user_dict['flow'].append(flow)

        # 3. 保存数据
        db_handler.save(user_dict)
        return True,flow
    return False,'提现金额不足,请重新输入!'

# 还款接口
def repay_interface(username,money):
    # 获取用户字典/金额
    user_dict = db_handler.select(username)
    user_dict['balance'] += money

    # 记录流水
    flow = f'用户{username}还款{money}元成功!当前额度为{user_dict["balance"]}元.'
    user_dict['flow'].append(flow)
    # 保存字典
    db_handler.save(user_dict)

    return True,flow

# 转账接口
def transfer_interface(login_user,to_user,money):
    # 获取当前用户数据
    # 获取目标用户数据
    # 获取转账金额
    login_user_dic = db_handler.select(login_user)
    to_user_dic = db_handler.select(to_user)

    # 先判断收款人是否存在
    if not to_user_dic:
        return False,f'目标用户不存在'

    # 判断金额是否足够
    if login_user_dic['balance'] >= money:
        # 当前用户减钱操作
        login_user_dic['balance'] -= money
        # 目标用户加钱操作
        to_user_dic['balance'] += money

        # 记录流水 当前用户  目标用户
        login_user_flow = f'用户 {login_user} 给用户 {to_user} 转账 {money}元成功.'
        login_user_dic['flow'].append(login_user_flow)

        to_user_flow = f'用户 {to_user} 接收 用户 {login_user} 转账 {money}元成功.'
        to_user_dic['flow'].append(to_user_flow)

        # 保存修改后的数据
        db_handler.save(login_user_dic)
        db_handler.save(to_user_dic)
        
        return True,login_user_flow
    return False,'当前用户余额不足无法转账'

# 查看流水接口
def check_flow_interface(login_user):
    user_dict = db_handler.select(login_user)

    return user_dict.get('flow')

# 支付接口
def pay_interface(login_user,cost):
    user_dict = db_handler.select(login_user)

    if user_dict.get('balance') >= cost:
        user_dict['balance'] -= cost

        flow = f'用户消费金额{cost}元'
        user_dict['flow'].append(flow)

        db_handler.save(user_dict)

        return True,'支付成功,准备发货!'
    return False,'支付失败,余额不足!'
