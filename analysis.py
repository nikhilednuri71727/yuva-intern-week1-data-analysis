import pandas as pd

df = pd.read_excel("Yuva_Week1_Raw_Practice_Data.xlsx", sheet_name="Raw_Data")

# Standardize text fields
df["Campaign Name"] = df["Campaign Name"].astype("string").str.strip().str.replace(r"\s+", " ", regex=True)
df["Platform"] = df["Platform"].astype("string").str.strip().str.title()

# Standardize dates
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Convert numeric columns
numeric = ["Impressions","Clicks","Likes","Shares","Comments","Ad Spend (INR)","Conversions"]
for col in numeric:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Fill selected missing numeric values with medians
for col in ["Clicks","Likes","Ad Spend (INR)","Conversions"]:
    df[col] = df[col].fillna(df[col].median())

# Remove exact duplicates
df = df.drop_duplicates().reset_index(drop=True)

# Derived KPIs
df["CTR (%)"] = df["Clicks"] / df["Impressions"] * 100
df["Engagement Rate (%)"] = (df["Likes"] + df["Shares"] + df["Comments"]) / df["Impressions"] * 100
df["Conversion Rate (%)"] = df["Conversions"] / df["Clicks"] * 100
df["CPC (INR)"] = df["Ad Spend (INR)"] / df["Clicks"]
df["CPA (INR)"] = df["Ad Spend (INR)"] / df["Conversions"]

df.to_excel("Yuva_Week1_Cleaned_Data_From_Code.xlsx", index=False)
print("Cleaned dataset created successfully.")
