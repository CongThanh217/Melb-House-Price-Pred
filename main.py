import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("melb_data.csv")

report = ProfileReport(df, title="melb_house_data")

report.to_file("melb_data.html")
