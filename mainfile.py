import pandas as pd
import matplotlib.pyplot as plt

file_name = "Formula1_2023season_drivers.csv"


# Read CSV
def csv_open(file_path):
    data = pd.read_csv(file_path)
    return data


def groupsorted_data(dataframe):
    # Group data by team and FPTS
    grouped = pd.DataFrame(dataframe.groupby("Team")["Points"].sum()).reset_index(
        drop=False
    )

    # Sort the new dataframe in ascending order
    grouped = grouped.sort_values(by="Points", ascending=True)
    return grouped


def summary_stat(dataframe):
    # Get summary statistics
    description = dataframe.describe()
    return description


# Creating bar chart
def bar_chart(dataframe):
    # Setting x to nfl team column and y to fantasy points column
    x = dataframe["Team"]
    y = dataframe["Points"]

    # Plotting the bar chart
    plt.bar(x, y, width=0.8, color="red")

    # Rotating all x-axis labels vertically to fit on the chart
    plt.xticks(range(len(x)), x, rotation="vertical")

    # Labeling the chart
    plt.title("F1 2023 Season Career Driver Points")
    plt.xlabel("Team")
    plt.ylabel("Total Career Team Driver Points")

    # Show the chart
    plt.show()


# Create Scatterplot
def scatterplot(dataframe):
    # Setting x to nfl team column and y to fantasy points column
    x = dataframe["Team"]
    y = dataframe["Career Points"]

    # Plotting the scatter chart
    plt.scatter(x, y, color="red")

    # Rotating all x-axis labels vertically to fit on the chart
    plt.xticks(range(len(x)), x, rotation="vertical")

    # Labeling the chart
    plt.title("F1 2023 Season Career Driver Points")
    plt.xlabel("Team")
    plt.ylabel("Total Career Team Driver Points")

    # Show the chart
    plt.show()


# Csv open
fantasy_dataframe = csv_open(file_name)

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
