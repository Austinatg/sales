# streamlit_app.py
import streamlit as st
import pandas as pd
import requests
import os
import django
import sqlite3

os.environ['DJANGO_SETTINGS_MODULE'] = 'sales.settings'
django.setup()

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
cursor.execute('SELECT * FROM home_sales')
tables = cursor.fetchall()

def fetch_sales_data(user_id):
    print(user_id)
    # Adjust the URL to your local Django server and endpoint
    url = f'http://127.0.0.1:8000/sales-data/?user_id={user_id}'
    response = requests.get(url)
    if response.status_code == 200:
        sales_data = response.json()
        return pd.DataFrame(sales_data)
    else:
        st.error("Failed to fetch sales data")
        return pd.DataFrame()

# Main function to display the data and visualizations
def main():
    st.title("Sales Data Visualization")

    user_id = 1  # Hardcoded user_id, replace with dynamic user ID as needed
    df = fetch_sales_data(user_id)

    if not df.empty:
        st.write("Sales Data", df)
        st.bar_chart(df.groupby('product')['quantity'].sum())
        st.line_chart(df.groupby('order_date')['quantity'].sum())
    else:
        st.error("No sales data found")

if __name__ == "__main__":
    main()