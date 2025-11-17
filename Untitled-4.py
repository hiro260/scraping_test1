import requests
from bs4 import BeautifulSoup
from pathlib import Path
import urllib
import time

time.sleep(1)
out_folder = Path("download")
out_folder.mkdir(exist_ok=True)

# url = "https://www.ymori.com/books/python2nen/sample1.png"
url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")

for element in soup.find_all("img"):
    src = element.get("src")
    # print(src)
    image_url = urllib.parse.urljoin(url, src)
    # print(image_url)
    filename = image_url.split("/")[-1]
    print(image_url, ">>", filename )
    
    out_path = out_folder.joinpath(filename)
    image_data = requests.get(image_url)

    with open(out_path, mode="wb") as f:
        f.write(image_data.content)




'''
filename = url.split("/")[-1]
out_path = out_folder.joinpath(filename)
print(filename)
with open(out_path, mode="wb") as f:
    f.write(image_data.content)
'''


#html = requests.get(url)


#html = requests.get(url)
#print(html.text)