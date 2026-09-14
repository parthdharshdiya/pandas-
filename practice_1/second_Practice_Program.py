import pandas as pd;
data = {
    "id":[1,2,3,4,5],
    "Name":['parth','dharmik','chintu','tommy','meet'],
    "Age":[55,33,22,44,55]
}
df = pd.DataFrame(data);
df['Rollno'] = [22,21,24,25,26];
print(df);
df['Salary'] = [55000,56000,67000,99000,43000];
print(df);
df.insert(0,'u_id',[11,22,33,55,66]);
print(df)
df.loc[0,'Rollno'] = [33];
print(df);
df.loc[1,'u_id'] = [101];
print(df)
df.loc[2,'id'] = [22];
print(df)
df.loc[3,'Salary'] = [99000];
print(df)
df.loc[4,'Name'] = ['parth patel'];
print(df)
df.loc[4,'Age'] = [33];
print(df)
df.drop(columns=['Age'],inplace=True);
print(df);
df.drop(columns=['Salary'],inplace=True);
print(df)
df.drop(columns=['u_id'],inplace=True);
print(df);
df.drop(columns=['id'],inplace=True);
print(df);
df.drop(columns=['Name'],inplace=True);
print(df)
df.drop(columns=['Rollno'],inplace=True);
print(df)