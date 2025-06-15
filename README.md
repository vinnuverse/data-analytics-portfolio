# COVID-19 Global Trends Analysis (Python)

This project analyzes COVID-19 trends across 5 countries using the Our World in Data dataset.

## 🔍 Objective
- Analyze daily new COVID-19 cases per million.
- Compare total cases per million by country.
- Save the filtered dataset for further use.

## 📁 Data Source
- https://covid.ourworldindata.org/data/owid-covid-data.csv

## 📊 Tools Used
- Python
- Pandas
- Matplotlib

## 📈 Output
- Line chart of daily new cases per million (India, USA, Brazil, UK, South Africa)
- Bar chart of total cases per million (latest date)
- Exported CSV: `covid_selected_countries.csv`

## 🚀 How to Run

```bash
pip install pandas matplotlib
python3 covid_analysis.py
