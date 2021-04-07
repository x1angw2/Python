import time
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors

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
                            fontSize = 18,
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
name = 'jack'
easycompute = [['6 ÷ 2 = ', '650 - 430 = ', '260 - 20 = ', '920 - 110 = ', '62 + 21 = '], ['950 - 110 = ', '88 - 63 = ', '86 - 72 = ', '19 + 69 = ', '260 - 60 = ']]
compute = [['652 - 457 = ', '109 + 890 = ', '766 - 72 = '], ['620 - 450 = ', '239 + 570 = ', '441 - 288 = '], ['438 + 742 = ', '283 - 282 = ', '463 + 593 = '], ['577+ 250 = ', '835 - 326 = ', '349 + 480 = ']]
question = '电影院有446个座位,三星小学来看电影的学生有212人,还剩多少个座位?'

CreatePDF(name,easycompute,compute,question)
