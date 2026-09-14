import pandas as pd;
data = {
    "Name":['parth','patel','viraat','khohli','Anushka'],
    "salary":[55000,6000,7000,80000,70000],
    "Age":[55,66,77,88,99],
}
df = pd.DataFrame(data);
print(df);
df['id'] = "parth";
df['id'] = "parth"*2;
df.insert(4,'bouns',[44,55,66,88,99]);
print(df)