# 🚀 ETL Pipeline using Apache Airflow & AWS Redshift

## 📌 Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline built using Apache Airflow and AWS Redshift.

The pipeline automates data ingestion from Amazon S3 into Redshift, performs transformations, and validates data quality.

---



## 🧱 Architecture

S3 → Redshift (Raw Tables) → Transform → Clean Tables

---

## ⚙️ Technologies Used

* Apache Airflow (Dockerized)
* AWS S3
* AWS Redshift
* SQL
* Python

---

## 🔄 Pipeline Workflow

1. **Create Tables**

   * Creates raw tables (`trips`, `stations`) in Redshift

2. **Load Data from S3**

   * Uses the `COPY` command with IAM Role for secure data ingestion

3. **Transform Data**

   * Creates a cleaned table (`clean_trips`) from raw data

4. **Data Quality Check**

   * Validates data using SQL checks (e.g., row count)

---

<img width="1920" height="1080" alt="Screenshot (1653)" src="https://github.com/user-attachments/assets/6e6ea0e6-5ff9-483a-9da3-0fdf00f71713" />
<img width="1920" height="1080" alt="Screenshot (1652)" src="https://github.com/user-attachments/assets/72fec91e-2508-40c7-830c-610d65820be0" />
<img width="1920" height="1080" alt="Screenshot (1655)" src="https://github.com/user-attachments/assets/813f3349-b0f8-470b-99bb-ea9bbf7047e4" />
<img width="1920" height="1080" alt="Screenshot (1654)" src="https://github.com/user-attachments/assets/6419cbee-0e91-4e53-b2cb-fa6f8df85c7e" />


## 🔐 Security

* Uses IAM Role (`myRedshiftRole`) instead of hardcoded AWS credentials
* Avoids exposing sensitive data in code

---

## 🧠 Key Concepts Demonstrated

* Airflow DAG design and scheduling
* Task dependencies and orchestration
* Idempotent pipeline design (avoiding duplicate data)
* SQL-based transformations
* Data quality validation
* AWS integration (S3 + Redshift)

---

## 📂 Project Structure

```
airflow-redshift-etl/
│
├── dags/
│   └── etl_pipeline.py
│
├── sql/
│   └── sql_statements.py
│
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🚀 How to Run

1. Start Airflow using Docker:

```
docker compose up
```

2. Open Airflow UI:

```
http://localhost:8080
```

3. Trigger the DAG:

```
etl_s3_to_redshift_pipeline
```

---

## 📊 Example Data

* Bike trip data stored in S3
* Loaded into Redshift for analysis

---

## 🔍 Improvements (Future Work)

* Incremental loading using Airflow execution date (`ds`)
* Partitioned data ingestion
* Advanced data quality checks
* Custom Airflow operators
* Integration with data lineage tools (OpenLineage)

---

## 💼 Use Case

This project simulates a real-world data engineering workflow where data is:

* Extracted from a data lake (S3)
* Loaded into a data warehouse (Redshift)
* Transformed for analytics
* Validated for quality

---

## 📬 Contact

Feel free to connect with me on LinkedIn or reach out for collaboration!


