import json
from pprint import pprint

dict1 = {"name" : "kyoto",
         "coord" : {"lat" : 35.02, "lon" : 135.75}
         }

print(dict1)
print(type(dict1))

print(dict1["name"])
print(dict1["coord"]["lat"])

list1 = [{'name': 'Tokyo', 'coord': {'lat': 35.69, 'lon': 139.69}}, {'name': 'Kyoto', 'coord': {'lat': 35.02, 'lon': 135.75}}]
print(type(list1))

list2 = ['apple', 'orange', 'banana', 'potate']
pprint(list2)