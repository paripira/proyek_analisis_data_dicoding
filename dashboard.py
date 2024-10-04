import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Judul dashboard
st.title('Bike Rentals Dashboard')

# Memuat data dari file CSV
df = pd.read_csv('all_data.csv')
# Sidebar untuk filter
st.sidebar.header('Filter Options')
days_selected = st.sidebar.multiselect('Select Days', df['weekday_x'].unique(), df['weekday_x'].unique())
weather_selected = st.sidebar.selectbox('Select Weather', df['weathersit_x'].unique())

# Filter data berdasarkan pilihan sidebar
filtered_data = df[(df['weekday_x'].isin(days_selected)) & (df['weathersit_x'] == weather_selected)]

# Line chart untuk jumlah rental per jam berdasarkan cuaca
st.subheader('Number of Rentals per Hour Based on Weather')
hourly_rentals = filtered_data.groupby('hr')['cnt_y'].sum()

fig, ax = plt.subplots()
ax.plot(hourly_rentals.index, hourly_rentals.values, color='red' if weather_selected == 'Mist' else 'yellow', marker='o', linestyle='-', alpha=0.7)
ax.set_xlabel('Hour of the Day')
ax.set_ylabel('Number of Rentals')
ax.set_title('Bike Rentals per Hour')
st.pyplot(fig)

# Bar chart penggunaan sepeda casual dan registered
st.subheader('Bike Rentals by Casual and Registered Users')
daily_rentals = filtered_data.groupby('weekday_x')[['casual_y', 'registered_y']].sum()

fig, ax = plt.subplots()
index = np.arange(len(daily_rentals))
bar_width = 0.35
ax.bar(index, daily_rentals['registered_y'], bar_width, label='Registered', color='purple')
ax.bar(index + bar_width, daily_rentals['casual_y'], bar_width, label='Casual', color='pink')

ax.set_xlabel('Days')
ax.set_ylabel('Total Rentals')
ax.set_title('Bike Rentals by Casual and Registered Users')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(daily_rentals.index)
ax.legend()

st.pyplot(fig)