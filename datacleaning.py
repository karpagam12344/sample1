import pandas as pd
df = pd.read_csv('customers-100.csv')
new_df = df.dropna()
print(new_df.to_string())
df.fillna(456-895-9632,inplace = True)
df.fillna({"Phone 1":456-895-9632},inplace = True)
print(df.to_string())
    
