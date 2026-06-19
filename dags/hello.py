from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'datamasterylab.com',
    'start_date': datetime(2026, 6, 19),
    'catchup': False,
}

dag = DAG(

    dag_id='hello_world_dag',
    default_args=default_args,
    schedule=timedelta(days=1),
)

t1 = BashOperator(
    task_id='hello_world_task1',
    bash_command='echo "Hello, World!"',
    dag=dag,
)

t2 = BashOperator(
    task_id='hello_world_task2',
    bash_command='echo "Hello, Data Mastery Lab!"',
    dag=dag,
)

t1 >> t2

