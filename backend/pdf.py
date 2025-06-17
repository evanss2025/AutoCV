# importing modules
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import LETTER
from io import BytesIO

class PDF:
    def __init__(self, name, contact, summary, experiences, education, skills, languages, certifications, awards, type):
        self.name = name
        self.contact = contact
        self.summary = summary
        self.experiences = experiences
        self.education = education
        self.skills = skills
        self.languages = languages
        self.certifications = certifications
        self.awards = awards
        self.type = type
        self.buffer = BytesIO()

    def print_details(self):
        print(self.name, self.contact, self.summary, 
              self.experiences, self.education, self.skills, 
              self.languages, self.certifications, self.awards, self.type)

    def create_pdf(self):
        doc = SimpleDocTemplate(self.buffer, pagesize=LETTER)
        styles = getSampleStyleSheet()
        flowables = []

        if (self.type) == "google-resume":
            print("google doc")
        elif (self.type) == "ivy-league":
            print("ivy league")
        elif (self.type) == "stylish":
            print("stylish doc")
        elif (self.type) == "single-column":
            print("single column")
        elif (self.type) == "double-column":
            print("double column")
        elif (self.type) == "classic":
            print("classic")
        else:
            print("not type defined")

        
        pdf = canvas.Canvas(self.buffer, pagesize=LETTER)
        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawString(100, 750, f"Name: {self.name}")
        pdf.save()
        self.buffer.seek(0)
  

        flowables.append(Paragraph(f"<b>Type:</b> {self.type}", styles["Normal"]))
        flowables.append(Spacer(1, 0.2 * inch))

        flowables.append(Paragraph(f"<b>Contact:</b> {self.contact}", styles["Normal"]))
        flowables.append(Spacer(1, 0.2 * inch))

        flowables.append(Paragraph(f"<b>Summary:</b> {self.summary}", styles["Normal"]))
        flowables.append(Spacer(1, 0.2 * inch))

        flowables.append(Paragraph(f"<b>Experiences:</b> {self.experiences}", styles["Normal"]))
        flowables.append(Spacer(1, 0.2 * inch))

        flowables.append(Paragraph(f"<b>Education:</b> {self.education}", styles["Normal"]))
        flowables.append(Spacer(1, 0.2 * inch))

        flowables.append(Paragraph(f"<b>Skills:</b> {self.skills}", styles["Normal"]))
        flowables.append(Spacer(1, 0.2 * inch))

        flowables.append(Paragraph(f"<b>Languages:</b> {self.languages}", styles["Normal"]))
        flowables.append(Spacer(1, 0.2 * inch))

        flowables.append(Paragraph(f"<b>Certifications:</b> {self.certifications}", styles["Normal"]))
        flowables.append(Spacer(1, 0.2 * inch))

        flowables.append(Paragraph(f"<b>Awards:</b> {self.awards}", styles["Normal"]))

        doc.build(flowables)

        self.buffer.seek(0)
        return self.buffer