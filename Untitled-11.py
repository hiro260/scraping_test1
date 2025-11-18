import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import folium

df1 = pd.read_csv("898.csv", encoding="utf-8-sig")
df2 = pd.read_csv("200.csv", encoding="shift-jis")

print(df1.head(5))
print(df2.head(5))

print(df1.columns.values)
print(df2.columns.values)

print(len(df1))
print(len(df2))

hydrant = df2[["緯度", "経度"]].values
# print(hydrant)
# print(type(hydrant))
# print(hydrant.shape)

m = folium.Map(location=[35.942957, 136.198863], zoom_start=16)
'''
for data in hydrant:
    folium.Marker(data).add_to(m)

m.save("hydrant.html")
'''

store = df1[["緯度", "経度", "店舗名(日本語)"]].values
print(len(store))
#print(store)

for data in store:
    folium.Marker([data[0], data[1]], tooltip=data[2]).add_to(m)

m.save("store.html")

#for data in store:
#    folium.Marker(data).add_to(m)


#folium.Marker([35.942957, 136.198863]).add_to(m)








# quit()
# with open("200.csv", "rb") as f:
#    print(f.read(3))