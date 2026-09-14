# data anylsis
import pandas as pd;
data = {
    'Name':['parth','chrish','meet','rahul','husen'],
    'age':[55,66,99,88,99],
    'salary':[55000,70000,65000,88000,99000]
}
df = pd.DataFrame(data);
df['Bounus_id'] = [101,102,103,104,105];
df.insert(0,'id',[1,2,3,4,5]);
print(df);
data = {
    "id":[1,2,3,4,5],
    "name":['parth','smit','rahul','dhaval','krishna'],
    "marks":[99,99,88,88,99]
}
df = pd.DataFrame(data);
print(df)
df['rollno'] = [11,33,55,44,22];
print(df);
df.insert(1,'u_id',[201,102,304,506,302]);
print(df)
data_1 = {
    "id":[101,102,103,104,150],
    "name":['parth','niraj','elvish','yogesh','angat'],
    "salary":[99000,88000,66000,77000,99000]
}
df = pd.DataFrame(data);
df['Bounus_id'] = [101,102,103,104,150];
print(df)
df.insert(1,'user_id',[22,55,66,77,88]);
print(df)
data_2 = {
     "B_id":['101','102','103','104','105'],
     "U_name":['parth','smit','mahesh','yogesh','gavan'],
     "Acc_type":['s','c','s','c','s'],
     "Acc_monery":['55000','60000','50000','80000','50000']
}
df = pd.DataFrame(data_2);
print(df);
data_3 = {
    "id":['1','2','3','4','5'],
    "name":['parth','meet','rahul','mahesh','chahan'],
    "salary":['50000','40000','70000','90000','55000']
}
df =pd.DataFrame(data_3);
print(df);
df['bounus'] = 500*2;
print(df)
data_4 = {
    "id":[101,102,103,104,105],
    "Name":['parth','mukesh','changan','magan','hemal'],
    "marks":[55000,65000,70000,88000,99]
}
df = pd.DataFrame(data_4);
df['rank'] = [1,5,66,7,9];
print(df)
df.insert(0,'u_id',[11,55,22,33,66]);
print(df);
df.loc[2,'marks'] = [99];
print(df)