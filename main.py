import numpy as np
import pandas as pd
from sklearn.ensemble import ExtraTreesRegressor
from ydata_profiling import ProfileReport
from sklearn.impute import KNNImputer
from sklearn.experimental import enable_iterative_imputer
from fancyimpute import IterativeImputer
from missforest.missforest import MissForest


df = pd.read_csv("melb_data.csv")
# Parsing the Address column (get name of street)
df["Address"] = df["Address"].apply(lambda x: x.split(" ")[1])

# Get the year of Date
df["Date"] = df["Date"].apply(lambda x: x.split("/")[2])

# Handle nan in CouncilArea column
df['CouncilArea'].fillna('Unknown', inplace=True)

# Drop nan rows
df = df.dropna(axis=0)
df["Suburb"].value_counts()
df.to_csv("Data_clean.csv")
# BuildingArea
# YearBuilt
# CouncilArea

