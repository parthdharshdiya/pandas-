import pandas as pd;
data = {
    "Name":["parth",'smith','shyam','shivam','henil'],
    "age":[20,23,22,22,22],
    "marks":[99,99,99,None,99]
}
df = pd.DataFrame(data);
print(df)
df.insert(3,'city',['rajkot','ahemdabad','surat','valsad','vapi']);
print(df)
df['pincode'] = [22,33,44,55,56];
print(df)
df.loc[0,'Name'] = ['ramiz'];
print(df)
df.loc[1,'age'] = [20];
print(df);
df.drop(columns=['salary'],inplace=True);
print(df)