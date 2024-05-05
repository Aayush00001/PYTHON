import pandas as pd
df = pd.read_excel("weekdata.xlsx")
print(df.shape)
ndf=df.dropna(axis=0)
print(ndf.shape)
