import pandas as pd
df=pd.read_csv("data.csv")
print(df.city[2])
print(df.city[2:5])
print(df.city[3::2])
print(df["city"][2])
print(df["city"][2:5])
