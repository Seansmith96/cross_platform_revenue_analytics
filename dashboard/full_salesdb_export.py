import pandas as pd
import sqlite3
from pathlib import Path

# Paths
project_root = Path(__file__).resolve().parent.parent
db_path = project_root / 'warehouse/sales_data.db'
csv_output = project_root / 'dashboard/reports/full_sales_export.csv'

# Connect and export
conn = sqlite3.connect(db_path)
df = pd.read_sql_query("SELECT * FROM sales", conn)
df.to_csv(csv_output, index=False)
conn.close()
