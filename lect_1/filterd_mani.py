import pandas as pd;
data = {
    "Name":["Ram","Parth","Patel","Arshil","Ram","Parth","Patel","Arshil"],
    "Age":[77,88,55,44,22,33,25,55,88],
    "Salary":[55000,66000,88000,55000,66000,88000,55000,66000,88000,55000,66000],
    "Performnce_Scprer":[44,99,77,56,44,99,77,56,44,99,77,56,]
}
df = pd.DataFrame(data)
print("Singal Data Feame");
print(df);
print("Names (Singal column return series)");
name = df['Name']
print(name)
subset = df[["name",["Age"]]]
print(subset)