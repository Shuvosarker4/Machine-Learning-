import pandas as pd

# read CSV file
df = pd.read_csv('data.csv')

# read excel file
df = pd.read_excel('data.xlsx')

# read json file
df = pd.read_json('data.json')

# read parquet file
df = pd.read_parquet('data.parquet')