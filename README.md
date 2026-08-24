# DSS150P Laboratory 01: Environment Validation and Source Profiling

**Author:** Vincenzo Luis Risma
**Student Number:** 2024100793

## Purpose of the Laboratory
The purpose of this laboratory is to establish a local data engineering environment, acquire and profile various raw data sources (CSV, JSON, Parquet, REST API, PostgreSQL), define formal schema requirements, and document a data contract to prevent downstream pipeline failures.

## Software Requirements
* Git
* Docker Desktop
* Python 3.10+
* VS Code (or preferred IDE)

## Exact Steps to Reproduce the Environment
1. Clone the repository locally.
2. Open a terminal in the project root.
3. Create a virtual environment: `python -m venv .venv`
4. Activate the virtual environment:
   * Windows: `source .venv/Scripts/activate`
   * Mac/Linux: `source .venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`

## Exact Commands to Start and Stop PostgreSQL
* **Start:** `docker compose up -d`
* **Stop:** `docker compose down`

## How to Run Each Python Script
Ensure the `.venv` is active and the PostgreSQL container is running before executing:
* **Verify Environment:** `python src/verify_environment.py`
* **Profile Sources:** `python src/profile_sources.py`
* **Fetch API Data:** `python src/fetch_api.py`
* **Database Inspection:** `python src/db_inspect.py`

## Description of Each Source
* `customers.csv`: A flat file containing customer demographic data and signup dates.
* `orders.json`: A semi-structured JSON file capturing transactional orders, including nested shipping dictionaries.
* `products.parquet`: A strongly typed, columnar storage file containing inventory details.
* `JSONPlaceholder API`: An external REST API serving mock post data in JSON format.
* `support_tickets` (PostgreSQL): A relational database table containing customer support interactions.

## Known Limitations or Unresolved Questions
* **Data Quality Issues:** The `customers.csv` source contains duplicate rows that cause primary key violations if not handled explicitly. Additionally, `orders.json` contains orphaned records referring to non-existent customers.
* **API Volatility:** The external JSONPlaceholder API does not have a guaranteed schema contract, making it vulnerable to breaking changes upstream.
* **AI Usage:** The usage of this tool became an staple and essential part to properly and promptly create the key parts of a code. General application was done to various aspects of the project.