# generate_fake_sales.py

import pandas as pd
import random
from faker import Faker
import os

# Initialize Faker
fake = Faker()

# Define constants
PLATFORMS = ['PC', 'PlayStation', 'Xbox', 'Switch']
REGIONS = ['North America', 'Europe', 'Asia', 'South America', 'Australia']

# Generate fake sales data
def generate_sales_data(num_records=5000):
    data = []
    for _ in range(num_records):
        order = {
            'order_id': fake.uuid4(),
            'order_date': fake.date_between(start_date='-2y', end_date='today'),
            'customer_id': fake.uuid4(),
            'product_name': fake.word().capitalize() + ' Expansion Pack',
            'platform': random.choice(PLATFORMS),
            'purchase_amount': round(random.uniform(5.0, 99.99), 2),
            'region': random.choice(REGIONS)
        }
        data.append(order)
    
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df_sales = generate_sales_data()
    df_sales.to_csv('raw/fake_sales_data.csv', index=False)
    print("Fake sales data generated and saved to 'fake_sales_data.csv'")
