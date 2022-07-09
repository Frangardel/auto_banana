import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect('flights_db.sqlite3')

c = conn.cursor()

flight_df = pd.read_sql_query("SELECT * FROM flight", conn)

st.dataframe(flight_df)



