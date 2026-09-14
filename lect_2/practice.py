import pandas as pd;
data = {
    'id':[1,2,3,4,5],
    'Name':['parth','Het','Hemal','Shyam','Arshil'],
    'Salary':[35000,25000,67000,45000,60000],
}
df = pd.DataFrame(data);
print(df);
df['bounos'] = 20*5;
print(df)
df.insert(4,'hike',[10,100,35,56,40]);
print(df)