import pandas as pd;
data = {
    "Id":[1,2,3,4,5],
    "Name":['parth','arshil','dharmik','hemal','shyam'],
    "Marks":[99,88,77,99,99]
}
df = pd.DataFrame(data);
df.insert(3,'Rollno',[55,11,22,44,55]);
df['salary'] = [55000,44000,66000,77000,33000];
df.loc[0,'Name'] = ['patel'];
df.drop(columns=['salary'],inplace=True);
print(df)