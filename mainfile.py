from lib.lib import *
import pandas as pd

file_name = "Formula1_2023season_drivers.csv"

# Csv open
fantasy_dataframe = csv_open(file_name)

# fantasy_dataframe = pd.read_csv("Formula1_2023season_drivers.csv")

# Group data
grouped_fantasy_df = groupsorted_data(fantasy_dataframe)
print(grouped_fantasy_df)

# Print stats summary
descriptioncsv = summary_stat(grouped_fantasy_df)
print(descriptioncsv)

# Bar chart
bar_chart(grouped_fantasy_df)

# Scatterplot
scatterplot(grouped_fantasy_df)
