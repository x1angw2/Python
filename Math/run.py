import random
import os,sys,time
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,Image,Table,TableStyle,Frame,ListFlowable, ListItem
from reportlab.lib.enums import TA_JUSTIFY,TA_CENTER,TA_LEFT
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4,B9,LETTER
from reportlab.lib.units import inch

def number_one():
    number_1 = random.randint(1,9)
    number_2 = random.randint(11,100)
    return number_1,number_2

def multiply_and_divide():
    a = number_one()[0]
    b = number_one()[0]
    c = a * b
    str_multiply = str(a) + ' × ' + str(b) + ' ='
    str_divide = str(c) + ' ÷ ' + str(a) + ' ='
    return str_multiply,str_divide

def plus_and_divide():
    while True:
        a = number_one()[1]
        b = number_one()[1]
        c = a + b
        if c < 101:
            str_plus = str(a) + '+' + str(b) + '='
            str_minus = str(c) + '-' + str(a) + '='
            return str_plus,str_minus

def data_equation():
    l2 = []
    count_2 = 0
    while count_2 < 20:
        l1 = []
        count_1 = 0
        while count_1 < 4:
           # l1 = []
            random_number = random.randint(0,3)
            if random_number == 0:
                a = plus_and_divide()[0]
                l1.append(a)
                count_1 += 1
            if random_number == 1:
                a = plus_and_divide()[1]
                l1.append(a)
                count_1 += 1
            if random_number == 2:
                a = multiply_and_divide()[0]
                l1.append(a)
                count_1 += 1
            if random_number == 3:
                a = multiply_and_divide()[1]
                l1.append(a)
                count_1 += 1
        l2.append(l1)
        count_2 += 1
    return l2  

def class_name(class_name='class_name'):
    l1 = []
    for name_line in open(class_name,mode='rt',encoding='utf-8'):
        name = name_line.rstrip()
        l1.append(name)
    return l1

def typesetting(class_name_one):
    pdfmetrics.registerFont(TTFont('mysh','my.ttf'))
    pdfmetrics.registerFont(TTFont('py','Pinyin.ttf'))

    # Title
    elements = []

    world_title_style = ParagraphStyle(
            name = 'title_Style',
            fontName = 'py',
            fontSize = 35,
            leading = 0,
            alignment = TA_CENTER,
            spaceAfter = 6
        )
    world_class_name_style = ParagraphStyle(
            name = 'class_and_Style',
            fontName = 'py',
            fontSize = 25,
            leading = 30,
            alignment = TA_LEFT,
            spaceAfter = 6
        )
    world_title = '二年级数学上册计算练习题'
    world_class_name = '姓名:  ' + class_name_one
    elements.append(Paragraph(world_title,style=world_title_style))
    elements.append(Spacer(1,0.7*inch))
    elements.append(Paragraph(world_class_name,style=world_class_name_style))
    elements.append(Spacer(1,0.2*inch))

    # Table
    table_date = data_equation()
    table_style = [
            ('GRID',(0,0),(-1,-1),1,colors.black),
            ('FONTSIZE',(0,0),(-1,-1),18),
            ('ALIGN',(0,0),(-1,-1),'LEFT'),
            # ('FONTNAME',(0,0),(-1,-1),'mysh'),
            ('VALIGN',(0,0),(-1,-1),'MIDDLE')
            ]

    mytable = Table(table_date,colWidths=125,rowHeights=32)
    mytable_style = TableStyle(table_style)
    mytable.setStyle(mytable_style)

    elements.append(mytable)

    doc = SimpleDocTemplate(
        class_name_one + ".pdf",
        pagesize = A4,
        topMargin = 20,
        bottomMargin = 20
        )

    doc.build(elements)

class_name_list = class_name()
for class_name in class_name_list:
    typesetting(class_name)
    os.system('lp ' + class_name + '.pdf')
    print(class_name + '的练习题正在打印')
    os.system('rm ' + class_name + '.pdf')
    time.sleep(1)
    print(class_name + '的练习题已经完成')


