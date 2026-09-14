import pandas as pd;
data = {
    "Name":['parth','Het',"Hemal"],
    "Age":[22,17,21],
    "Salary":[10000,20000,3000]
}
df = pd.DataFrame(data);
df.sort_values(by="Age",ascending=False,inplace=True);
print(df)
