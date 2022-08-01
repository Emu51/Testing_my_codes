import pandas as pd
df =  pd.read_csv('pokemon_data.csv')
print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')])

