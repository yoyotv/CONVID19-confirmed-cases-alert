import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'Neil',
    'start_date': dt.datetime(2020, 5, 7, 10, 00, 00),
    'concurrency': 1,
    'retries': 1
}

with DAG('my_simple_dag',
         catchup=False,
         default_args=default_args,
	 schedule_interval='*/5 * * * *',  # run every 5 minutes
         ) as dag:

    opr_hello = BashOperator(task_id='say_Hi',
                             bash_command='echo "Hi!!"')


    opr_convid19 = BashOperator(task_id='convid19',
                             bash_command="/home/ucare/test.sh ",
			     )


opr_hello >> opr_convid19
