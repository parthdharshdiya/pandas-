import pandas as pd;
df = pd.read_csv('output_Chandigarh_builderfloor (1).csv');
print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df['status']);
df['status'] = df['status'].fillna(df['status'].median());
print(df.isnull().sum());
df['description'] = df['description'].fillna('it is not aviable');
print(df.isnull().sum());
print(df['facing']);
df['facing'] = df['facing'].fillna('not any area');
print(df.isnull().sum());
df.drop(columns=['locality_score'],inplace=True);
print(df.isnull().sum())
df.drop(columns=['project_score'],inplace=True);
print(df.isnull().sum());
df.drop(columns=['builder_experience'],inplace=True)
print(df.isnull().sum())
print(df['Intercom']);
df['Intercom'] = df['Intercom'].fillna(df['Intercom'].median());
print(df.isnull().sum());
print(df['Indoor Games']);
df['Indoor Games'] = df['Indoor Games'].fillna(df['Indoor Games'].median());
print(df.isnull().sum())
print(df['ATM'])
df['ATM'] = df['ATM'].fillna(df['ATM'].median());
print(df.isnull().sum())
df['Maintenance Staff'] = df['Maintenance Staff'].fillna(df['Maintenance Staff'].median());
print(df.isnull().sum())
df['Staff Quarter'] = df['Staff Quarter'].fillna(df['Staff Quarter'].median());
print(df.isnull().sum())
df['Multipurpose Room'] = df['Multipurpose Room'].fillna(df['Multipurpose Room'].median());
print(df.isnull().sum());
df['Car Parking'] = df['Car Parking'].fillna(df['Car Parking'].median());
print(df.isnull().sum())
df['Hospital'] = df['Hospital'].fillna(df['Hospital'].median());
print(df.isnull().sum())
df['School'] = df['School'].fillna(df['School'].median());
print(df.isnull().sum())
df['Shopping Mall'] = df['Shopping Mall'].fillna(df['Shopping Mall'].median());
print(df.isnull().sum())
df['Vaastu Compliant'] = df['Vaastu Compliant'].fillna(df['Vaastu Compliant'].median());
print(df.isnull().sum())
df['Cafeteria'] = df['Cafeteria'].fillna(df['Cafeteria'].median());
print(df.isnull().sum());
df['Rain Water Harvesting'] = df['Rain Water Harvesting'].fillna(df['Rain Water Harvesting'].sum());
print(df.isnull().sum())
df.drop(columns=['Golf Course'],inplace=True);
print(df.isnull().sum())
df.to_csv('Chandigarh_buildfloor.csv');
print(df)