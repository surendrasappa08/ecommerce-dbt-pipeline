# E-Commerce dbt + Airflow Pipeline

End-to-end data pipeline for e-commerce sales analytics using dbt, Airflow, and PostgreSQL.

## Stack
- **PostgreSQL** — local data warehouse
- **Python** — synthetic data generation (500 rows)
- **dbt** — SQL transformations (staging → marts)
- **Apache Airflow** — pipeline orchestration (daily schedule)

## Architecture
Raw Orders → PostgreSQL → dbt Staging → dbt Marts → Dashboard

## dbt Models
- `stg_orders` — cleans raw orders, calculates total_amount
- `mart_sales_summary` — aggregates revenue by category, product, and month

## Airflow DAG
- DAG: `ecommerce_dbt_pipeline`
- Schedule: daily
- Tasks: `dbt_run` → `dbt_test`

## Results
- 500 raw orders loaded
- Revenue aggregated by category (Electronics, Clothing, Food)
- dbt run: PASS=4 ERROR=0
- Dashboard: [E-Commerce Sales Dashboard](https://datastudio.google.com/reporting/ed240629-8f35-4bd9-91ab-b22e43386caa)

## Setup
```bash
python3 -m venv venv && source venv/bin/activate
pip install dbt-postgres apache-airflow
psql -d ecommerce_db -U dbt_user
dbt run
```

## Author
Surendra Sappa | Data Engineer