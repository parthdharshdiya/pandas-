import pandas as pd;
data = {
     "Name":['ram','shyam','krishna','parth','aditi','jagdish','raj'],
    "Age":[55,30,20,22,34,26,22],
    "Salary":[250000,125000,5000,60000,34000,50000,26000],
    "Performce_scorer":[88,99,55,33,66,55,66]
}
# How to Update a values any precize location
df = pd.DataFrame(data);
#loc[]
#df.loc[row_index,"column number"] = new_value
df.loc[0,'Salary'] = 45000
print(df)