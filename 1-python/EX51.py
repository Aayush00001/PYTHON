import pandas as pd
Student_data={"id":[1,2,3,4,5],
             "name":["aayush","aayush","aayush","aayush","aayush"],
             "marks":[10,10,10,10,10]}
df=pd.DataFrame(Student_data,columns=["id","name","marks"])
print(df)
