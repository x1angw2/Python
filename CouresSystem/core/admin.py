# 管理员视图

def register():
    pass

def login():
    pass

def create_school():
    pass

def create_course():
    pass

def create_teachear():
    pass

func_dict = {
        '1':register,
        '2':login,
        '3':create_school,
        '4':create_course,
        '5':create_teachear,
        }

def admin_view():
    while True:
        print('''
            - 1. 注册
            - 2. 登陆
            - 3. 创建学校
            - 4. 创建课程
            - 5. 创建讲师
            - q. 返回上一层
        ''')


        choice = input('请输入功能编号: ').strip()

        if choice == 'q':
            break

        if choice not in func_dict:
            print('您的输入有误,请重新输入!')
            continue

        func_dict.get(choice)()
