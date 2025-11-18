import pandas as pd
import chardet

'''
with open("13TOKYO.CSV", "rb") as f:
    result = chardet.detect(f.read())
    print(result)
'''

# quit()
df = pd.read_csv("13TOKYO.CSV", header=None, encoding="shift_jis")
# print(len(df))
# print(df.columns.values)

results = df[df[2] == 1600006]
print(results[[2, 6, 7, 8]])

results2 = df[df[8] == "四谷"]
print(results2[[2, 6, 7, 8]])

results3 = df[df[8].str.contains("四谷")]
print(results3[[2, 6, 7, 8]])