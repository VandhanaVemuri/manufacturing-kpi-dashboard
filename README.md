# Manufacturing Production KPI Dashboard

🔗 Live Demo: https://manufacturing-kpi-dashboard.onrender.com  
📂 GitHub Repository: https://github.com/VandhanaVemuri/manufacturing-kpi-dashboard

---

## Overview

The Manufacturing Production KPI Dashboard is a full-stack web application that simulates ERP/MES-style manufacturing data and transforms raw production metrics into actionable operational insights.

The dashboard enables monitoring of:

- Production Output Trends
- Defect Rate by Production Line
- Total Downtime by Line
- Inventory Level Trends
- Overall Line Efficiency

This project demonstrates applied analytics in a manufacturing systems context.

---

## Key Features

- Interactive web dashboard built with Flask
- KPI calculation using Pandas
- Production, quality, and inventory analytics
- Dynamic data aggregation by production line and date
- Plotly visualizations integrated into web interface
- Deployed using Gunicorn on Render
- Version controlled with Git and GitHub

---

## Technologies Used

- Python
- Flask
- Pandas
- Plotly
- Gunicorn
- Render (Cloud Deployment)
- Git / GitHub

---

## Business Objective

This project simulates how manufacturing organizations use operational data from ERP/MES systems to:

- Monitor production performance
- Identify quality issues (defect trends)
- Track downtime by production line
- Analyze inventory levels over time
- Support data-driven operational decisions

---

## Project Structure

manufacturing-kpi-dashboard/
│
├── app.py
├── requirements.txt
├── Procfile
├── data/
│ └── production_data.csv
└── templates/
└── dashboard.html


---

## Deployment

The application is deployed on Render using:

Build Command:
pip install -r requirements.txt


Start Command:


gunicorn app:app


---

## Future Improvements

- Add interactive filters (Production Line / Shift)
- Connect to live database instead of CSV
- Add authentication layer
- Enhance dashboard UI styling
