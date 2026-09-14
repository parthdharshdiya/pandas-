
import pandas as pd;

data = {
    "Name":['ram','shyam','ghanshyam','parth','meet','arshil','parth'],
    "Age":[55,44,66,77,88,99,100],
    "Salary":[50000,60000,70000,48000,99000,78000,88000],
    "Performnce_score":[85,77,99,77,88,99,87]
}
df = pd.DataFrame(data);
print(df);
df["Bonus"] = df["Salary"] * 0.1;
print(df)
df.loc[0,'Salary'] = 105000
print(df)
#incressing values 5%;
df['Salary'] = df['Salary'] * 1.05;
print(df)
#drop columns
df.drop(columns=["Performnce_score"],inplace=True);
print(df)