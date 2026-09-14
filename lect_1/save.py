import pandas as pd;
data = {
    'Name':['Ram','Shyam','Ghanshyam'],
    'Age':[10,20,30],
    'city':['nagpur','rajkot','jaypur']
}
df = pd.DataFrame(data)
print(df);
df.to_excel('parth.xlsx')