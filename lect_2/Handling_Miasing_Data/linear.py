import pandas as pd;
data = {
    "Time":[1,2,3,4,5],
    "Values":[10,None,30,None,50]
}
df = pd.DataFrame(data);
print(df)
df['Values'] = df['Values'].interpolate(methos = "linear");
print("After interpolution")
df['']