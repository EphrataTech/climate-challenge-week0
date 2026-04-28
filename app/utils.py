import pandas as pd

def load_data():
    ethiopia = pd.read_csv("data/ethiopia_clean.csv")
    kenya = pd.read_csv("data/kenya_clean.csv")
    tanzania = pd.read_csv("data/tanzania_clean.csv")
    sudan = pd.read_csv("data/sudan_clean.csv")
    nigeria = pd.read_csv("data/nigeria_clean.csv")

    df = pd.concat([ethiopia, kenya, tanzania, sudan, nigeria])
    return df

def filter_data(df, countries, year_range):
    df = df[df["Country"].isin(countries)]
    df["Year"] = pd.to_datetime(df["Date"]).dt.year
    df = df[(df["Year"] >= year_range[0]) & (df["Year"] <= year_range[1])]
    return df