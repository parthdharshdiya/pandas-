import pandas as pd;
data = {
    'id':[1,2,3,4,5],
    'Name':['parth',None,'meet','mehul','viraj'],
    'Age':[55,44,55,None,22]
}
df = pd.DataFrame(data);
df['Age'] = df['Age'].interpolate(method='linear');
print(df)
# df['Name'] = df['Name'].interpolate(methods='linear');
# print(df)
df['id'] = df['id'].interpolate(method='linear');
print(df)
df.fillna(3,inplace=True);
print(df)