import pandas as pd;
data = {
    "Name":['ram','shyam','krishna','parth','aditi','jagdish','raj'],
    "Age":[55,30,20,22,34,26,22],
    "Salary":[250000,125000,5000,60000,34000,50000,26000],
    "Performce_scorer":[88,99,55,33,66,55,66]
}
df = pd.DataFrame(data);
print(df);
print('Modify data');
df.drop(columns=['Performce_scorer',"Salary"],inplace=True);
print(df)