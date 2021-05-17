from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
# 导入文档模板,段落,空格 class type
from reportlab.lib.styles import getSampleStyleSheet
# 导入提取文档模板  函数
from reportlab.rl_config import defaultPageSize
# 导入默认画布大小 tuple 595.2755905511812, 841.8897637795277
from reportlab.lib.units import inch
# 导入英寸 72.0 浮点数

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas

# 注册字体
pdfmetrics.registerFont(TTFont('FZKT','FangZhengKaiTi.ttf'))

PAGE_HEIGHT = defaultPageSize[1]
PAGE_WIDTH = defaultPageSize[0]
styles = getSampleStyleSheet()

Title = '每日一练'
Subtitle = '(二年级数学下册)'
student_name = '姓名: ' + '张三'
YI = '一: 口算'
ER = '二: 比算'
SAN = '三: 问题解决'
pageinfo = 'platypus example'

def titile_and_name(canvas, doc):
    canvas.saveState()
    # canvas.setFont('Times-Bold', 16)
    canvas.setFont('FZKT', 26)
    canvas.drawCentredString(PAGE_WIDTH/2.0-60, PAGE_HEIGHT-38, Title)
    canvas.setFont('FZKT',14)
    canvas.drawCentredString(PAGE_WIDTH/2.0+43, PAGE_HEIGHT-38, Subtitle)
    canvas.setFont('FZKT',18)
    canvas.drawCentredString(PAGE_HEIGHT/2.0,PAGE_HEIGHT-60, student_name)
    canvas.drawString(72,inch, student_name)
    # canvas.setFont('Times-Roman', 9)
    # canvas.drawString(inch, 0.75 * inch, "First Page / %s" % pageinfo)
    canvas.restoreState()

def KuoSuan(canvas,doc):
    canvas.saveState()
    canvas.setFont('FZKT',18)
    canvas.restoreState()




def myLaterPages(canvas,doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 9)
    canvas.drawString(inch,0.75*inch,"Page %d %s"%(doc.page, pageinfo))
    canvas.restoreState()

def run():
    doc = SimpleDocTemplate('phello.pdf')

    Story = [Spacer(1, 2 * inch)]
    style = styles['Normal']
    
    for i in range(100):
        bogustext  = ('Paragraph number %s.' %i) * 20
        p = Paragraph(bogustext, style)
        Story.append(p)
        Story.append(Spacer(1, 0.2 * inch))
    doc.build(Story,onFirstPage=titile_and_name,onLaterPages=myLaterPages)

if __name__ == '__main__':
    run()
