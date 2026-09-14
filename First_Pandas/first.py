import pandas as pd;
df_cus1 = pd.DataFrame({
    "Cus_Id":[1,2,3],
    'Name':['parth','arshil','dharmik'],

})
df_cus2 = pd.DataFrame({
      "Cus_Id":[22,33,44],
      "Name":["parth","patel","Dharmesh"]
})
df_merged = pd.merge(df_cus1,df_cus2,on="Cus_ID",how="innerjoin");
print(df_merged)