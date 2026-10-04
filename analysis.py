import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# Recreate/load the workbook and model in the full report workflow.
wb = pd.ExcelFile("Yuva_Week5_Predictive_Modeling.xlsx")
print(wb.sheet_names)
