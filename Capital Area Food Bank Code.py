import pandas as pd

df = pd.read_excel('data_case2.xlsx')

df = df.iloc[:, :-22]  # Drops the last 'x' columns
pd.set_option('display.max_columns', None)

df.head()