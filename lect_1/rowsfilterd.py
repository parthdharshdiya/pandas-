import pandas as pd;
data = {
    "Name":["Ram","Parth","Patel","Arshil","Ram","Parth","Patel","Arshil"],
    "Age":[77,88,55,44,22,33,25,55,88],
    "Salary":[55000,66000,88000,55000,66000,88000,55000,66000,88000,55000,66000],
    "Performnce_Scprer":[44,99,77,56,44,99,77,56,44,99,77,56,]
}
df = pd.DataFrame(data)
high_salary = df[df['salary'] > 50000]
print('Employees with salary  > 50000');
print(high_salary)
filtered = df[{df['Age'] > 30} & df['salary'] > 50000];
print(f'Employee list Age > 30 + salary > 50000');
print(filtered)
#using or condtion
filteres_or = df[(df['AGe']> 35) | (df["Performnce_score"] > 50)];
print(filteres_or)