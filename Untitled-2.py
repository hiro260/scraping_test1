import requests
from bs4 import BeautifulSoup

url = "https://www.ymori.com/books/python2nen/test1.html"
html = requests.get(url)
html.encoding = html.apparent_encoding 
# print(response.text)
# print(response.url)

print(html.text)
print("###################")
print("###################")
print(html.content)

print("###################")
print("###################")

x = b'hello'
print(x)
print(type(x))

y = 'name'
print(y)
print(type(y))

'''
soup = BeautifulSoup(html.content, "html.parser")

print(soup.find("title").text)
print(soup.find("h2").text)
print(soup.find("li").text)
'''



'''
filename = "download.txt"
with open(filename, "w", encoding="utf-8") as f:
    f.write(response.text)
'''
