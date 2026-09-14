import pandas as pd;
data = {
    "Time":[1,2,3,4,5],
    "Values":[10,None,1,None,5],
}
df = pd.DataFrame(data);
print(df);
df['Values'] = df['Values'].interpolate(methos="linear");
print(df)
data_1 = {
    "Name":['parth','patel','meet','jay','jenish'],
    "Rollno":[1,None,3,None,4],
    "marks":[99,77,66,55,44]
}
df = pd.DataFrame(data_1);
print(df);
df['Rollno'] = df['Rollno'].interpolate(method = 'linear');
print(df)
data_2 = {
    "Name":['parth','patel','angat','parvez','osho'],
    "Rollno":[55,44,66,None,33],
    "Marks":[99,99,88,99,88]
}
df = pd.DataFrame(data_2);
print(df);
df['Rollno'] = df['Rollno'].interpolate(method= "linear");
print(df);
data_3 = {
    "Id":[11,22,33,44,55],
    "Name":['parth','patel','meet','raj','yug'],
    "Age":[22,None,25,33,44]
}
df = pd.DataFrame(data_3);
df["Age"] = df["Age"].interpolate(method="linear");
print(df)