# run_analytics.py

import sqlite3
import pandas as pd
from pathlib import Path

# Get the project root (one level up from dashboard/)
project_root = Path(__file__).resolve().parent.parent

# Connect to the database
conn = sqlite3.connect(project_root/'warehouse/sales_data.db')

# Create a dictionary to hold queries
queries = {
    'total_revenue': """
        SELECT SUM(purchase_amount) AS total_revenue
        FROM sales
    """,
    'revenue_by_product': """
        SELECT product_name, SUM(purchase_amount) AS total_revenue
        FROM sales
        GROUP BY product_name
        ORDER BY total_revenue DESC
    """,
    'top_customers': """
        SELECT customer_id, SUM(purchase_amount) AS total_spent
        FROM sales
        GROUP BY customer_id
        ORDER BY total_spent DESC
        LIMIT 5
    """,
    'monthly_sales': """
        SELECT strftime('%Y-%m', order_date) AS month, SUM(purchase_amount) AS monthly_revenue
        FROM sales
        GROUP BY month
        ORDER BY month
    """,
    'revenue_by_platform': """
        SELECT platform, SUM(purchase_amount) AS platform_revenue
        FROM sales
        GROUP BY platform
        ORDER BY platform_revenue DESC
    """,
    'revenue_by_region': """
        SELECT region, SUM(purchase_amount) AS region_revenue
        FROM sales
        GROUP BY region
        ORDER BY region_revenue DESC
    """
}

# Run queries and save results
for name, query in queries.items():
    df = pd.read_sql_query(query, conn)
    print(f"\n=== {name.replace('_', ' ').title()} ===")
    print(df)
    df.to_csv(project_root / 'dashboard' / 'reports' / f'{name}_report.csv', index=False) # Save to CSV

# Close the connection
conn.close()
print("\nAll analytics reports have been generated and saved!")
