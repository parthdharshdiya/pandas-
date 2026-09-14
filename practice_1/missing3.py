import pandas as pd;

data_3  = {
        "id":[1,2,None,4,5],
        "Name":['parth',None,'meet','jeel','smith'],
        "Age":[55,None,77,99,None]
}
df = pd.DataFrame(data_3);
print(df);
df.isnull();
print(df)
df['Age'] = df['Age'].interpolate(method='linear');
print(df)
df['id'] = df['id'].interpolate(method="linear");
print(df)