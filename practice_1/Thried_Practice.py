import pandas as pd;
data = {
    "Id":[11,22,33,44,55],
    "Name":['parth','hemal','arjun','angat','abheshek'],
    "Rollno":[11,44,55,66,10]
}
df = pd.DataFrame(data);
df['age'] = [33,44,11,10,22];
print(df);
df['marks'] = [99,99,98,99,99];
print(df)
df.insert(0,'u_id',[22,11,33,44,66]);
print(df);
df.loc[0,'u_id'] = [33];
print(df);
df.loc[1,'Id'] = [44];
print(df)
df.loc[2,'Name'] = ['patel'];
print(df);
df.loc[3,'Rollno'] = [55];
print(df)
df.loc[4,'age'] = [44];
print(df);
df.loc[4,'marks'] = [100];
print(df)
df.loc[3,'marks'] = [100];
print(df);
df.loc[4,'age'] = [40];
print(df)
df.drop(columns=['u_id'],inplace=True);
print(df)
df.drop(columns=['Id'],inplace=True);
print(df);
df.drop(columns=['Name'],inplace=True);
print(df);
df.drop(columns=['Rollno'],inplace=True);
print(df)
df.drop(columns=['age'],inplace=True);
print(df)
df.drop(columns=['marks'],inplace=True);
print(df)
df.drop(columns=['Index'],inplace=True);
print(df)