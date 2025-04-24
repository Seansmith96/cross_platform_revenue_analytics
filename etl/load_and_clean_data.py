# load_and_clean_data.py

import pandas as pd
import sqlite3
from pathlib import Path

# Get the project root (one level up from etl/)
project_root = Path(__file__).resolve().parent.parent

# Load the data from the CSV file
df_sales = pd.read_csv(project_root/'data/raw/fake_sales_data.csv')

# clean the data
# Check for missing values and handle them
print("Checking for missing values...")
print(df_sales.isnull().sum())  # Will print out missing value count per column

# drop rows with missing data
df_sales = df_sales.dropna()

# ensure data types are correct
df_sales['purchase_amount'] = df_sales['purchase_amount'].astype(float)  # Ensure it's a float

# check if any duplicates exist
print("\nChecking for duplicates...")
print(f"Duplicate records: {df_sales.duplicated().sum()}")
df_sales = df_sales.drop_duplicates()

# load the cleaned data into SQLite
conn = sqlite3.connect(project_root/'warehouse/sales_data.db')
df_sales.to_sql('sales', conn, if_exists='replace', index=False)  # replace ensures we overwrite existing table
print("\nData successfully loaded into SQLite database: 'sales_data.db'")

# Close the connection
conn.close()
