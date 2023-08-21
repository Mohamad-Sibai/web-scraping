import json
import re
import unicodedata
from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
from flask import Flask, jsonify


client = MongoClient('mongodb://localhost:27017/')
db = client['db_news']
collection = db['articles']

url = 'https://www.aljazeera.com/middle-east/'

response = requests.get(url)
html_text = response.content

soup = BeautifulSoup(html_text, 'lxml')
data = []

for title_element in soup.find_all('a', class_='u-clickable-card__link'):
    span_element = title_element.find('span')
    if span_element:
        title = span_element.text.strip()
        cleaned_title = re.sub(r'[^\x00-\x7F]', '', title)
        cleaned_title = unicodedata.normalize("NFKD", cleaned_title)

        div_element = title_element.find_next('div', class_='gc__excerpt')
        if div_element:
            paragraph = div_element.get_text(strip=True)

        date_div = title_element.find_next('div', class_='date-simple')
        if date_div:
            date_span = date_div.find('span', class_='screen-reader-text')
            if date_span:
                date = date_span.get_text(strip=True)
            else:
                date = 'Date not found'

        data.append({'title': cleaned_title, 'paragraph': paragraph, 'date': date})

save_file = open("savedata.json", "w")
json.dump(data, save_file, indent=4, sort_keys=True)
save_file.close()

##collection.insert_many(data)

for item in data:
    print("Title:", item['title'])
    print("Paragraph:", item['paragraph'])
    print("Date:", item['date'])
    print()

