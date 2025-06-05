from bs4 import BeautifulSoup
import requests

def scraper_name(link):
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, "lxml")

    name = "Sophia Evans" #testing
    print(name)
    
    return name




def print_link(link):
    print("scraper running")
    return print(link)