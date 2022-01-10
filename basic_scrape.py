import requests
from bs4 import BeautifulSoup

url = "https://princetonscientific.com/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

head = soup.head
title = soup.title.text
body = soup.body.text
all_content = []


for element in soup.select('.siteorigin-widget-tinymce'):
    all_content.append(element.text)

print(title)
for item in all_content:
    print(item.strip())