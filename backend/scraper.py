from bs4 import BeautifulSoup
import requests
from pypdf import PdfReader

def scraper_name(file):
    reader = PdfReader(file)
    number_of_pages = len(reader.pages)
    print(number_of_pages)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text

def print_link(link):
    print("scraper running")
    return print(link)