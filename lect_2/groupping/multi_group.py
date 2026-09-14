import pandas as pd;
data = {
    "Name":['Arun','Varun','Karun','Narun','Turun'],
    "Age":[28,28,45,23,28],
    "Salary":[50000,6000,70000,80000,40000]
}
df  = pd.DataFrame(data);
groupped = df.groupby(["Age","Name"])["Salary"].sum();
print(groupped);