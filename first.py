import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Analyze a given sales dataset to extract insights like total revenue, best-selling products, and monthly trends.
# Load dataset
file_path = r'C:\Users\91620\OneDrive\Desktop\New 2025\sales_data.csv'
df = pd.read_csv(file_path)
# Streamlit App
st.title("Sales Data Analysis Dashboard")
# Data Cleaning
# Drop duplicates
df.drop_duplicates(inplace=True)
# Handle missing values
df.dropna(inplace=True)

# Convert date column to datetime if applicable
if 'Sale_Date' in df.columns:
    df['Sale_Date'] = pd.to_datetime(df['Sale_Date'])
    df['Month'] = df['Sale_Date'].dt.to_period('M') 

# Display basic information
st.subheader("Initial Dataset Info")
st.write(df.head())

# Extract insights
if 'Sales_Amount' in df.columns:
    total_revenue = df['Sales_Amount'].sum()
    st.subheader("Total Revenue")
    st.write(f"${total_revenue:,.2f}")

if 'Product_Category' in df.columns and 'Quantity_Sold' in df.columns:
    best_sellers = df.groupby('Product_Category')['Quantity_Sold'].sum().sort_values(ascending=False)
    st.subheader("Best-Selling Products")
    st.write(best_sellers.head(10))

if 'Month' in df.columns and 'Sales_Amount' in df.columns:
    monthly_trend = df.groupby('Month')['Sales_Amount'].sum()
    st.subheader("Monthly Revenue Trend")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x=monthly_trend.index.astype(str), y=monthly_trend.values, marker='o', ax=ax)
    plt.xticks(rotation=45)
    plt.xlabel("Month")
    plt.ylabel("Total Revenue")
    plt.title("Monthly Revenue Trend")
    st.pyplot(fig)
