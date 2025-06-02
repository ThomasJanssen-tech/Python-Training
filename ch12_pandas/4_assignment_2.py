import pandas as pd

df = pd.read_csv('ch12_pandas/titanic.csv')

print(df['Age'].max())
