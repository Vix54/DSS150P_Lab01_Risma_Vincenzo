import os
from pathlib import Path
import pandas as pd


RAW = Path("data/raw")


customers = pd.read_csv(RAW / "customers.csv")
orders = pd.read_json(RAW / "orders.json")
products = pd.read_parquet(RAW / "products.parquet")

datasets = {
    "customers.csv": customers,
    "orders.json": orders,
    "products.parquet": products
}

for name, df in datasets.items():
    print(f"\n{'='*60}")
    print(f"PROFILING: {name}")
    print(f"{'='*60}")
    

    file_path = RAW / name
    size_bytes = file_path.stat().st_size
    print(f"File Size: {size_bytes} bytes ({size_bytes / 1024:.2f} KB)")
    

    print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    

    print(f"Columns: {list(df.columns)}")

    print("\n--- Data Types ---")
    print(df.dtypes)
    
    print("\n--- Null Values ---")
    print(df.isna().sum())
    

    print(f"\nFully Duplicated Rows: {df.astype(str).duplicated().sum()}")
    
   
    print("\n--- Distinct Values ---")
    print(df.astype(str).nunique())
    

    print("\n--- First 5 Records ---")
    print(df.head())
    

    numeric_cols = df.select_dtypes(include='number')
    if not numeric_cols.empty:
        print("\n--- Numeric Columns (Min/Max) ---")
        print(numeric_cols.agg(['min', 'max']).T)
    else:
        print("\n--- Numeric Columns --- \nNone found.")
        

    print("\n--- Date/Time Columns (Earliest/Latest) ---")

    date_cols = df.select_dtypes(include=['datetime', 'datetimetz']).columns.tolist()
    for col in df.columns:
        if ('date' in col.lower() or 'time' in col.lower()) and col not in date_cols:
            try:

                df[col] = pd.to_datetime(df[col])
                date_cols.append(col)
            except Exception:
                pass
                
    if date_cols:
        for col in date_cols:
            print(f"{col}:")
            print(f"  Earliest: {df[col].min()}")
            print(f"  Latest:   {df[col].max()}")
    else:
        print("No date/time columns identified.")
        
    print(f"{'='*60}\n")