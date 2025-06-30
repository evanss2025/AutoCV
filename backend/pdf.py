# importing modules

#NOTICE: I used chatGPT to aid me in designing the pdf resume designs due to the repetitive, and boring trial and error
#proccess of them

from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Frame, PageTemplate, FrameBreak, Table, TableStyle
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_LEFT
import reportlab
from io import BytesIO
from reportlab.platypus import HRFlowable

pdfmetrics.registerFont(TTFont("Merriweather", "fonts/Merriweather_36pt-Regular.ttf"))

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
        if (self.type) == "ivy-league":
            self.ivy_league_resume()
        elif (self.type) == "single-column":
            self.single_column_resume()
        # elif (self.type) == "classic":
        #     self.classic_resume()
        else:
            print("no type defined")
        
        self.buffer.seek(0)
        return self.buffer
    
    def ivy_league_resume(self):
        self.buffer.seek(0)
        doc = SimpleDocTemplate(self.buffer, topMargin=0.5*inch, bottomMargin=0.5*inch, leftMargin=0.5*inch, rightMargin=0.5*inch)

        styles = getSampleStyleSheet()
        header = ParagraphStyle('header', parent=styles['Heading1'], fontSize=22, leading=22, spaceAfter=2, fontName="times-roman", uppercase=True, alignment=TA_CENTER)
        contact = ParagraphStyle('subheader', parent=styles['Heading2'], fontSize=10, leading=8, textColor=colors.HexColor("#242425"), spaceAfter=5, fontName="times-roman", alignment=TA_CENTER)
        subheader = ParagraphStyle('subheader', parent=styles['Heading2'], fontSize=10, leading=8, textColor=colors.HexColor("#242425"), spaceAfter=8, fontName="times-roman")
        normal = ParagraphStyle('normal', parent=styles['Normal'], fontSize=10, leading=14, spaceAfter=10, textColor=colors.HexColor("#1D1D1D"), fontName="times-roman")
        bullet = ParagraphStyle('bullet', parent=styles['Normal'], fontSize=10, leading=13, leftIndent=12, bulletIndent=6, spaceAfter=8, fontName="times-roman")
        section_title = ParagraphStyle('section_title', parent=styles['Heading2'], fontSize=14, textColor=colors.HexColor("#000000"), fontName="times-roman", spaceBefore=12, spaceAfter=4, alignment=TA_CENTER)
        details = ParagraphStyle('section_title', parent=styles['Heading2'], fontSize=9, textColor=colors.HexColor("#000000"), spaceBefore=3, spaceAfter=3, fontName="times-roman", alignment=TA_RIGHT)

        story = []

        story.append(Paragraph(f"<b>{(self.name).upper()}</b>", header))
        story.append(Spacer(1, 2))

        contact_string = ""
        if isinstance(self.contact, list):
            contact_string = " | ".join(self.contact)
        elif isinstance(self.contact, str):
            contact_string = self.contact
        story.append(Paragraph(contact_string, contact)) 

        if self.summary:
            summary = " ".join(self.summary) if isinstance(self.summary, list) else self.summary
            story.append(Paragraph("Summary", section_title))
            story.append(HRFlowable(width="100%", thickness=1, lineCap='round', color=colors.HexColor('#333333')))
            story.append(Spacer(1, 8)) 
            story.append(Paragraph(summary, normal))

        if self.experiences:
            story.append(Paragraph("Experience", section_title))
            story.append(HRFlowable(width="100%", thickness=1, lineCap='round', color=colors.HexColor('#333333')))
            story.append(Spacer(1, 8)) 

            for i, exp in enumerate(self.experiences):
                if i < 3:
                    left_top = Paragraph(f"<b>{exp['company']}</b>", subheader)
                    left_bottom = Paragraph(exp['title'], normal)

                    right_top = Paragraph(exp.get('location', ''), details)
                    right_bottom = Paragraph(exp.get('date', ''), details)

                    data = [
                        [left_top, right_top],
                        [left_bottom, right_bottom],
                    ]

                    table = Table(data, colWidths=[doc.width * 0.65, doc.width * 0.35])
                    table.setStyle(TableStyle([
                        ("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("ALIGN", (1, 0), (1, -1), "RIGHT"),
                        ("LEFTPADDING", (0, 0), (-1, -1), 0),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                        ("TOPPADDING", (0, 0), (-1, -1), 0),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
                    ]))

                    story.append(table)

                    if exp.get('description'):
                        story.append(Paragraph(exp['description'], bullet))

        if self.education:
            story.append(Paragraph("Education", section_title))
            story.append(HRFlowable(width="100%", thickness=1, lineCap='round', color=colors.HexColor('#333333')))
            story.append(Spacer(1, 8)) 

            title = ""
            date = ""

            for i in range(0, len(self.education), 2):
                title = self.education[i]
                date = self.education[i + 1] if i + 1 < len(self.education) else ""
                left_top = Paragraph(f"<b>{title}</b>", subheader)
                right_top = Paragraph(f"{date}", details)

                data = [
                    [left_top, right_top],
                ]

                table = Table(data, colWidths=[doc.width * 0.65, doc.width * 0.35])
                table.setStyle(TableStyle([
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("ALIGN", (1, 0), (1, -1), "RIGHT"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 0),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                    ("TOPPADDING", (0, 0), (-1, -1), 0),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
                ]))

                story.append(table)

        if self.awards:
            story.append(Paragraph("Key Achievements", section_title))
            story.append(HRFlowable(width="100%", thickness=1, lineCap='round', color=colors.HexColor('#333333')))
            story.append(Spacer(1, 5))
            awards_text = " · ".join(self.awards)
            story.append(Paragraph(awards_text, subheader))

        if self.skills:
            story.append(Paragraph("Skills", section_title))
            story.append(HRFlowable(width="100%", thickness=1, lineCap='round', color=colors.HexColor('#333333')))
            story.append(Spacer(1, 5))
            awards_text = " · ".join(self.skills)
            story.append(Paragraph(awards_text, subheader))

        if self.certifications:
            story.append(Paragraph("Certifications", section_title))
            story.append(HRFlowable(width="100%", thickness=1, lineCap='round', color=colors.HexColor('#333333')))
            story.append(Spacer(1, 5))
            awards_text = " · ".join(self.certifications)
            story.append(Paragraph(awards_text, subheader))


        doc.build(story)

        self.buffer.seek(0)
        return self.buffer

    def single_column_resume(self):
        self.buffer.seek(0)
        doc = SimpleDocTemplate(self.buffer, topMargin=0.3*inch, bottomMargin=0.3*inch, leftMargin=0.3*inch, rightMargin=0.3*inch)

        styles = getSampleStyleSheet()
        header = ParagraphStyle('header', parent=styles['Heading1'], fontSize=26, leading=22, spaceAfter=6)
        subheader = ParagraphStyle('subheader', parent=styles['Heading2'], fontSize=10, leading=14, textColor=colors.HexColor("#216BCC"), spaceAfter=10)
        normal = ParagraphStyle('normal', parent=styles['Normal'], fontSize=10, leading=14, spaceAfter=6)
        bullet = ParagraphStyle('bullet', parent=styles['Normal'], fontSize=10, leading=13, leftIndent=12, bulletIndent=6, spaceAfter=3)
        section_title = ParagraphStyle('section_title', parent=styles['Heading2'], fontSize=13, textColor=colors.HexColor("#000000"), spaceBefore=12, spaceAfter=4, uppercase=True)
        details = ParagraphStyle('section_title', parent=styles['Heading2'], fontSize=8, textColor=colors.HexColor("#000000"), spaceBefore=3, spaceAfter=3)
        
        story = []

        # name
        story.append(Paragraph(f"<b>{self.name}</b>", header))
        story.append(Spacer(1, 2)) 

        # contact
        contact_string = ""
        if isinstance(self.contact, list):
            contact_string = " | ".join(self.contact)
        elif isinstance(self.contact, str):
            contact_string = self.contact
        story.append(Paragraph(contact_string, subheader))

        # sum
        if self.summary:
            summary = " ".join(self.summary) if isinstance(self.summary, list) else self.summary
            story.append(Paragraph("SUMMARY", section_title))
            story.append(HRFlowable(width="100%", thickness=2, lineCap='round', color=colors.HexColor('#333333')))
            story.append(Spacer(1, 8)) 
            story.append(Paragraph(summary, normal))

        # experiences
        if self.experiences:
            story.append(Paragraph("EXPERIENCE", section_title))
            story.append(HRFlowable(width="100%", thickness=2, lineCap='round', color=colors.HexColor('#333333')))
            story.append(Spacer(1, 8)) 
            for i, exp in enumerate(self.experiences):
                if i < 3:
                    detail_line = ""
                    story.append(Paragraph(f"<b>{exp['company']}</b>", subheader))
                    story.append(Paragraph(exp['title'], normal))
                    if exp['date']:
                        detail_line += exp['date']
                    if exp['location']:
                        detail_line += f", {exp['location']}"

                    story.append(Paragraph(detail_line, details))

                    if exp['description']:
                        story.append(Paragraph(exp['description'], bullet))

        # edu
        if self.education:
            story.append(Paragraph("EDUCATION", section_title))
            story.append(HRFlowable(width="100%", thickness=2, lineCap='round', color=colors.HexColor('#333333')))
            story.append(Spacer(1, 2)) 
            for i, edu in enumerate(self.education):
                if i % 2 == 0:
                    story.append(Paragraph(edu, subheader))
                else:
                    story.append(Paragraph(edu, bullet))

        # awards
        if self.awards:
            story.append(Paragraph("KEY ACHIEVEMENTS", section_title))
            story.append(HRFlowable(width="100%", thickness=2, lineCap='round', color=colors.HexColor('#333333')))
            story.append(Spacer(1, 5))
            awards_text = " | ".join(self.awards)
            story.append(Paragraph(awards_text, subheader))

        story.append(Spacer(1, 12))
        doc.build(story)

        self.buffer.seek(0)
        return self.buffer
    
    def classic_resume(self):
        print("classic")
