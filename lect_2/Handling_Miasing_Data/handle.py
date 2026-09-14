import pandas as pd;
data = {
    "Name":['ram',None,'krishna','parth','aditi','jagdish','raj'],
    "Age":[55,None,20,22,34,26,22],
    "Salary":[250000,None,5000,60000,34000,50000,26000],
    "Performce_scorer":[88,None,55,33,66,55,66]
}
df = pd.DataFrame(data);
print(df);
df.fillna(0,inplace=True);
print(df)