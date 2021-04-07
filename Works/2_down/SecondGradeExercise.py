import random
import os
import sys
import time

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors


name = []

# 一:导入学生名册
def Student():
    with open('StudentName.txt','rt',encoding='utf-8') as f:
        for line in f.readlines():
            student_name = line.strip('\n')
            name.append(student_name)

# 二:生成口算练习题
# 1) 表内乘除
def TimesAndDic():
    multiplier_a = random.randint(2,9)
    multiplier_b = random.randint(2,9)
    product = multiplier_a * multiplier_b
    random_num = random.randint(1,2)
    if random_num == 1:
        topic = str(product) + ' ÷ ' + str(multiplier_a) + ' = '
        return topic
    else:
        topic = str(multiplier_b) + ' × ' + str(multiplier_a) + ' = '
        return topic
# 2) 口算加减
# def PlusAndMinus():
# 2.1) 口算100以内减法
def HundredDiff():
    while True:
        num_a = random.randint(11,99)
        num_b = random.randint(11,99)
        if num_a != num_b:
            if num_a > num_b:
                return str(num_a) + ' - ' + str(num_b) + ' = '
            else:
                return str(num_b) + ' - ' + str(num_a) + ' = '
        else:
            continue
# 2.2)  口算100以内加法
def HundredSum():
    while True:
        num_a = random.randint(11,80)
        num_b = random.randint(11,80)
        if num_a + num_b < 100:
            return str(num_a) + ' + ' + str(num_b) + ' = '
        else:
            continue
# 2.3) 口算不进/借位减法
def ThousandDiff():
    while True:
        num_a = random.randint(1,99) * 10
        num_b = random.randint(1,99) * 10
        if num_a != num_b:
            if (num_a / 100) % 10 > (num_b / 100) % 10:
                if (num_a / 10) %10 > (num_b / 10) % 10:
                    return str(num_a) + ' - ' + str(num_b) + ' = '
                else:
                    continue
            else:
                if (num_a / 10) %10 > (num_b / 10) % 10:
                    continue
                else:
                    return str(num_b) + ' - ' + str(num_a) + ' = '
        else:continue
# 2.4) 口算不进/借位加法
def ThousandSum():
    while True:
        num_a = random.randint(1,99) * 10
        num_b = random.randint(1,99) * 10
        if num_a != num_b:
            if ((num_a / 100) % 10 + (num_b / 100 ) % 10 ) < 10 and ((num_a / 10) % 10 + (num_b / 10 ) % 10 ) < 10:
                return str(num_a) + ' + ' + str(num_b) + ' = '
            else:continue
# 2.5) 随机生成算式   
def CreateEasyCompute():
    random_num = random.randint(1,5)
    if random_num == 1:
        Thousand_tuple = ThousandDiff()
        return Thousand_tuple
    elif random_num == 2:
        HundredSum_tuple = HundredSum()
        return HundredSum_tuple
    elif random_num == 3:
        HundredDiff_tuple = HundredDiff()
        return HundredDiff_tuple
    elif random_num == 4:
        ThousandSum_tuple = ThousandSum()
        return ThousandSum_tuple
    else:
        TimesAndDic_tuple = TimesAndDic()
        return TimesAndDic_tuple

# 三:生成笔算练习题
def CreateCompute():
    while True:
        num_a = random.randint(71,899)
        num_b = random.randint(71,899)
        if num_a > num_b:
            # sum_a = num_a + num_b
            # diff_a = num_a - num_b
            if random.randint(1,2) == 1:
                return str(num_a) + ' + ' + str(num_b) + ' = '
            else:
                return str(num_a) + ' - ' + str(num_b) + ' = '
        else:
            # sum_b = num_b + num_a
            # diff_b = num_b - num_a
            if random.randint(1,2) == 1:
                return str(num_a) + ' + ' + str(num_b) + ' = '
            else:
                return str(num_b) + ' - ' + str(num_a) + ' = '

# 四 生成笔算/口算练习题列表
def CreateComputeList(inside,outide,func):
    computelist = []
    for i in range(outide):
        nei = []
        for i in range(inside):
            l1 = func()
            nei.append(l1)
        computelist.append(nei)
    return computelist

# 四:生成问题解决练习题
def CreateQuestion():
    List = []
    with open('tmp.txt','rt',encoding='utf-8') as f:
        for line in f.readlines():
            if line != '\n':
                List.append(line.strip())

    num = random.randint(1,len(List)-1)
    question = List[num]

    num_a = random.randint(71,899)
    num_b = random.randint(71,899)
    if num_a != num_b:
        if '{low}' not in question:
            question1 = question.replace('{}',str(num_a),1)
            Question =  question1.replace('{}',str(num_b),1)
        else:
            if num_a > num_b:
                question1 = question.replace('{low}',str(num_b))
                Question = question1.replace('{hight}',str(num_a))
            else:
                question1 = question.replace('{low}',str(num_a))
                Question = question1.replace('{hight}',str(num_b))

    return Question

# 五:创建pdf文档
def CreatePDF(name,easycompute,compute,question):
    element = []
    pdf_file = SimpleDocTemplate(name + '.pdf',
                                pagesizes = A4,
                                rightMargin = 72,
                                leftMargin = 22,
                                topMargin = 20,
                                bottomMargin = 18
                                )

    # 注册字体
    pdfmetrics.registerFont(TTFont('FZKT','FangZhengKaiTi.ttf'))

    # 设置段落格式
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name = 'title01',
                            fontName = 'FZKT',
                            alignment = 1,
                            ))
    styles.add(ParagraphStyle(name = 'name',
                            fontName = 'FZKT',
                            # alignment = 2,
                            fontSize = 20,
                            leftIndent = 282,
                            ))
    styles.add(ParagraphStyle(name = 'subject',
                            fontName = 'FZKT',
                            alignment = 4,
                            fontSize = 18,
                            ))
    styles.add(ParagraphStyle(name = 'question',
                            fontName = 'FZKT',
                            leading = 24,
                            alignment = 4,
                            fontSize = 15,
                            ))

    # 添加titile
    title = '<font size=25>每日一练</font><font size=15>(二年级下册)</font>'
    element.append(Paragraph(title,styles['title01']))
    # 添加空格行
    element.append(Spacer(1,24))
    name_and_data = '姓名: ' + name
    element.append(Paragraph(name_and_data,styles['name']))
    element.append(Spacer(1,12))
    element.append(Paragraph('一:口算',styles['subject']))
    element.append(Spacer(1,12))

    # 表格样式
    table_style = TableStyle([('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                            ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                            ('FONTSIZE',(0,0),(-1,-1),14),
                            ('LEFTPADDING',(0,0),(-1,-1),28),
                            ('BOTTOMPADDING',(0,0),(-1,-1),9),
                            ])
    table_all_data = Table(easycompute, style=table_style)
    element.append(table_all_data)

    element.append(Paragraph('二:笔算',styles['subject']))
    element.append(Spacer(1,12))

    table_style1 = TableStyle([('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                            ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                            ('FONTSIZE',(0,0),(-1,-1),14),
                            ('RIGHTPADDING',(0,0),(-1,-1),80),
                            ('BOTTOMPADDING',(0,0),(-1,-1),100),
                            ('VALIGN',(0,0),(-1,-1),'TOP'),
                            ])

    table_all_data = Table(compute,style=table_style1)
    element.append(table_all_data)

    element.append(Paragraph('三:问题解决',styles['subject']))
    element.append(Spacer(1,12))
    element.append(Paragraph(question,styles['question']))

    pdf_file.build(element)

# class_name_list = class_name()
# for class_name in class_name_list:
#     typesetting(class_name)
#     os.system('lp ' + class_name + '.pdf')
#     print(class_name + '的练习题正在打印')
#     os.system('rm ' + class_name + '.pdf')
#     time.sleep(1)
#     print(class_name + '的练习题已经完成')

if __name__ == '__main__':
    Student()
    for i in name:
        easycompute = CreateComputeList(5,2,CreateEasyCompute)
        compute = CreateComputeList(3,4,CreateCompute)
        question = CreateQuestion()
        CreatePDF(name=i,easycompute=easycompute,compute=compute,question=question)
        os.system('lp ' + i + '.pdf')
        print(i + '的练习题正在打印.')
        os.system('rm ' + i + '.pdf')
        time.sleep(1)
        print(i + '的练习题已经完成!')



    # CreateEsayCompute()
    # CreateComputeList()
    # print(name)
    # print(esay_compute)
    # print(compute)
    # with open('test.txt','wt',encoding='utf-8') as f:
    #     f.write(str(name))
    #     f.write(str(esay_compute))
    #     f.write(str(compute))

