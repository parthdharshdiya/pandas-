import pandas as pd;
data = {
    "id":[1,2,3,4,5],
    "Name":['parth','patel','meet','yug','raj'],
    "Age":[55,24,18,17,66]
}
df = pd.DataFrame(data);
df.isnull();
print(df)
df['id'] = df['id'].interpolate(method='linear');
print(df);
df['id'] = df['id'].interpolate(method='linear');
print(df)
df['id'] = df['id'].interpolate(method='linear');
print(df)
df['id'] = df['id']