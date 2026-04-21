# =========================
# CREATE TABLES
# =========================

CREATE_TRIPS_TABLE_SQL = """



CREATE TABLE IF NOT EXISTS trips (
    idx INTEGER,
    trip_id INTEGER,
    starttime VARCHAR(50),
    stoptime VARCHAR(50),
    bikeid INTEGER,
    tripduration INTEGER,
    from_station_id INTEGER,
    from_station_name VARCHAR(255),
    to_station_id INTEGER,
    to_station_name VARCHAR(255),
    usertype VARCHAR(50),
    gender VARCHAR(10),
    birthyear FLOAT
);
"""

CREATE_STATIONS_TABLE_SQL = """

DROP TABLE IF EXISTS stations;


CREATE TABLE stations (
    idx INTEGER,
    station_id INTEGER,
    name VARCHAR(255),
    latitude FLOAT,
    longitude FLOAT,
    dpcapacity INTEGER,
    online_date VARCHAR(50)
);
"""


# =========================
# COPY FROM S3
# =========================

COPY_ALL_TRIPS_SQL = """
COPY trips
FROM 's3://s3-airflow-malek/Divvy_Trips_Simplified_2015_07.csv'
IAM_ROLE 'arn:aws:iam::442129305835:role/myRedshiftRole'
CSV
IGNOREHEADER 1
TIMEFORMAT 'auto';
"""

COPY_STATIONS_SQL = """
COPY stations
FROM 's3://s3-airflow-malek/Divvy_Stations.csv'
IAM_ROLE 'arn:aws:iam::442129305835:role/myRedshiftRole'
CSV
IGNOREHEADER 1;
"""



CREATE_Clean_TRIPS_TABLE_SQL = """
DROP TABLE IF EXISTS clean_trips;

CREATE TABLE clean_trips AS
SELECT
    trip_id,
    bikeid,
    tripduration
FROM trips;
"""



COPY_Monthly_TRIPS_SQL = """
COPY trips
FROM 's3://s3-airflow-malek/{{ds[:4]}}/{{ds[5:7]}}/Divvy_Trips_Simplified_{{ds[:4]}}_{{ds[5:7]}}.csv'
IAM_ROLE 'arn:aws:iam::442129305835:role/myRedshiftRole'
CSV
IGNOREHEADER 1
TIMEFORMAT 'auto';
"""    
