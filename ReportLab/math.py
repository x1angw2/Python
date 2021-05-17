from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('FZKT','FangZhengKaiTi.ttf'))
# 注册字体
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,Image,Table,TableStyle,Frame,ListFlowable, ListItem

from reportlab.lib.pagesizes import A4,B9,LETTER


elements = []

Title = '每日一练'
Subtitle = '(二年级数学下册)'
name = '张三'
student_name = '姓名: ' + '张三'

YI = '一: 口算'
easy = ['7 × 9 = ', '67 + 23 = ', '56 - 22 = ', '7 × 6 = ', '33 + 60 = ', '61 + 14 = ', '44 - 31 = ', '130 + 620 = ', '93 - 69 = ', '79 - 32 = ', '10 ÷ 2 = ', '63 ÷ 9 = ']

ER = '二: 比算'
check = ['690 + 154 = ', '674 + 233 = ', '634 + 343 = ', '469 + 857 = ', '464 - 293 = ', '723 - 394 = ', '421 - 245 = ', '651 - 191 = ', '399 - 119 = ', '619 - 380 = ', '512 - 438 = ', '641 - 639 = ', '645 - 472 = ', '315 + 691 = ', '591 - 224 = ', '355 - 151 = ', '88 + 860 = ', '853 + 399 = ', '468 - 258 = ', '156 + 85 = ']

SAN = '三: 问题解决'



world_title_style = ParagraphStyle(
        name = 'title_Style',
        fontName = 'py',
        fontSize = 35,
        leading = 0,
        alignment = 1,
        spaceAfter = 6
    )
world_class_name_style = ParagraphStyle(
        name = 'class_and_Style',
        fontName = 'py',
        fontSize = 25,
        leading = 30,
        alignment = 0,
        spaceAfter = 6
    )



# elements.append(Paragraph(world_title,style=world_title_style))
# elements.append(Spacer(1,0.7*inch))
# elements.append(Paragraph(world_class_name,style=world_class_name_style))
# elements.append(Spacer(1,0.2*inch))

doc = SimpleDocTemplate(
    name + ".pdf",
    pagesize = A4,
    topMargin = 20,
    bottomMargin = 20
    )

doc.build(elements)
