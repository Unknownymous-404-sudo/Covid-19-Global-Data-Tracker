
# 🌍 COVID-19 Data Analysis and Dashboard

This project provides an interactive and insightful look into global COVID-19 trends using real-world data from **Our World in Data**. It includes:

- A data analysis notebook (`covid-19 Data.ipynb`) with visualizations and insights.
- An interactive Streamlit dashboard (`covid_dashboard.py`) for exploring cases, deaths, and vaccinations across countries and time.

---

## 📁 Project Structure

```
├── covid-19 Data.ipynb         # Jupyter notebook with EDA and visualizations
├── covid_dashboard.py          # Streamlit dashboard application
├── owid-covid-data.csv         # COVID-19 dataset from Our World in Data
├── README.md                   # Project documentation
```

---

## 📊 Features

### `covid-19 Data.ipynb`

- Data loading and cleaning (handling nulls, date parsing, etc.)
- Time-series visualizations:
  - Total and new cases
  - Deaths and death rate
  - Vaccination rollout
- Country-level comparison (e.g., Kenya, USA, India)
- Correlation analysis (optional heatmap)
- Geospatial mapping using Plotly
- Markdown insights and takeaways

---

### `covid_dashboard.py` (Streamlit App)

- 🧭 **Interactive Filters**:
  - Country multi-select
  - Date range slider
- 📈 **Visuals**:
  - Line charts for total cases, deaths, vaccinations, and death rate
  - Choropleth map of global case distribution
- 📌 **Sidebar Metrics**:
  - Total vaccinations
  - New cases and deaths (latest)
- 📤 **Export**:
  - Download filtered dataset as CSV

---

## 📦 Installation & Setup

### Requirements

```bash
pip install pandas streamlit plotly altair
```

### Run Streamlit App

```bash
streamlit run covid_dashboard.py
```

---

## 📂 Data Source

- [Our World in Data – COVID-19 Dataset](https://github.com/owid/covid-19-data/tree/master/public/data)

> **Note**: Make sure `owid-covid-data.csv` is placed in the project directory.

---

## 📌 Sample Insights

- India had a steep rise in total cases during 2021.
- Kenya’s vaccination rollout lagged behind other major countries early on.
- The death rate (% deaths over cases) varied significantly by region and time.
- Global vaccination efforts picked up rapidly in mid-2021.

---

## 🚀 Future Enhancements

- Add per capita metrics (cases per 100k)
- Enable vaccination comparison as % of population
- Add multi-page navigation in Streamlit (with `st.tabs()` or `st.page`)
- Deploy on Streamlit Cloud for public access

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

- Data by [Our World in Data](https://ourworldindata.org/)
- Visualization tools: Streamlit, Plotly, Seaborn, Matplotlib
