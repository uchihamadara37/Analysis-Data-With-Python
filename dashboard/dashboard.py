import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

sort_bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
              "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
sort_day = ["Senin", "Selasa", "Rabu", "Kamis", "Jum'at", "Sabtu", "Ahad"]
def create_monthly_rental_df(df):
    result = df.groupby(by="mnth")[["cnt"]].sum()
    result = result.reindex(sort_bulan)
    result.rename(columns={
        "mnth": "Month",
        "cnt": "Count"
    }, inplace=True)
    return result
def create_weekly_rental_df(df):
    weekday_sum = df.groupby(["weekday"])[["cnt"]].sum().reindex(sort_day)
    return weekday_sum
def create_seasonly_rental_df(df):
    season_count = df.groupby(by="season")[["cnt"]].sum().sort_values(by="cnt", ascending=False)
    return season_count
def create_seasonly_avg_df(df):
    seasonal_avg = df.groupby('mnth')[['temp', 'hum', 'windspeed', 'cnt']].mean().reindex(sort_bulan)
    return seasonal_avg
def create_holiday_rental_df(df):
    holiday_count = df.groupby(['holiday'])[['cnt']].sum()
    return holiday_count
def create_working_rental_df(df):
    working_count = df.groupby(['workingday'])[['cnt']].sum()
    return working_count
def create_daily_rent(df):
    return df.groupby("dteday")[["casual","registered","cnt"]].sum().sort_index()

all_df = pd.read_csv("../data/all_data.csv")

all_df["dteday"] = pd.to_datetime(all_df["dteday"])

st.sidebar.title("Bycycle Rental")
st.sidebar.markdown("Shared bycycle rental data between 2011 to 2012")

with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Melbourne_City_Bikes.JPG/1200px-Melbourne_City_Bikes.JPG", width=300)

monthly_rental_df = create_monthly_rental_df(all_df)
weekly_rental_df = create_weekly_rental_df(all_df)
seasonly_rental_df = create_seasonly_rental_df(all_df)
seasonly_avg_df = create_seasonly_avg_df(all_df)
working_rental_df = create_working_rental_df(all_df)
holiday_rental_df = create_holiday_rental_df(all_df)
daily_rent = create_daily_rent(all_df)

st.header('Melbourne Bycycle Rental :^)')
st.subheader('Monthly rental')

with st.container():
    total_orders = monthly_rental_df.Count.sum()
    st.metric("Total rent", value=total_orders)

    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        monthly_rental_df.index,
        monthly_rental_df["Count"],
        marker='o',
        linewidth=2,
        color="#90CAF9"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=20, rotation=45)

    st.pyplot(fig)

st.subheader("Weekly Rental")
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    weekly_rental_df.index,
    weekly_rental_df["cnt"],
    marker='o',
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=20, rotation=45)
st.pyplot(fig)

# # ============================================================
st.subheader("Holiday and Workingday Rental")
col1, col2 = st.columns(2)
with col1:
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.pie(
        x=holiday_rental_df["cnt"],
        labels=holiday_rental_df.index,
        autopct='%1.2f%%',
        colors=('#93C572', '#E67F0D'),
        explode=(0, 0.1),
        textprops={'fontsize': 40}
    )
    ax.set_title("Number of Customer by Gender", loc="center", fontsize=50)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.pie(
        x=working_rental_df["cnt"],
        labels=working_rental_df.index,
        autopct='%1.2f%%',
        colors=('#E67F0D', '#93C572'),
        explode=(0.1, 0),
        textprops={'fontsize': 40}
    )
    ax.set_title("Number of Customer by Age", loc="center", fontsize=50)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

# ==================================
st.subheader("Weather and Rental Correlation")
weather_cols = ['temp', 'atemp', 'hum', 'windspeed', 'weathersit']
correlation = all_df[weather_cols + ['cnt']].corr()
column_names = {
    'temp': 'Temperature',
    'atemp': 'Temperature Feel',
    'hum': 'Humidity',
    'windspeed': 'Velocity',
    'weathersit': 'Weathersit',
    'cnt': 'Rent count'
}
correlation = correlation.rename(columns=column_names, index=column_names)

# =======================================
fig, ax = plt.subplots(figsize=(20, 10))
sns.heatmap(correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0, annot_kws={"size": 20})
ax.tick_params(axis='y', labelsize=20, rotation=45)
ax.tick_params(axis='x', labelsize=20)
st.pyplot(fig)

# =====================================
st.subheader("Effect of Temperature on Rental Amount")
fig, ax = plt.subplots(figsize=(20, 10))
sns.scatterplot(
    x='temp',
    y='cnt',
    data=all_df
)
ax.tick_params(axis='y', labelsize=30, rotation=45)
ax.tick_params(axis='x', labelsize=30)
ax.set_xlabel("Temperature", fontsize=30)
ax.set_ylabel("Count", fontsize=30)
st.pyplot(fig)
# w
st.caption('Copyright (c) github.com/uchihamadara37 2024')