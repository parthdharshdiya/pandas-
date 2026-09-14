import pandas as pd;
data = {
    "id":[11,22,33,None,55],
    'Name':['parth',None,'meet','rahul','abhay'],
    "Age":[44,55,None,21,20]
}
df= pd.DataFrame(data);
print(df)
df.isnull();
print(df)
df['id'] = df['id'].interpolate(method='linear');
df['Age'] = df['Age'].interpolate(method='linear');
print(df)