import pandas as pd
df=pd.read_csv("data.csv")
#print(df.loc[1:4,["id","name"]])
print(df.iloc[1:4,0:3])
