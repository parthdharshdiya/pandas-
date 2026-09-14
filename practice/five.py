import pandas as pd;
data = {
    "Name":['parth','harsh','hemal','shyam','smith'],
    "Age":[25,23,24,25,26],
    "Salary":[25000,55000,65000,70000,60000]
}
df = pd.DataFrame(data);
print(df);
df.insert(0,'U_id',[1,2,3,4,5]);
print(df)
df['bounus'] = [2000,2000,2000,2000,2000];
print(df);
df.loc[0,'Salary'] = 200000;
print(df)
df.drop(columns=['Salary'],inplace=True);
print(df);
df.drop(columns=['U_id'],inplace=True);
print(df)