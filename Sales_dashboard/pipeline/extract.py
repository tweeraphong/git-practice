import pandas as pd

def extract():
    df = pd.read_csv("data/raw_sales.csv")
    print(f"Extracted {len(df)} rows")
    return df