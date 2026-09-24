"""
analysis.py
-----------
Core data-loading, cleaning, and summarisation logic for the
Supermarket Sales Analysis project.

All functions return plain DataFrames / scalars so the Streamlit
frontend (app.py) can render them however it likes.
"""

import pandas as pd
import numpy as np


# ─────────────────────────────────────────────
# 1.  LOAD
# ─────────────────────────────────────────────

def load_data(filepath: str) -> pd.DataFrame:
    """Load the CSV and apply basic type coercions."""
    df = pd.read_csv(filepath)

    # Normalise column names: strip whitespace
    df.columns = df.columns.str.strip()

    # Parse Date
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Ensure numeric columns are actually numeric
    for col in ["Quantity", "Unit Price", "Rating", "Sales"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


# ─────────────────────────────────────────────
# 2.  DATA QUALITY CHECK
# ─────────────────────────────────────────────

def data_quality_report(df: pd.DataFrame) -> dict:
    """
    Returns a summary dict with:
      - total_rows
      - total_columns
      - missing_values   (Series: col → count of NaNs)
      - duplicate_rows
      - dtypes           (Series)
    """
    missing = df.isnull().sum()
    missing = missing[missing > 0]  # only columns that have gaps

    return {
        "total_rows": len(df),
        "total_columns": len(df.columns),
        "missing_values": missing,
        "duplicate_rows": int(df.duplicated().sum()),
        "dtypes": df.dtypes,
    }


# ─────────────────────────────────────────────
# 3.  RECALCULATE / VALIDATE SALES COLUMN
# ─────────────────────────────────────────────

def recalculate_sales(df: pd.DataFrame) -> pd.DataFrame:
    """
    Recalculates Sales = Quantity × Unit Price and flags rows
    where the stored value differs from the computed value
    (absolute difference > 0.01 ₹).
    """
    df = df.copy()
    df["Computed_Sales"] = df["Quantity"] * df["Unit Price"]
    df["Sales_Match"] = np.abs(df["Sales"] - df["Computed_Sales"]) <= 0.01
    # Use the authoritative computed value going forward
    df["Sales"] = df["Computed_Sales"]
    return df


# ─────────────────────────────────────────────
# 4.  SUMMARY / AGGREGATIONS
# ─────────────────────────────────────────────

def summary_kpis(df: pd.DataFrame) -> dict:
    """High-level KPI cards."""
    return {
        "total_revenue": df["Sales"].sum(),
        "total_transactions": len(df),
        "avg_order_value": df["Sales"].mean(),
        "avg_rating": df["Rating"].mean(),
        "total_units_sold": df["Quantity"].sum(),
    }


def sales_by_category(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("Category")["Sales"]
        .agg(Total_Sales="sum", Transactions="count", Avg_Sale="mean")
        .sort_values("Total_Sales", ascending=False)
        .reset_index()
    )


def sales_by_branch(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby(["Branch", "City"])["Sales"]
        .agg(Total_Sales="sum", Transactions="count", Avg_Sale="mean")
        .sort_values("Total_Sales", ascending=False)
        .reset_index()
    )


def sales_by_payment(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("Payment")["Sales"]
        .agg(Total_Sales="sum", Transactions="count")
        .sort_values("Total_Sales", ascending=False)
        .reset_index()
    )


def sales_by_customer_type(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("Customer Type")["Sales"]
        .agg(Total_Sales="sum", Transactions="count", Avg_Sale="mean")
        .reset_index()
    )


def sales_by_gender(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("Gender")["Sales"]
        .agg(Total_Sales="sum", Transactions="count", Avg_Sale="mean")
        .reset_index()
    )


def monthly_trend(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Month"] = df["Date"].dt.to_period("M").astype(str)
    return (
        df.groupby("Month")["Sales"]
        .agg(Total_Sales="sum", Transactions="count")
        .reset_index()
        .sort_values("Month")
    )


def top_products(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    return (
        df.groupby("Product")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
        .rename(columns={"Sales": "Total_Sales"})
    )


def rating_by_category(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("Category")["Rating"]
        .agg(Avg_Rating="mean", Count="count")
        .sort_values("Avg_Rating", ascending=False)
        .reset_index()
    )


def category_gender_pivot(df: pd.DataFrame) -> pd.DataFrame:
    """Pivot: Category × Gender → Total Sales."""
    return df.pivot_table(
        index="Category", columns="Gender", values="Sales", aggfunc="sum"
    ).fillna(0)
