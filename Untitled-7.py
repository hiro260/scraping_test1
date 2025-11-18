import pandas as pd
import openpyxl
'''
df = pd.read_csv("./python2nen_sample/chap3/test.csv")
print(df)

kokugo = df.sort_values("国語", ascending=False)

kokugo.to_excel("csv_to_excel.xlsx")
kokugo.to_excel("csv_to_excel2.xlsx", index=False, sheet_name="国語でソート")

with pd.ExcelWriter("csv_to_excel3.xlsx") as writer:
    df.to_excel(writer, index=False, sheet_name="元のデータ")
    kokugo.to_excel(writer, index=False, sheet_name="国語でソート")
'''
    
# quit()

df = pd.read_excel("csv_to_excel3.xlsx")
print(df)
df = pd.read_excel("csv_to_excel3.xlsx", sheet_name="国語でソート")
print(df)






# print(kokugo)