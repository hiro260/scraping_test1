import requests
from bs4 import BeautifulSoup

url = "https://www.ymori.com/books/python2nen/test1.html"
url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(url)
html.encoding = html.apparent_encoding 
# print(html.text)
# print(html.url)
# quit()

soup = BeautifulSoup(html.content, "html.parser")

#print(soup.find("title").text)
#print(soup.find("h2").text)
#print(soup.find("li").text)

#print(soup.find_all("li"))
#print(type(soup.find_all("li")))
#print(type(soup))

# quit()
chap2 = soup.find(id="chap2")
# print(chap2)
# print(type(chap2))
for element in chap2.find_all("li"):
    print(element.text)

print(type(chap2))
print(type(chap2.find_all("li")))

'''
for element in soup.find_all("li"):
    print(element.text)
    #print(type(element))

print(type([1, 2, 3]))
'''

'''
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


'''
filename = "download.txt"
with open(filename, "w", encoding="utf-8") as f:
    f.write(response.text)
'''
