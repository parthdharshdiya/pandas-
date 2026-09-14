import pandas as pd;
data_5 = {
    "Name":['parth','meet','rahul','dharmik','shyam'],
    "age":[88,99,55,77,88],
}
df = pd.DataFrame(data_5);
df['rollno'] = [22,33,11,66,33];
df.insert(2,'u_id',[1,3,5,6,7])
print(df)