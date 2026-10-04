import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Week1_Cleaned_Data_Source.xlsx", sheet_name="Cleaned_Data")
df["Date"] = pd.to_datetime(df["Date"])
df["CTR (%)"] = df["Clicks"] / df["Impressions"] * 100
df["Engagement Rate (%)"] = (df["Likes"]+df["Shares"]+df["Comments"]) / df["Impressions"] * 100
df["Conversion Rate (%)"] = df["Conversions"] / df["Clicks"] * 100
df["CPC (INR)"] = df["Ad Spend (INR)"] / df["Clicks"]
df["CPA (INR)"] = df["Ad Spend (INR)"] / df["Conversions"]

platform = df.groupby("Platform").agg(
    Impressions=("Impressions","sum"),
    Clicks=("Clicks","sum"),
    Conversions=("Conversions","sum"),
    Spend=("Ad Spend (INR)","sum")
).reset_index()
platform["CTR (%)"] = platform["Clicks"]/platform["Impressions"]*100
platform["Conversion Rate (%)"] = platform["Conversions"]/platform["Clicks"]*100
platform["CPC (INR)"] = platform["Spend"]/platform["Clicks"]
platform["CPA (INR)"] = platform["Spend"]/platform["Conversions"]

print(platform.sort_values("Conversions", ascending=False))
