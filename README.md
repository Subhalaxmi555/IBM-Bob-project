# 🛒 Supermarket Sales Analysis

A full-stack data analytics project built with **Python Flask (backend)** and **Streamlit (frontend)** for analysing supermarket sales data.

---

## 📁 Project Structure

```
supermarket_analysis/
├── data/
│   └── supermarket_sales.csv          # Dataset (500 rows)
├── backend/
│   ├── data_loader.py                 # CSV loading & feature engineering
│   ├── analytics.py                   # All analytics computations
│   ├── app.py                         # Flask REST API (port 5000)
│   └── train_model.py                 # ML model training script
├── frontend/
│   └── dashboard.py                   # Streamlit dashboard (port 8501)
├── models/
│   ├── sales_model.pkl                # Trained model (after running train_model.py)
│   ├── feature_cols.pkl               # Model feature columns
│   └── model_meta.pkl                 # Model metadata & scores
├── reports/                           # Generated analysis outputs
├── requirements.txt                   # Python dependencies
└── run.ps1                            # One-click startup script (Windows)
```

---

## 🚀 Quick Start

### 1. Install dependencies
```powershell
pip install -r requirements.txt
```

### 2. Train the ML model (run once)
```powershell
cd backend
python train_model.py
```

### 3. Start the Flask API backend
```powershell
cd backend
python app.py
# Runs on http://localhost:5000
```

### 4. Start the Streamlit frontend (new terminal)
```powershell
cd frontend
streamlit run dashboard.py
# Opens http://localhost:8501
```

### Or: Use the one-click script
```powershell
.\run.ps1
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/health` | API health check |
| GET | `/api/summary` | KPI summary statistics |
| GET | `/api/sales/category` | Sales by product category |
| GET | `/api/sales/city` | Sales by city |
| GET | `/api/sales/branch` | Sales by branch |
| GET | `/api/sales/monthly` | Monthly sales trend |
| GET | `/api/sales/payment` | Sales by payment method |
| GET | `/api/sales/gender` | Sales by gender |
| GET | `/api/sales/customer-type` | Member vs Normal customers |
| GET | `/api/sales/top-products?n=10` | Top N products by sales |
| GET | `/api/sales/ratings` | Rating distribution |
| GET | `/api/sales/heatmap` | Category × City sales heatmap |
| GET | `/api/sales/day-of-week` | Sales by day of week |
| GET | `/api/sales/quarterly` | Quarterly sales |
| GET | `/api/sales/correlation` | Numeric feature correlation matrix |
| GET | `/api/data?category=&city=&branch=&limit=100` | Filtered raw data |
| POST | `/api/predict` | ML sales prediction |

---

## 🤖 ML Model

- **Algorithm:** Random Forest Regressor / Gradient Boosting (best selected)
- **Features:** Category, City, Quantity, Unit Price, Customer Type, Gender, Payment
- **Target:** Sales (₹)
- **Evaluation:** MAE, RMSE, R², 5-fold cross-validation

---

## 📊 Dashboard Pages

| Page | Content |
|------|---------|
| 📊 Dashboard | KPI cards, category donut, city/branch bar charts |
| 📈 Sales Trends | Monthly line chart, day-of-week, quarterly funnel |
| 🏪 Products & Categories | Top products, category×city heatmap, rating distribution |
| 👥 Customer Insights | Gender, customer type, correlation matrix |
| 🗺️ Geographic Analysis | City comparison, branch treemap, stacked category bars |
| 🤖 ML Predictor | Form-based sales prediction with gauge chart |
| 📋 Data Explorer | Filterable table with CSV download |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend API | Flask 3.0, Flask-CORS |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn (Random Forest, Gradient Boosting) |
| Visualisation | Plotly Express, Plotly Graph Objects |
| Frontend | Streamlit 1.36 |
| Serialisation | Joblib |

---

## 📋 Dataset Columns

`Invoice ID`, `Date`, `Branch`, `City`, `Customer Type`, `Gender`, `Product`, `Category`, `Quantity`, `Unit Price`, `Payment`, `Rating`, `Sales`

- **Branches:** A (Jaipur), B (Delhi), C (Mumbai), D (Bengaluru)
- **Categories:** Dairy, Grocery, Snacks, Personal Care, Fruits, Vegetables, Beverages, Bakery
- **Payment:** Cash, Card, UPI, Net Banking
