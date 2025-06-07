from bs4 import BeautifulSoup
import requests
from pypdf import PdfReader

parts=[]

def scraper_name(file):
    reader = PdfReader(file)
    number_of_pages = len(reader.pages)
    print(number_of_pages)

    text = ""

    for page in reader.pages:
        text += page.extract_text(extraction_mode="layout", layout_mode_space_vertically=True)

    page.extract_text(visitor_text=visitor_body)
    text_body = "".join(parts)

    # print(f"textbody: {text_body} parts: {parts}")

    return text_body

def visitor_body(text, cm, tm, font_dict, font_size):
    y = cm[5]
    if 50 < y < 720:
        parts.append(text)

