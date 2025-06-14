# importing modules
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors

class PDF:
    def __init__(self, name, contact, experiences, type):
        self.name = name
        self.contact = contact
        self.experiences = experiences
        self.type = type

    def print_details(self):
        print(self.name, self.contact, self.type)

    def create_pdf():
        print('placeholder')
        #create pdf

# c = canvas.Canvas("resume.pdf")
# c.save()