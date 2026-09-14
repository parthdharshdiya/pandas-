import pandas as pd;
data = {
    'Name':['Arun','Parth','Patel','Tarun','Meet'],
    'Age':[22,21,25,28,24],
    'Salary':[55000,200000,50000,70000,80000]
}
df = pd.DataFrame(data);
print(df);
df.drop(columns=['Salary'],inplace=True);
print(df)