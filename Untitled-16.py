import requests
import json
from pprint import pprint
from datetime import datetime, timedelta, timezone
import pandas as pd
import matplotlib.pyplot as plt

lang = "ja"
API_key = "01079198a68bb0a1c78add811e265957"
units = "metric"
city = "Kobe, JP"
#city = "San Jose, US"
#zipcode = "160-0006,JP"
#zipcode = "83706,US"

#url = f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode}&appid={API_key}&lang={lang}&units={units}"
#api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}

url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_key}&lang={lang}&units={units}"
tz = timezone(timedelta(hours=+9), 'JST')
jsondata = requests.get(url).json()

df = pd.DataFrame(columns=["気温"])

for dat in jsondata['list']:
    #print(dat['dt'])
    #print(dat['dt_txt'][:-3])
    jst = str(datetime.fromtimestamp(dat['dt'], tz))[:-9]
    #print(f"UTC: {dat['dt_txt'][:-3]}, JST: {jst}")
    weather = dat['weather'][0]['description']
    temp = dat['main']['temp']
    #print(f"JST: {jst}, weather: {weather}, temp: {temp}")
    df.loc[jst] = temp

print(df)
df.plot(figsize=(15,8))
plt.ylim(-10,40)
plt.grid()


plt.show()
#pprint(jsondata["list"])


quit()

pprint(jsondata)
print("##############")
print("##############")
pprint(jsondata["message"])
print("##############")
print("##############")
pprint(jsondata["city"])
print("##############")
print("##############")
print(len(jsondata))
print(jsondata.keys())
print("##############")
print("##############")
pprint(jsondata["cnt"])
print("##############")
print("##############")
pprint(jsondata["cod"])
print("##############")
print("##############")
pprint(jsondata["list"])