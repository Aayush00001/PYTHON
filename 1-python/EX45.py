import pandas as pd
df=pd.read_excel("mydata.xlsx")
print(df.info())
print("*"*30)
print(df.count())
print("*"*30)
print(df.describe())
