import requests
import json
from pprint import pprint



lang = "ja"
API_key = "01079198a68bb0a1c78add811e265957"
units = "metric"
city = "Kobe, JP"
city = "San Jose, US"
zipcode = "160-0006,JP"
zipcode = "83706,US"

# url = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}"
#url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&lang={lang}&units={units}"
url = f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode}&appid={API_key}&lang={lang}&units={units}"
jsondata = requests.get(url).json()
pprint(jsondata)
print(f"都市名: {jsondata['name']}")
print(f"気温: {jsondata['main']['temp']}")
print(f"天気: {jsondata['weather'][0]['main']}")
print(f"天気詳細: {jsondata['weather'][0]['description']}")
      
'''
print("####################")
print("####################")
print(jsondata)
'''

'''
ans = "今日は{key1}です。明日は{key2}です。"
print(ans)
ans = ans.format(key1="晴れ", key2="曇り")
print(ans)
'''
'''
key1="晴れ"
key2="曇り"
ans = f"今日は{key1}です。明日は{key2}です。"
print(ans)
'''