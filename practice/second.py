import pandas as pd;
data = {
  "id":[1,2,3,4,5],
  "Name":['parth','patel','smit','dhaval','het'],
  "marks":[99,88,99,99,99]
}
df = pd.DataFrame(data);
df['rank'] = [1,11,5,33,2];
print(df);
data = {
    "id":[11,10,33,44,55],
    "Name":['parth','patel','smith','mohit','hardik'],
    "marks":[99,99,88,99,89]
}
df = pd.DataFrame(data);
df.insert(1,'u_id',[11,22,33,55,11]);
print(df)
data_5 = {
    "Name":['parth','meet','rahul','dharmik'],
    "age":[88,99,55,77,88],
}
df =  pd.DataFrame(data_5);
df['rollno'] = [33,44,55,1,2];
print(df);