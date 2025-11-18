import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df1 = pd.read_csv("Preview_20251117151523.csv", skiprows=1, index_col="時点")
df2 = pd.read_csv("Preview_20251117151534.csv", skiprows=1, index_col="時点")
df3 = pd.read_csv("Preview_20251117151548.csv", skiprows=1, index_col="時点")
df1.columns.values[0] = "平均"
df2.columns.values[0] = "最高"
df3.columns.values[0] = "最低"
print(df1.head(5))
print(df1.columns.values)
print(df1.index.values)
print(df1.dtypes)
# print(df2)
# print(df3)
print(df2.head(5))
print(df3.head(5))

# quit()

df1["平均"].plot()
df2["最高"].plot()
df3["最低"].plot()
plt.ylim(-10, 40)
plt.legend(loc="lower right")
plt.show()