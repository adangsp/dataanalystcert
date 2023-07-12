import pandas as pd

# Read the data from "fcc-forum-pageviews.csv" and set the index to the date column
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Calculate the boundaries for filtering the data
bottom_percentile = df["value"].quantile(0.025)
top_percentile = df["value"].quantile(0.975)

# Filter out the days outside the boundaries
df_cleaned = df[(df["value"] >= bottom_percentile) & (df["value"] <= top_percentile)]

import matplotlib.pyplot as plt

def draw_line_plot():
    # Create a line chart using Matplotlib
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df_cleaned.index, df_cleaned["value"], color="r")
    
    # Set the title and labels for the chart
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save the figure
    plt.savefig("line_plot.png")

    # Show the chart
    plt.show()

def draw_bar_plot():
    # Create a new DataFrame by grouping the data by year and month, and calculating the average page views
    df_bar = df_cleaned.groupby([df_cleaned.index.year, df_cleaned.index.month])["value"].mean().unstack()
    
    # Create the bar chart using Matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))
    df_bar.plot(kind="bar", ax=ax)
    
    # Set the title and labels for the chart
    ax.set_title("Average Daily Page Views for Each Month (Grouped by Year)")
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title="Months")
    
    # Save the figure
    plt.savefig("bar_plot.png")

    # Show the chart
    plt.show()
