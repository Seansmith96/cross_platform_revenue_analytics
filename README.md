Game Industry Sales Dashboard (Data Pipeline + Visualization)

Overview:
This project simulates a full-stack data analytics workflow for a fictional video game company. It includes synthetic data generation, ETL processing, database management, CSV report generation, and the creation of an interactive dashboard using Tableau Public.

Tools Used:
- Python (pandas, sqlite3, faker)
- SQLite
- Tableau Public
- CSV for report generation

Project Workflow:

1. Data Generation:
   A Python script (generate_fake_sales.py) creates 5,000 rows of synthetic sales data, including customers, platforms, purchase dates, amounts, and geographic regions.
   Output: fake_sales_data.csv

2. ETL Process:
   The load_and_clean_data.py script loads the raw CSV into a cleaned SQLite database (sales_data.db), performing data transformation and validation.

3. Data Export:
   A Python script (full_salesdb_export.py) pulls all records from the sales_data.db and exports them to full_sales_export.csv.
   A separate script (run_analytics.py) generates multiple summarized CSV reports:
   - Total Revenue
   - Revenue by Product
   - Revenue by Platform
   - Revenue by Region
   - Monthly Sales
   - Top Customers

4. Tableau Dashboard:
   Connected to full_sales_export.csv and created an interactive dashboard including:
   - Revenue trends over time
   - Pie chart by region
   - Revenue by platform
   - KPIs for Total Revenue
   - Mobile-responsive layout

Live Dashboard:
https://public.tableau.com/views/cross_platform_revenue_analytics_dashboard/Revenue?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

Business Relevance:
This project mirrors a real-world data analytics pipeline from raw ingestion to executive dashboarding. The CSV reports are lightweight and suitable for email distribution or automated transfer to FTP environments.

