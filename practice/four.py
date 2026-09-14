import pandas as pd;
data = {
    "Name":['parth','Harsh','Shyam','Shivam','Angat'],
    "Age":[55,66,77,88,99],
    "City":['rajkot','Ahemdabad','surat','mumbai','pune'],
}
df = pd.DataFrame(data);
df['U_id'] = [1,2,3,4,5];
print(df);
df.insert(3,'salary',[500000,600000,600000,5000000,6000000]);
print(df)
df.loc[0,'Name'] = 'khantushyam';
print(df)
df.loc[2,'Age'] = 25;
print(df)
df.loc[3,'Age'] = 28;
print(df)
df.loc[4,'Age'] = 25;
print(df)
df.loc[1,'Age'] = 22;
print(df)