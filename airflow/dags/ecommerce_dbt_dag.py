from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'surendra',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='ecommerce_dbt_pipeline',
    default_args=default_args,
    description='Run dbt models for ecommerce pipeline',
    schedule='@daily',
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=['ecommerce', 'dbt'],
) as dag:

    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='cd /Users/happie/Desktop/ecommerce-dbt-pipeline/ecommerce_dbt && source /Users/happie/Desktop/ecommerce-dbt-pipeline/venv/bin/activate && dbt run',
    )

    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command='cd /Users/happie/Desktop/ecommerce-dbt-pipeline/ecommerce_dbt && source /Users/happie/Desktop/ecommerce-dbt-pipeline/venv/bin/activate && dbt test',
    )

    dbt_run >> dbt_test