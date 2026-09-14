import pandas as pd;
data = {
    "id":[11,22,33,44,55],
    "Name":['parth','patel','meet','raj','Hemal'],
    "age":[20,24,25,26,27]
}
df = pd.DataFrame(data);
print(df);
df['salary'] = [25000,55000,66000,55000,88000];
print(df);
df.insert(1,'uid',[2,3,4,5,6,]);
print(df) 
df.loc[1,'Name'] = 'yug';
print(df)
# df.loc[0,1,2,3,4,'Name'] = ['ansh','harsh','dhruv','jayveen','zenit'];
print(df)
df.loc[0,'Name'] = ['ansh'];
print(df);
df.drop(columns=['id'],inplace=True);
print(df)
df.drop(columns=['uid'],inplace=True);
print(df)
df.infi