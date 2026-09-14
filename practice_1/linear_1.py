import pandas as pd;
data = {
    "Id":[1,2,3,4,5],
    "Name":['parth','patel','meet','raj','akash'],
    "Rollno":[33,44,55,None,22]
}
df = pd.DataFrame(data);
df['Rollno'] = df['Rollno'].interpolate(method="linear");
print(df)
data_1 = {
    "Id":[1,2,3,4,5],
    "Name":['parth','patel','meet','raj','abhay'],
    "rollno":[22,14,55,66,None]
}
df = pd.DataFrame(data_1);
df['rollno'] = df['rollno'].interpolate(method="linear");
print(df)