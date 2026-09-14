import pandas as pd;
data = {
    "Name":['ram','shyam','krishan'],
    "Age":[10,20,30],
    "City":['Rajkot','Suruat','Ahemdabad']
}
df = pd.DataFrame(data);
df.to_json("output.json");