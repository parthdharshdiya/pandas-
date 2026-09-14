import pandas as pd;
data = {
    "Name":['ram','shyam','krishna','parth','aditi','jagdish','raj'],
    "Age":[55,30,20,22,34,26,22],
    "Salary":[250000,125000,5000,60000,34000,50000,26000],
    "Performce_scorer":[88,99,55,33,66,55,66]
}
df = pd.DataFrame(data);
print(df);
df["Bouns"] = df['Salary'] * 0.20
print(df);
df.insert(0,"Employee_id",[10,20,30,40,50,60,70])
print(df)