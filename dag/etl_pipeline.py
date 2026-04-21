import datetime

from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

import sql_statements


with DAG(
    dag_id="etl_s3_to_redshift_pipeline",
    start_date=datetime.datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    # =========================
    # CREATE TABLES
    # =========================
    create_trips_table = SQLExecuteQueryOperator(
        task_id="create_trips_table",
        conn_id="redshift_default",
        sql=sql_statements.CREATE_TRIPS_TABLE_SQL,
    )

    create_stations_table = SQLExecuteQueryOperator(
        task_id="create_stations_table",
        conn_id="redshift_default",
        sql=sql_statements.CREATE_STATIONS_TABLE_SQL,
    )

    # =========================
    # COPY FROM S3 (USING IAM ROLE)
    # =========================
    copy_trips_task = SQLExecuteQueryOperator(
        task_id="copy_trips",
        conn_id="redshift_default",
        sql=sql_statements.COPY_ALL_TRIPS_SQL,
    )

    copy_stations_task = SQLExecuteQueryOperator(
        task_id="copy_stations",
        conn_id="redshift_default",
        sql=sql_statements.COPY_STATIONS_SQL,
    )

    data_quality = SQLExecuteQueryOperator(
    task_id="data_quality_check",
    conn_id="redshift_default",
    sql="SELECT COUNT(*) FROM trips;",
    )

    create_clean_trips_table = SQLExecuteQueryOperator(
        task_id="create_clean_trips_table",
        conn_id="redshift_default",
        sql=sql_statements.CREATE_Clean_TRIPS_TABLE_SQL,
    )

    # =========================
    # DEPENDENCIES
    # =========================
    create_trips_table >> copy_trips_task
    create_stations_table >> copy_stations_task
    copy_trips_task >> data_quality
    data_quality >> create_clean_trips_table
