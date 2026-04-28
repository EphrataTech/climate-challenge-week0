import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_data, filter_data

st.set_page_config(page_title="Climate Dashboard", layout="wide")

st.title("🌍 Climate Insights Dashboard (Africa)")

# ---------------------------
# LOAD DATA
# ---------------------------
df = load_data()

df["Year"] = pd.to_datetime(df["Date"]).dt.year

# ---------------------------
# SIDEBAR CONTROLS
# ---------------------------
st.sidebar.header("Filters")

countries = st.sidebar.multiselect(
    "Select Countries",
    options=df["Country"].unique(),
    default=df["Country"].unique()
)

year_range = st.sidebar.slider(
    "Select Year Range",
    int(df["Year"].min()),
    int(df["Year"].max()),
    (2015, 2026)
)

variable = st.sidebar.selectbox(
    "Select Variable",
    ["T2M", "PRECTOTCORR", "RH2M"]
)

# ---------------------------
# FILTER DATA
# ---------------------------
filtered_df = filter_data(df, countries, year_range)

# ---------------------------
# TEMPERATURE TREND
# ---------------------------
st.subheader("📈 Temperature Trend")

temp = filtered_df.groupby(["Country", "Month"])["T2M"].mean().reset_index()

fig, ax = plt.subplots()

for country in temp["Country"].unique():
    data = temp[temp["Country"] == country]
    ax.plot(data["Month"], data["T2M"], label=country)

ax.set_title("Monthly Temperature Trend")
ax.set_xlabel("Month")
ax.set_ylabel("Temperature")
ax.legend()

st.pyplot(fig)

# ---------------------------
# PRECIPITATION BOXPLOT
# ---------------------------
st.subheader("🌧️ Precipitation Distribution")

fig2, ax2 = plt.subplots()
sns.boxplot(x="Country", y="PRECTOTCORR", data=filtered_df, ax=ax2)

ax2.set_title("Precipitation Variability")

st.pyplot(fig2)

# ---------------------------
# VARIABLE DISTRIBUTION
# ---------------------------
st.subheader("📊 Variable Distribution")

fig3, ax3 = plt.subplots()
sns.histplot(filtered_df[variable], kde=True, ax=ax3)

ax3.set_title(f"{variable} Distribution")

st.pyplot(fig3)