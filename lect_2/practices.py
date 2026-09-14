import pandas as pd;
data = {
    "Id":[1,2,3,4,5],
    "Name":['parth','ziyan','suneyo','ayush','meet'],
    "Salary":[35000,25000,75000,89000,60000],
}
df = pd.DataFrame(data);
print(df);
df['bouns'] = df['Salary']+5*500;
print(df)
df.insert(4,'bounus',[22,44,55,66,77]);
print(df);
df.loc[1,'Id'] = 2;
print(df)
df.loc[3,'Name'] = 'parth';
print(df)
df.loc[4,'Name'] = 'meet';
print(df)
df.drop(columns=['Salary'],inplace=True);