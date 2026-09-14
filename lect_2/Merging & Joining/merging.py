import pandas as pd;
df_custemers = pd.DataFrame({
    "CunstomerId":[1,2,3],
    'Name':['Ramesh','Suresh','kalpesh']
})
df_orders = pd.DataFrame({
    'CustomerId':[1,2,4],
    'OrderdAmmount':[250,450,350]
})
#merged
df_merged = pd.merge(df_custemers,df_orders,on="CustomerId",how='innerjoin')
print('outer join')
print(df_merged)