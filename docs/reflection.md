# Laboratory 01 Reflection

**1. Which source would be easiest to integrate into a future pipeline, and why?**
The `products.parquet` file is the easiest to integrate. Because Parquet is a strictly typed, columnar format, the schema is embedded directly within the metadata. Our profiling script revealed zero missing values, zero duplicated rows, and well-enforced numeric boundaries (such as zero negative values for stock). This strict structure removes the need for heavy data cleansing and allows the ingestion pipeline to parse the data reliably without complex type-casting overhead.

**2. Which source presents the greatest schema or data-quality risk, and what evidence supports your answer?**
The `orders.json` source presents the greatest risk. Profiling revealed nested dictionary objects within the `shipping` column, which prevents standard relational mapping and requires explicit flattening logic. Furthermore, when attempting basic ingestion, the pipeline triggered a Foreign Key Violation because an order referenced a `customer_id` (C0223) that did not exist in the `customers.csv` file. This lack of referential integrity in the source data poses a severe risk of orphaned records crashing downstream analytics.

**3. What could go wrong if a pipeline is built before the source schema and contract are understood?**
Building a pipeline blindly leads to catastrophic ingestion failures. Without understanding constraints, duplicate primary keys (like C0090 in our CSV) or unexpected null values will trigger immediate database crashes. Without a data contract, upstream application developers might rename a field or nest a previously flat column, silently breaking transformations and leading to corrupted, untrustworthy data in the warehouse.

**4. How do Git, virtual environments, containers, and documentation improve reproducibility for a data-engineering team?**
These tools eliminate the "it works on my machine" problem. Virtual environments (`.venv`) lock Python dependencies, while Docker containers isolate the exact PostgreSQL operating system, ports, and version. Git provides an auditable history of codebase changes and allows developers to collaborate safely. Finally, clear documentation acts as the blueprint, allowing any new engineer to pull the code, spin up the identical architecture, and execute scripts successfully within minutes.