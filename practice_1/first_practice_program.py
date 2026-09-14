import pandas as pd;
data = {
    "id":[1,2,3,4,5],
    "Name":['parth','dharmik','shyam','shivam','krishna'],
    "Rollno":[11,22,33,44,55]
}
df = pd.DataFrame(data);
df['marks'] = [99,77,88,66,55];
print(df);
df.insert(2,'age',[22,21,22,24,25]);
print(df)
df.loc[0,'id'] = [11];
print(df)
df.loc[2,'id'] = [22];
print(df)
df.loc[3,'Name'] = ['parth'];
print(df)
df.loc[4,'Name'] = ['hari'];
print(df)
df.loc[4,'Rollno'] = [555];
print(df)
df.loc[4,'Rollno'] =[666];
print(df)
df.loc[3,'marks'] = [77];
print(df)
df.loc[4,'Name'] = ['krushna'];
print(df);
df.drop(columns=['Rollno'],inplace=True);
df.drop(columns=['marks'],inplace=True);
# df.drop(columns=['Age'],inplace=True);
df.drop(columns=['age'],inplace=True);
print(df);
df.drop(columns=['id'],inplace=True);
print(df)