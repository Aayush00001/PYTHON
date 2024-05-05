import pandas as pd
df=pd.read_csv("data.csv")
print(df.loc[1,"name"])
print(df.loc[0:4,"name"])
