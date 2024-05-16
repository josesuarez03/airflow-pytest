from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'retries': 1,
}

with DAG('pytest_dag',
          default_args=default_args,
          description='Un DAG para correr Pytest',
          schedule_interval='@daily',
          start_date=datetime(2023, 1, 1),
          catchup=False) as dag:

    t1 = BashOperator(
        task_id='run_pytest',
        bash_command='pytest /path/to/your/test_ejemplo.py'
    )

    t1
