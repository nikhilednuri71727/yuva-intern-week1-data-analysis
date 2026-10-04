# Yuva Intern – Week 1: Social Media Campaign Data Collection & Cleaning

**Candidate:** Nikhil Ednuri  
**Role:** Junior Data Analyst – Digital Marketing & Advertising

## Project objective
Prepare social-media campaign data for analysis by documenting data collection, quality checks, cleaning, and KPI preparation.

## Public reference source
Kaggle – Sales Conversion Optimization:
https://www.kaggle.com/datasets/loveall/clicks-conversion-tracking

A public reference analysis reports that the dataset contains 1,143 observations and 11 variables and identifies 204 records where Clicks = 0 while Total_Conversion > 0; those records were removed in that reference workflow, leaving 939 records.

## Files
- `Yuva_Intern_Week1_Report.docx` – internship submission report
- `Yuva_Week1_Raw_Practice_Data.xlsx` – 100-record practice dataset with intentional data-quality issues
- `Yuva_Week1_Cleaned_Data.xlsx` – cleaned practice dataset with KPI fields
- `analysis.py` – reproducible Python cleaning script
- `cleaning_impact.png` – data-quality visualization
- `field_groups.png` – field-role visualization

## Cleaning performed
- Trimmed and standardized text categories
- Normalized dates
- Converted numeric fields
- Imputed selected missing numeric values using medians
- Removed exact duplicate rows
- Added CTR, engagement rate, conversion rate, CPC and CPA

## Important transparency note
The 100-record working dataset is a practice extract created to demonstrate the cleaning workflow. It is not represented as a raw export from the Kaggle source.
