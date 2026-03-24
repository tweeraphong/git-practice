import pandas as pd
import random
import os
from datetime import datetime, timedelta

# Create folder if not exists
os.makedirs("data", exist_ok=True)

rows = 5000

products = ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"]
regions = ["Bangkok", "Chonburi", "Chiang Mai", "Phuket", "Rayong"]

data = []

start_date = datetime(2023, 1, 1)

for i in range(rows):
    date = start_date + timedelta(days=random.randint(0, 365))
    product = random.choice(products)
    region = random.choice(regions)
    quantity = random.randint(1, 10)
    price = random.randint(100, 2000)

    data.append({
        "order_id": i + 1,
        "order_date": date.strftime("%Y-%m-%d"),
        "product": product,
        "region": region,
        "quantity": quantity,
        "price": price
    })

# Create DataFrame AFTER data is ready
df = pd.DataFrame(data)

# Save file
df.to_csv("data/raw_sales.csv", index=False)

print(f"Dataset generated: {len(df)} rows")