import pandas as pd
import streamlit as st
import plotly.express as px

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("owid-covid-data (1).csv", parse_dates=["date"])
    df = df[df['iso_code'].str.len() == 3]  # Keep only countries (3-letter ISO)
    return df

df = load_data()

# Sidebar filters
st.sidebar.title("Filter Data")
countries = df['location'].unique()
selected_countries = st.sidebar.multiselect("Select countries", sorted(countries), default=['Kenya', 'United States', 'India'])

min_date = df['date'].min()
max_date = df['date'].max()
date_range = st.sidebar.date_input("Select date range", [min_date, max_date], min_value=min_date, max_value=max_date)

# Filter data
start_date, end_date = date_range
filtered_df = df[
    (df['location'].isin(selected_countries)) &
    (df['date'] >= pd.to_datetime(start_date)) &
    (df['date'] <= pd.to_datetime(end_date))
]

# Sidebar metrics
st.sidebar.markdown("### 📌 Key Stats (Selected Data)")

latest_filtered = filtered_df.sort_values('date').groupby('location').tail(1)

total_vax = latest_filtered['total_vaccinations'].sum()
new_cases = latest_filtered['new_cases'].sum()
new_deaths = latest_filtered['new_deaths'].sum()

st.sidebar.metric("💉 Total Vaccinations", f"{int(total_vax):,}")
st.sidebar.metric("🆕 New Cases (latest)", f"{int(new_cases):,}")
st.sidebar.metric("⚰️ New Deaths (latest)", f"{int(new_deaths):,}")

# Title
st.title("🌍 COVID-19 Global Dashboard")

# Total cases over time
st.subheader("📈 Total Cases Over Time")
fig_cases = px.line(filtered_df, x='date', y='total_cases', color='location', title="Total COVID-19 Cases")
st.plotly_chart(fig_cases)

# Total deaths over time
st.subheader("💀 Total Deaths Over Time")
fig_deaths = px.line(filtered_df, x='date', y='total_deaths', color='location', title="Total COVID-19 Deaths")
st.plotly_chart(fig_deaths)

# Vaccinations over time
st.subheader("💉 Total Vaccinations Over Time")
fig_vax = px.line(filtered_df, x='date', y='total_vaccinations', color='location', title="Total COVID-19 Vaccinations")
st.plotly_chart(fig_vax)

# Death rate (total_deaths / total_cases)
st.subheader("⚖️ Death Rate (%)")
filtered_df['death_rate'] = (filtered_df['total_deaths'] / filtered_df['total_cases']) * 100
fig_rate = px.line(filtered_df, x='date', y='death_rate', color='location', title="COVID-19 Death Rate (%)")
st.plotly_chart(fig_rate)

st.subheader("🗺️ Global COVID-19 Case Map (Latest Date)")

# Get latest data per country
latest_df = df.sort_values('date').groupby('location').tail(1)

# Only countries (with valid ISO codes)
latest_df = latest_df[latest_df['iso_code'].str.len() == 3]

# Plot choropleth
fig_choropleth = px.choropleth(
    latest_df,
    locations="iso_code",
    color="total_cases",
    hover_name="location",
    color_continuous_scale="Reds",
    title="Total COVID-19 Cases by Country",
    projection="natural earth"
)

st.plotly_chart(fig_choropleth)

st.subheader("📤 Export Filtered Data")

csv = filtered_df.to_csv(index=False)
st.download_button(
    label="Download as CSV",
    data=csv,
    file_name='filtered_covid_data.csv',
    mime='text/csv'
)


