import pandas as pd

df = pd.read_csv('ch12_pandas/titanic.csv')

print(df.loc[df['Pclass'] == 1]['Age'].mean())

print(df.loc[df['Pclass'] == 3]['Age'].mean())

