import pandas as pd
import numpy as np
df = pd.read_excel("weekdata.xlsx")

#1Print the column : answeringAgent names.
#print(df['AnsweringAgent'].to_string)

#2Print all the data of the odd index.

#3Display all the details of calls that are made on Monday.
#print(df[df["DayOfWeek"]=="mon"].to_string())

#4List all the contact numbers that is made for Complaints
#print(df[df["ReasonForCall"]=="Complaint"].to_string())

#5Display call details having call duration more than 10 minutes.
#print(df[df["CallDuration"]>=10].to_string())

#6How many calls are answered by agent ‘David’ ?
#print(df[df["AnsweringAgent"]=="David"].to_string())

#7Count the number of calls made after 9.30 AM.
#print(df[df["TimeOfDay"]>=9:30].to_string())

#8Add new Column in dataframe named “ CallingFrom”
#df["CallingFrom"]=np.NaN

#9Fill above the newly added column with value “IND”.
#df["CallingFrom"]="IND"

#10Drop All the rows containing at least 1 NULL value.
#ndf=df.dropna(axis=0,how="all")
#print(ndf.shape)

#11Drop all the columns containing all the NULL values.
#ndf=df.dropna(axis=1,how="all")
#print(ndf.shape)



