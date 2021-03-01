# 教师视图

def login():
    pass

def check_score():
    pass

def chooce_course():
    pass

def check_stu_from_source():
    pass

def change_score_from_student():
    pass

func_dict = {
        '1':login,
        '2':check_score,
        '3':chooce_course,
        '4':check_stu_from_source,
        '5':change_score_from_student,
        }

def teacher_view():
    while True:
        print('''
            - 1. 登陆
            - 2. 查看教授课程
            - 3. 选择教授课程
            - 4. 查看课程下学生
            - 5. 修改学生分数
            - q. 返回上一层
        ''')

        choice = input('请输入功能编号: ').strip()

        if choice == 'q':
            break

        if choice not in func_dict:
            print('您的输入有误,请重新输入!')
            continue

        func_dict.get(choice)()
