# 💡 Resource Data Pipeline

# 📌 Overview
This project implements a **production-like data pipeline** for workforce and recource utilization analytics.

The pipeline integrates **planned allocation data and actual timesheets**, transforms them into a unified analytical model and delivers a curated dataset for downstream BI and reporting.

---

## 🎯 Business Context
Project-based organizations face ongoing challenges in workforce management:

- lack of alignment between planned and actual workload
- inefficient resource allocation across projects
- employee overload or underutilization
- limited visibility at organizational levels

This pipeline enables **centralized, reliable, and scalable data processing** to support data-driven resource planning and decision-making.

---

## ⚙️ Architecture
The pipeline follows a layered architecture:

 ### 1. Sources
 - planned allocation data
 - actual timesheet data
 - employee master data

### 2. Staging
- ingestion of raw data as-is
- schema alignment and basic validation

### 3. Transformation
- data cleaning and normalization
- enrichment with organizational attributes
- calculation of business metrics

### 4. Data Mart
- curated table (workload)
- optimized for analytical queries and BI tools

---

## 🛢️ Data Model
The final dataset follows a **denormalized fact table approach**:

- employee_id
- project_id
- date
- planned_hours
- actual_hours
- capacity
- idle_time
- department
- unit
- roles
- fte

Supports hierarchical analysis:

Project ⭢ Unit ⭢ Employee

---

## 📊 Key Metrics

### Workload & Performance
- Planned Mhrs
- Spent Mhrs

### Capacity Management
- Capacity (based on FTE)

### Efficiency
- Idle Mhrs

---

## 🧠 Pipeline Components
**Extract**
- reads raw datasets from configures sources
- includes error handling and logging

**Transform**
- merges planned and actual datasets
- applies business logic
- handles missing values and inconsistencies

**Validate**
- enforces data quality checks:
    - non-null key
    - non-negative values
    - logical constraints

**Load**
- writes processed data to target layer
- ensures reproducibility and consistency

---

## 🛠️ Configuration
Pipeline behavior is controlled via a configuration file: config/config.yaml:
- input / output paths
- logging configuration

This enables flexibility and environment separation.

---

## 📈 Observation & Reliability
The pipeline includes:

- structured logging (execution steps, errors)
- exception handling across all stages
- validation layer for data quality assurance

These features ensure **traceability and robustness**, aligning with production standards.

---

## 🕐 Execution
Run the pipeline: main.py

Execution flow:
1. Load configuration
2. Initialize logging
3. Extract data
4. Transform data
5. Validate dataset
6. Load results

---

## 📥 Project Structure

data-pipeline/

|

|-- data/

    |-- raw/       #source data
    
    |--processed/  #curated dataset
    
|-- scripts/

    |-- extract.py

    |-- transform.py

    |-- validation.py

    |-- load.py

    |-- logger.py

|-- config/

|-- logs/

|-- main.py

|-- README.md

---

## 〰️ Design Principles

- modular pipeline architecture
- separation of concerns (extract / transform / load)
- reproducibility and configurability
- business-driven data modeling
- scalability for future extensions

## 📊 Downstream Usage
The output dataset is designed for:

- Power BI dashboards
- resource utilization analytics
- workload optimization

## 🖇️ Potential Extensions

- integration with relational databases (MS SQL, PostgreSQL)
- orchestration via scheduling tools
- containerization (Docker)
- automated testing (unit / data tests)
- incremental data loading

## 📍 Conclusion
This project demonstrates a **production-oriented approach to data pipeline development**, combining:
- data engineering practices
- domain-specific busic logic
- scalable architecture

It reflects the type of solution typically implemented in **enterprise data platforms and project-driven organizations**.
