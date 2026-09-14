import pandas as pd;
data = {
    "id":[1,2,3,4,5],
    "Name":['parth','patel','viraj','alakh','Hemal'],
    "Rollno":[11,22,33,44,55]
}
df = pd.DataFrame(data);
print(df)
df['age'] = [33,44,22,21,20];
print(df);
df.insert(0,'u_id',[22,22,44,55,11]);
print(df);
df.insert(5,'marks',[99,88,99,99,99]);
print(df)
df.loc[0,'Rollno'] = [11];
print(df)
df.loc[0,'u_id'] = [24];
print(df);
df.loc[0,'id'] = [11];
print(df)
df.loc[0,'Name'] = ['krish'];
print(df)
df.loc[0,'Rollno'] = [33];
print(df)
df.loc[0,'age'] = [44];
df.loc[0,'marks'] = [55];
print(df)
df.drop(columns='u_id',inplace=True);
print(df);
df.drop(columns='Name',inplace=True);
print(df)
df.drop(columns='marks',inplace=True);
print(df);
df.drop(columns='Rollno',inplace=True);
print(df);
df.drop(columns='id',inplace=True);
print(df)
df.drop(columns='age',inplace=True);
print(df)