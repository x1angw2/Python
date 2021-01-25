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

