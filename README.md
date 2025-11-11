
# 🧩 End-To-End Data Pipeline

*(Vietnamese & English Overview)*

## 🚀 Giới thiệu / Introduction

**End-To-End Data Pipeline** là dự án mô phỏng quy trình xử lý dữ liệu hoàn chỉnh — từ **Ingestion → Validation → Transformation → Storage → Monitoring**.
Mục tiêu là xây dựng một nền tảng dữ liệu hiện đại (Modern Data Platform) có khả năng **tự động hoá luồng dữ liệu**, đảm bảo **tính chính xác, mở rộng và giám sát được**.

This project demonstrates a full **data engineering pipeline** integrating **Apache Airflow**, **Spark**, **PostgreSQL**, and **data quality monitoring**, showcasing orchestration, ETL/ELT best practices, and modular architecture for real-world analytics.

---

## 🏗️ Kiến trúc hệ thống / System Architecture

```text
             ┌──────────────────┐
             │  Data Sources     │
             │ (API / Files / DB)│
             └────────┬─────────┘
                      │
                      ▼
              ┌─────────────────┐
              │  Ingestion Layer │  →  Extract raw data
              └─────────────────┘
                      │
                      ▼
              ┌─────────────────┐
              │ Validation Layer │  →  Great Expectations, schema checks
              └─────────────────┘
                      │
                      ▼
              ┌─────────────────┐
              │ Transformation   │  →  Spark jobs (cleaning, join, enrich)
              └─────────────────┘
                      │
                      ▼
              ┌─────────────────┐
              │ Storage Layer    │  →  PostgreSQL / Data Warehouse
              └─────────────────┘
                      │
                      ▼
              ┌─────────────────┐
              │ Monitoring & DAG │  →  Airflow, Logs, Metrics
              └─────────────────┘
```

---

## ⚙️ Công nghệ sử dụng / Tech Stack

| Layer                          | Tools & Frameworks        |
| ------------------------------ | ------------------------- |
| **Orchestration**        | Apache Airflow            |
| **Transformation**       | Apache Spark              |
| **Validation**           | Great Expectations        |
| **Storage**              | PostgreSQL, MinIO         |
| **Monitoring & Logging** | Airflow UI, Custom Logger |
| **Containerization**     | Docker Compose            |
| **Config Management**    | Pydantic-based Configs    |

---

## 🧩 Các DAG chính / Main DAGs

| DAG Name                | Description                                                |
| ----------------------- | ---------------------------------------------------------- |
| `batch_ingestion_dag` | Thu thập và lưu dữ liệu thô từ nhiều nguồn.       |
| `data_quality_dag`    | Kiểm tra chất lượng dữ liệu (schema, nulls, ranges). |
| `monitoring_dag`      | Theo dõi pipeline và gửi cảnh báo khi thất bại.     |

## 👨‍💻 Tác giả / Author

**Đỗ Văn Cường**
📫 Email: [dovancuong3636@gmail.com](mailto:dovancuong3636@gmail.com)
🌐 GitHub: [dovancuong12](https://github.com/dovancuong12)
