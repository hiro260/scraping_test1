import requests
from bs4 import BeautifulSoup
import urllib

url = 'https://news.yahoo.co.jp/categories/it'

html = requests.get(url)
html.encoding = html.apparent_encoding

soup = BeautifulSoup(html.content, "html.parser")
topic = soup.find(class_="sc-1d6xg0e-3 eUEpFI")

# print(topic)
filename = "linklist.txt"

with open(filename, 'w', encoding='utf-8') as f:
    for element in topic.find_all("a"):
        f.write(element.text+"\n")
        individual_url = element.get("href")
        #print(individual_url)
        link_url = urllib.parse.urljoin(url, individual_url)
        f.write(link_url+"\n")

