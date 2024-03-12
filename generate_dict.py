
import requests
from bs4 import BeautifulSoup
import re
import json



def create_dict():
    questions_page_url = "https://corbettmaths.com/5-a-day/gcse/"
    page = requests.get(questions_page_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    links = soup.find_all('a')
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    difficulty_levels = {
        "Numeracy": ["Numeracy"],
        "Foundation": ["Foundation"],
        "Foundation Plus": ["Foundation Plus", "FP"],
        "Higher": ["Higher"],
        "Higher Plus": ["Higher Plus", "HP"]
    }
    page_dict = {}
    for link in links:
        url = link.get('href')
        if not url or not url.endswith('.pdf'):
            continue

        filename = url.split('/')[-1]
        identified_month = next((month for month in months if month.lower() in filename.lower()), None)
        identified_difficulty = next((level for level, keywords in difficulty_levels.items() for keyword in keywords if keyword.lower() in filename.lower()), None)
        numbers = re.findall(r'\d+', filename)
        identified_day = numbers[0] if numbers else None

        if identified_month and identified_difficulty:
            page_dict.setdefault(identified_month, {"Answers": {}, "Questions": {}})
            page_dict[identified_month]["Questions"].setdefault(identified_day, {})[identified_difficulty] = url

    answer_pages = {
        "Jan": "https://corbettmaths.com/5-a-day/gcse/january-answers/",
        "Feb": "https://corbettmaths.com/5-a-day/gcse/february-answers/",
        "Mar": "https://corbettmaths.com/5-a-day/gcse/march-answers/",
        "Apr": "https://corbettmaths.com/5-a-day/gcse/april-answers/",
        "May": "https://corbettmaths.com/5-a-day/gcse/may-answers/",
        "Jun": "https://corbettmaths.com/5-a-day/gcse/june-answers/",
        "Jul": "https://corbettmaths.com/5-a-day/gcse/july-answers/",
        "Aug": "https://corbettmaths.com/5-a-day/gcse/august-answers/",
        "Sep": "https://corbettmaths.com/5-a-day/gcse/september-answers/",
        "Oct": "https://corbettmaths.com/5-a-day/gcse/october-answers/",
        "Nov": "https://corbettmaths.com/5-a-day/gcse/november-answers/",
        "Dec": "https://corbettmaths.com/5-a-day/gcse/december-answers/" 
    }
    for month, url in answer_pages.items():
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            url = link.get('href')
            if not url or not url.endswith('.pdf'):
                continue

            filename = url.split('/')[-1]
            identified_difficulty = next((level for level, keywords in difficulty_levels.items() for keyword in keywords if keyword.lower() in filename.lower()), None)
            numbers = re.findall(r'\d+', filename)
            identified_day = numbers[0] if numbers else None

            if identified_difficulty:
                page_dict[month]["Answers"][identified_difficulty] = url

    with open("corbettmaths.json", "w") as f:
        json.dump(page_dict, f)
