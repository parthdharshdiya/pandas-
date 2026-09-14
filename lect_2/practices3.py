import pandas as pd;
data = {
    'id':[1,2,3,4,5],
    'Name':['parth','meet','jeet','dharmik','patel'],
    'salary':[55000,66000,77000,88000,99000]
}
df = pd.DataFrame(data);
print(df)
df.loc[4,'salary'] = 88000;
df.loc[5,'salary'] = 66000;
df.loc[3,'salary'] = 109000;
print(df)
df.drop(columns=['Name'],inplace=True);
print(df)