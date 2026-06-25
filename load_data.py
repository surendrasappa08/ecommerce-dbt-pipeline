import psycopg2
import random
from datetime import datetime, timedelta

conn = psycopg2.connect(
    host="localhost", port=5432,
    dbname="ecommerce_db", user="dbt_user", password="dbt_pass"
)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS raw_orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT,
    product_name VARCHAR(100),
    category VARCHAR(50),
    quantity INT,
    unit_price NUMERIC(10,2),
    order_date DATE,
    status VARCHAR(20)
);
""")

categories = {'Electronics': ['Laptop','Phone','Tablet'], 'Clothing': ['Shirt','Pants','Jacket'], 'Food': ['Coffee','Tea','Snacks']}
statuses = ['completed','completed','completed','returned','pending']

for i in range(500):
    cat = random.choice(list(categories.keys()))
    product = random.choice(categories[cat])
    date = datetime(2024,1,1) + timedelta(days=random.randint(0,364))
    cur.execute("INSERT INTO raw_orders (customer_id, product_name, category, quantity, unit_price, order_date, status) VALUES (%s,%s,%s,%s,%s,%s,%s)",
        (random.randint(1,100), product, cat, random.randint(1,5), round(random.uniform(10,500),2), date, random.choice(statuses)))

conn.commit()
cur.close()
conn.close()
print("500 rows loaded successfully!")
