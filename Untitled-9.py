import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv("FEH_00200524_251118062717.csv", index_col="全国・都道府県", encoding="shift_jis")
print(df)
print(len(df))
print(df.columns.values)

print(df["2024年"])
print(df.dtypes)
print(type(df["2024年"]))

df = df.drop("全国", axis=0)

df["2024年"] = pd.to_numeric(df["2024年"].str.replace(",", ""))
df["2020年"] = pd.to_numeric(df["2020年"].str.replace(",", ""))
print(df.dtypes)

df["人口増減"] = df["2024年"] - df["2020年"]
df = df.sort_values("人口増減", ascending=False)
df["人口増減"].plot.bar(figsize=(10, 6))
plt.ylim(-200, 14000)
#df = df.sort_values("2024年", ascending=False)
#df["2024年"].plot.bar(figsize=(10, 6))


plt.show()

