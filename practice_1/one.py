import pandas as pd;
data = {
    "Id":[1,2,3,4,5],
    "Name":['parth','meet','hemal','jasmin','ashish'],
    "Age":[22,21,23,24,25]
}
df = pd.DataFrame(data);
df.insert(0,'salary',[35000,45000,50000,60000,34000])
df['u_id'] = [11,22,33,44,55];
print(df)
df.loc[0,'salary'] = [50000];
print(df)
df.loc[0,'Id'] = [60000];
df.loc[4,'Id'] = [50000];
print(df)
df.loc[5,'Name'] = ['parth'];
print(df)
df.loc[4,'Age'] = [22];
print(df)