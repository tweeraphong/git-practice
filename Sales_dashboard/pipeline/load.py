import mysql.connector

def load(df):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="sales_db"
    )

    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO sales (
                order_id, order_date, product, region,
                quantity, price, revenue
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            int(row["order_id"]),
            row["order_date"].strftime('%Y-%m-%d'),
            row["product"],
            row["region"],
            int(row["quantity"]),
            int(row["price"]),
            float(row["revenue"])
        ))

    conn.commit()
    cursor.close()
    conn.close()

    print("Data loaded to MySQL")