import pandas as pd

df = pd.read_excel('ch8_installing_importing_libraries/excel.xlsx',header=None)

print(df.to_string()) 