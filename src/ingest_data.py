import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

RAW = Path("data/raw")
DB_URI = "postgresql+psycopg2://dss150p:dss150p_lab@localhost:5432/dss150p_lab"

def process_customers():
    df = pd.read_csv(RAW / "customers.csv")
    df['signup_date'] = pd.to_datetime(df['signup_date'])
    return df.drop_duplicates(subset=['customer_id'])

def process_products():
    return pd.read_parquet(RAW / "products.parquet")

def process_orders():
    df = pd.read_json(RAW / "orders.json")
    shipping_df = pd.json_normalize(df['shipping'])
    shipping_df = shipping_df.rename(columns={'region': 'shipping_region', 'method': 'shipping_method'})
    df = df.drop(columns=['shipping']).join(shipping_df)
    df['order_timestamp'] = pd.to_datetime(df['order_timestamp'])
    return df

def load_to_db():
    engine = create_engine(DB_URI)
    
    customers_df = process_customers()
    products_df = process_products()
    orders_df = process_orders()
    
    valid_customers = customers_df['customer_id'].tolist()
    orders_df = orders_df[orders_df['customer_id'].isin(valid_customers)]
    
    with engine.begin() as conn:
        conn.exec_driver_sql("TRUNCATE TABLE orders, products, customers CASCADE;")
        
        customers_df.to_sql('customers', conn, if_exists='append', index=False)
        products_df.to_sql('products', conn, if_exists='append', index=False)
        orders_df.to_sql('orders', conn, if_exists='append', index=False)

if __name__ == "__main__":
    load_to_db()
    print("Data successfully loaded into PostgreSQL!")