import pandas as pd;
data = {
    "id":[2,3,4,5,5],
    "name":['parth','angat','jay','mayuer','mehul'],
    "age":[20,22,24,25,26]
}
df = pd.DataFrame(data);
print(df)
df['salary'] = [25000,55000,76000,55000,50000];
print(df)
df.insert(0,'bouns',[5500,4500,5000,6000,7000]);
print(df)
df.loc[0,'bouns'] = 70000;
print(df)
df.loc[1,'id'] = 4;
print(df)
df.drop()