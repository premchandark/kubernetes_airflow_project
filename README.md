# Kubernetes-Native Apache Airflow Data Pipeline

## Overview

This project demonstrates how to deploy and run Apache Airflow on Kubernetes using Helm and the KubernetesExecutor. Instead of running tasks on a single machine, every Airflow task is executed as a separate Kubernetes pod, providing better isolation and scalability.

One of the key goals of this project was to learn how modern data engineering platforms are deployed in production environments using Kubernetes, Git-based workflow management, and containerized execution.

The DAGs are automatically synchronized from GitHub using GitSync, which means any changes pushed to the repository are automatically reflected in Airflow without rebuilding Docker images.

---

## Why I Built This Project

As someone interested in Data Engineering and Cloud technologies, I wanted hands-on experience with:

* Apache Airflow
* Kubernetes
* Helm Charts
* GitOps workflows
* Workflow orchestration
* Containerized task execution

Most beginner Airflow projects run locally using SequentialExecutor or LocalExecutor. I wanted to go beyond that and understand how Airflow works in a Kubernetes environment where tasks are dynamically created and managed as pods.

---

## Architecture

```text
GitHub Repository
        │
        ▼
     GitSync
        │
        ▼
 Apache Airflow
        │
        ▼
KubernetesExecutor
        │
        ▼
Worker Pods Created Dynamically
        │
        ▼
 Data Processing Tasks
```

---

## Technologies Used

* Apache Airflow 3.2.2
* Kubernetes
* Helm
* GitSync
* PostgreSQL
* Python
* Git & GitHub
* Docker Desktop Kubernetes

---

## Key Features

### KubernetesExecutor

Every task runs inside its own Kubernetes pod.

Instead of using local execution, Airflow dynamically creates pods when tasks are triggered and removes them after execution.

### GitSync Integration

DAGs are stored in GitHub and automatically synchronized into Airflow.

Benefits:

* No manual file copying
* Version-controlled workflows
* Easy updates through GitHub

### PostgreSQL Backend

Airflow metadata is stored in PostgreSQL.

This includes:

* DAG runs
* Task status
* Scheduling information
* Execution history

### Helm-Based Deployment

The entire Airflow platform is deployed using Helm charts, making installation and upgrades much easier.

---

## Project Structure

```text
kubernetes_airflow_project/
│
├── dags/
│   └── fetch_and_preview.py
│
├── values.yaml
│
├── airflow-backup.yaml
│
└── README.md
```

---

## Sample Workflow

### Fetch and Preview DAG

The sample DAG performs:

1. Reads sample data
2. Processes the data
3. Performs aggregation
4. Displays summarized results

Example output:

```text
Category       Total
-----------------------
Electronics    10199.65
Fashion          319.94
Home             269.79
Tools            151.96
Sports           149.92
```

---

## Deployment Steps

### Add Airflow Helm Repository

```bash
helm repo add apache-airflow https://airflow.apache.org
helm repo update
```

### Install Airflow

```bash
helm install airflow apache-airflow/airflow \
--namespace airflow \
--create-namespace
```

### Verify Pods

```bash
kubectl get pods -n airflow
```

Example:

```text
airflow-api-server
airflow-scheduler
airflow-triggerer
airflow-postgresql
airflow-dag-processor
```

### Access Airflow UI

```bash
kubectl port-forward svc/airflow-api-server 8080:8080 -n airflow
```

Then open:

```text
http://localhost:8080
```

---

## GitSync Configuration

```yaml
dags:
  gitSync:
    enabled: true
    repo: https://github.com/premchandark/kubernetes_airflow_project.git
    branch: main
    rev: HEAD
    depth: 1
    maxFailures: 0
    subPath: dags
```

This configuration automatically syncs DAG files from GitHub into Airflow.

---

## Monitoring Execution

View Airflow resources:

```bash
kubectl get pods -n airflow
```

View task logs:

```bash
kubectl logs <pod-name> -n airflow
```

Example:

```bash
kubectl logs fetch-and-preview-dag-preview-data-rwcgp6sh -n airflow
```

---

## Challenges Faced and Solutions

### GitHub Synchronization Issues

Initially, DAG updates were not appearing in Airflow because the Git repository was not properly synchronized.

**Solution:**

* Verified GitSync configuration
* Fixed repository structure
* Confirmed DAG folder path

### KubernetesExecutor Log Visibility

Task logs were generated successfully but were not visible in the Airflow UI.

**Solution:**

* Verified logs directly from Kubernetes pods
* Confirmed task execution through pod logs
* Learned how Airflow handles logs when using KubernetesExecutor

### Helm Upgrade Errors

While updating Airflow configurations, some Helm upgrades failed due to StatefulSet restrictions.

**Solution:**

* Backed up Helm values
* Recreated affected resources
* Applied configuration changes safely

---

## What I Learned

This project helped me understand:

* How Airflow works internally
* How KubernetesExecutor launches task-specific pods
* Deploying applications with Helm
* GitOps-style workflow management
* Kubernetes troubleshooting
* Airflow scheduling and task lifecycle
* PostgreSQL integration with Airflow

---

## Future Improvements

Some enhancements I plan to add in future versions:

* Real-world ETL pipeline
* AWS integration
* Data warehouse integration
* Apache Spark jobs
* CI/CD pipeline using GitHub Actions
* Monitoring with Grafana and Prometheus

---

## Project Outcome

Successfully deployed Apache Airflow on Kubernetes using Helm, configured GitSync for automatic DAG deployment, executed workflows using KubernetesExecutor, and managed the entire setup through Kubernetes-native tools.

This project provided practical experience with technologies commonly used in modern Data Engineering platforms.

---

## Author

**Premchandar K**

GitHub: https://github.com/premchandark
