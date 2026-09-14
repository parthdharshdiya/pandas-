import pandas as pd
df = pd.read_csv("sales_data.csv");
print("Display 10 rows first");
print(df.head(10));
print("Diaplay 10 rows last")
print(df.tail(10));