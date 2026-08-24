# Source Inventory

## 1. Customers Data
* **Source name:** `customers.csv`
* **Source-system type:** Flat file / Export
* **Data format:** CSV
* **Structured / semi-structured / unstructured:** Structured
* **Expected update pattern:** Batch (e.g., daily or weekly dumps)
* **Likely acquisition method:** SFTP, cloud storage bucket drop, or file transfer
* **Schema location or schema owner:** CRM Team / Unknown - requires confirmation
* **Possible primary/business key:** `customer_id` (pending profiling verification)
* **Potential schema-evolution risk:** Columns might be reordered, renamed, or new columns appended without notice.
* **Potential data-quality risk:** Missing values, inconsistent text formatting, or duplicate records.

## 2. Orders Data
* **Source name:** `orders.json`
* **Source-system type:** Web Application / E-commerce Platform
* **Data format:** JSON
* **Structured / semi-structured / unstructured:** Semi-structured
* **Expected update pattern:** Incremental or event-driven (streaming)
* **Likely acquisition method:** Message queue (e.g., Kafka) or API extraction
* **Schema location or schema owner:** Application Development Team
* **Possible primary/business key:** `order_id`
* **Potential schema-evolution risk:** Nested arrays or objects changing structure; new dynamic keys being added.
* **Potential data-quality risk:** Missing expected keys, or varying data types for the same field (e.g., string vs. integer).

## 3. Products Data
* **Source name:** `products.parquet`
* **Source-system type:** Data Lake / Analytics Storage
* **Data format:** Parquet
* **Structured / semi-structured / unstructured:** Structured
* **Expected update pattern:** Batch or micro-batch
* **Likely acquisition method:** Direct read from cloud storage (e.g., S3) or local file system
* **Schema location or schema owner:** Inventory/Data Warehouse Team (Schema is embedded in the file metadata)
* **Possible primary/business key:** `product_id`
* **Potential schema-evolution risk:** Data type mismatches if upstream producers change the writer schema without updating downstream consumers.
* **Potential data-quality risk:** Null values in critical filtering columns or corrupted file blocks.

## 4. External REST API
* **Source name:** JSONPlaceholder Posts API
* **Source-system type:** External Web Service
* **Data format:** JSON
* **Structured / semi-structured / unstructured:** Semi-structured
* **Expected update pattern:** On-demand / Incremental
* **Likely acquisition method:** HTTP GET requests using Python
* **Schema location or schema owner:** Third-party API provider
* **Possible primary/business key:** `id`
* **Potential schema-evolution risk:** The provider releases a new API version (e.g., v2) that changes the payload structure or deprecates fields.
* **Potential data-quality risk:** Network timeouts, rate limiting causing incomplete data pulls, or unexpected HTTP error codes.

## 5. Relational Database Sample
* **Source name:** PostgreSQL Sample Table (`inventory_snapshot` or similar)
* **Source-system type:** Relational Database Management System (RDBMS)
* **Data format:** SQL Table
* **Structured / semi-structured / unstructured:** Structured
* **Expected update pattern:** Continuous / Transactional updates
* **Likely acquisition method:** SQL query extract (JDBC/ODBC) or Change Data Capture (CDC)
* **Schema location or schema owner:** Database Administrator (DBA)
* **Possible primary/business key:** Database Primary Key (e.g., `id` or a composite key)
* **Potential schema-evolution risk:** An `ALTER TABLE` command drops or renames a column that the pipeline relies on.
* **Potential data-quality risk:** Constraints being disabled, leading to orphaned records or referential integrity loss.