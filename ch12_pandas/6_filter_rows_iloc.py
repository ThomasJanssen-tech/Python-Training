import pandas as pd

df = pd.read_csv('ch12_pandas/titanic.csv')

print(df.iloc[0:5])  # Display the first 5 rows

print(df.iloc[0,0])  # Display line 0, column 0
