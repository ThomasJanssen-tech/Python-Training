import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

df = pd.DataFrame(mydataset)

df.to_csv('ch12_pandas\cars.csv',index=False)
df.to_excel('ch12_pandas\cars.xlsx',index=False)