import pandas as pd

def transform(df):
    # Convert date
    df["order_date"] = pd.to_datetime(df["order_date"])

    # Create revenue column
    df["revenue"] = df["quantity"] * df["price"]

    # Clean data
    df = df.dropna()

    return df