import pandas as pd
df=pd.read_excel("mydata.xlsx")
print(df.sort_index())
print(df.sort_values(by="city"))
print(df.rank())
