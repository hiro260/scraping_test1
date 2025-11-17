import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv("./python2nen_sample/chap3/test.csv", index_col=0)
print(df)
#print(df.columns)
#print(df.index)

#quit()
df["国語"].plot.bar()
plt.legend(loc="lower left")
plt.show()

df[["国語", "数学"]].plot.barh()
plt.legend(loc="lower left")
plt.show()

df.loc["C子"].plot.barh()
plt.legend(loc="lower left")
plt.show()

df.loc["C子"].plot.pie(labeldistance=0.6)
plt.legend(loc="lower left")
plt.show()


quit()
df.plot.bar(stacked=True)
plt.legend(loc="lower right")
plt.show()

df.plot.box()
plt.show()

df.plot.area()
plt.legend(loc="lower right")
plt.show()

'''
df.to_csv("csv_test1.csv", encoding="utf-8-sig")
df.to_csv("csv_test2.csv", index=False,  encoding="utf-8-sig")
df.to_csv("csv_test3.csv", index=False, header=False,  encoding="utf-8-sig")
'''

'''
print(df.T)
print(df.values)
print(type(df.values))
'''

'''
kokugo = df.sort_values("国語", ascending=False)
print(kokugo)
'''

'''
print(df["数学"].max())
print(df["数学"].min())
print(df["数学"].mean())
print(df["数学"].median())
print(df["数学"].sum())
'''

'''
data_s = df[df["国語"] >= 90]
print(data_s)

data_c = df[df["数学"] < 70]
print(data_c)
'''

"""
df = df.drop("名前", axis=1)
print(df)
df = df.drop(2, axis=0)
print(df)
"""

'''
df["美術"] = [68, 73, 82, 77, 94, 96]
print(df)

df.loc[6] = ["G恵", 90, 92, 94, 96, 92, 98]
print(df)
'''

'''
print(len(df))
print(df.columns.values)
print(df.index.values)
print("kokugo\n", df["国語"])
print("kokugo and sugaku\n", df[["国語", "数学"]])
print("c-ko\n", df.loc[2])
print("c-ko and d-ro\n", df.loc[[2, 3]])
print("c-ko kokugo\n", df.loc[2]["国語"])
print(type(df.loc[2]["国語"]))
print("c-ko\n", type(df.loc[2]))
'''