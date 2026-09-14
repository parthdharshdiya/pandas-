import pandas as pd;
data = {
    "Name":['ram','shyam','ghanshyam','chaman','naman'],
    "Age":[55,22,44,20,13,55],
    "Salary":[55000,66000,12000,43200],
    "performnce_scorer":[86,55,33,66,99]
}
df = pd.DataFrame(data);
high_salary = df[df['salary'] > 50000]
print('Employess with salary > 50000');
print(high_salary);

filtered = df[(df['Age'] > 30) & (df['salary'] > 50000)];
print(f'Employee list age > 30 + salary > 50000');
print(filtered);