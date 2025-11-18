import json
from pprint import pprint
import os

path1 = "python2nen_sample"
path2 = "chap5/test2.json"

path = os.path.join(path1, path2)
print(path)

#with open("python2nen_sample/chap5/test2.json", mode="r") as f:
with open(path, mode="r") as f:
    text1 = f.read()
print(text1)
pprint(json.loads(text1))
print("#####")
print("#####")
with open(path, mode="r") as f:
    jsondata = json.loads(f.read())
pprint(jsondata)

print(jsondata[0]["name"])