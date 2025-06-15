# covid_analysis.py
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the global COVID-19 data CSV
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"

print("Loading data...")
df = pd.read_csv(url, usecols=[
    "location", "date", "new_cases_per_million", "total_cases_per_million"
], parse_dates=["date"])
print("Data loaded successfully.")

# 2. Select a few countries
countries = ["India", "United States", "Brazil", "United Kingdom", "South Africa"]

df2 = df[df["location"].isin(countries)]

# 3. Plot daily new cases per million
plt.figure(figsize=(12, 6))
for country in countries:
    subset = df2[df2["location"] == country]
    plt.plot(subset["date"], subset["new_cases_per_million"], label=country)

plt.xlabel("Date")
plt.ylabel("New Cases per Million")
plt.title("Daily New COVID‑19 Cases per Million (Global)")
plt.legend()
plt.tight_layout()
# 4. Bar chart: Total cases per million (latest date)
latest = df2[df2["date"] == df2["date"].max()]
latest_totals = latest.groupby("location")["total_cases_per_million"].max().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
latest_totals.plot(kind="bar", color="teal")
plt.ylabel("Total Cases per Million")
plt.title("Total COVID‑19 Cases per Million (Latest Data)")
plt.tight_layout()
plt.show()

# 5. Save filtered data to CSV
df2.to_csv("covid_selected_countries.csv", index=False)
print("Filtered data saved as CSV.")
