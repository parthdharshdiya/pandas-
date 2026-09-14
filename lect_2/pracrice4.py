import pandas as pd;
data = {
    "Name":['parth','meet','rahul','sarukh','abhay'],
    "age":[22,24,23,34,40],
    "marks":[99,88,99,99,97]
}
df = pd.DataFrame(data);
print(df);
df['salary'] = ['100000','70000','80000','60000','50000'];
print(df)
df.insert(2,'u_id',[20,44,55,22,33]);
df.loc[2,'Name'] ="aman";
df.loc[4,'age'] = 45;
df.loc[3,'marks'] = 100;
df.loc[4,'marks'] = 89;
print(df)