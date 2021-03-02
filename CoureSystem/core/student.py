# 学生视图

def register():
    pass

def login():
    pass

def choice_school():
    pass

def choice_course():
    pass

def check_score():
    pass

func_dict = {
        '1':register,
        '2':login,
        '3':choice_school,
        '4':choice_course,
        '5':check_score,
        }



def student_view():
    while True:
        print('''
            - 1. 注册
            - 2. 登陆
            - 3. 选择学校
            - 4. 选择课程
            - 5. 查看分数
            - q. 返回上一层
        ''')

        choice = input('请输入功能编号: ').strip()

        if choice == 'q':
            break

        if choice not in func_dict:
            print('您的输入有误,请重新输入!')
            continue

        func_dict.get(choice)()
