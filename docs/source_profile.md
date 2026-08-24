# Source Profile Interpretations

## 1. customers.csv
* **Observation 1 (Duplicate Risk):** The profile reveals 2 fully duplicated rows. A deduplication step must be implemented in the ingestion pipeline before loading this data into a relational database to avoid primary key constraint violations.
* **Observation 2 (Nullability):** While the `customer_id` is fully populated, the `email` (3 missing) and `city` (2 missing) fields contain null values. The future table schema and data contract must explicitly allow nulls for these specific columns.

## 2. orders.json
* **Observation 1 (Nested JSON Structure):** The `shipping` column contains nested dictionary objects (e.g., `{'region': 'Region VII', 'method': 'Standard'}`). A pipeline transformation step will be required to flatten this data into separate `shipping_region` and `shipping_method` columns before it can be stored in a standard SQL table.
* **Observation 2 (Reliable Primary Key):** There are exactly 250 distinct `order_id` values for the 250 rows, and zero nulls across the entire dataset. This means `order_id` can be safely enforced as a strict Primary Key without fear of immediate conflicts.

## 3. products.parquet
* **Observation 1 (Clean & Strongly Typed):** As is typical for Parquet files, the data is highly structured with enforced types (`float64` for prices/weights, `int32` for quantities). It is perfectly clean, containing exactly 0 nulls and 0 duplicated rows, making it the lowest-risk source to ingest.
* **Observation 2 (Domain/Range Boundaries):** Profiling the numeric columns confirms that the business logic is intact. For example, the minimum `stock_quantity` is `0` (no invalid negative inventory), and `unit_price` and `weight_kg` are strictly positive. We can enforce `CHECK (stock_quantity >= 0)` in our future schema based on this evidence.