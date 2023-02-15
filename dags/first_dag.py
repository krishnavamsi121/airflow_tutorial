from datetime import datetime, timedelta
from airflow import DAG

default_args = {
    'owner' : 'krish',
    'retries' : 5,
    'retry_delay' : timedelta(minutes=2)
}

with DAG(
    dag_id = 'first_dag',
    default_args = default_args,
    description = 'This is my first dag',
    start_date = datetime(2023,7,29,2),
    schedule_interval = '@daily'
    ) as dag:
    pass