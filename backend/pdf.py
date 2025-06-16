# importing modules
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from io import BytesIO

class PDF:
    def __init__(self, name, title, contact, experiences, type):
        self.name = name
        self.title = title
        self.contact = contact
        self.experiences = experiences
        self.type = type
        self.buffer = BytesIO()

    def print_details(self):
        print(self.name, self.contact, self.type)

    def create_pdf(self):
        pdf = canvas.Canvas(self.buffer)

        pdf.drawString(100, 750, self.title)

        pdf.save()
        self.buffer.seek(0) 
        return self.buffer

# c = canvas.Canvas("resume.pdf")
# c.save()