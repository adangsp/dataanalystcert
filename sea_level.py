import pandas as pd

# Read the data from "epa-sea-level.csv"
df = pd.read_csv("epa-sea-level.csv")

import matplotlib.pyplot as plt

# Create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis
plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

# Set the labels and title for the plot
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.title("Rise in Sea Level")

import scipy.stats as stats

# Get the slope, y-intercept, and other regression values using linregress
slope, intercept, r_value, p_value, std_err = stats.linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

# Create a range of years from 1880 to 2050
years = range(1880, 2051)

# Create the line of best fit using the slope and y-intercept
line = slope * years + intercept

# Plot the line of best fit
plt.plot(years, line, color="r", label="Line of Best Fit")

# Show the legend for the line of best fit
plt.legend()

# Filter the data from year 2000 through the most recent year
recent_years_df = df[df["Year"] >= 2000]

# Get the slope, y-intercept, and other regression values for the recent years
slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = stats.linregress(
    recent_years_df["Year"], recent_years_df["CSIRO Adjusted Sea Level"]
)

# Create the line of best fit for the recent years using the slope and y-intercept
line_recent = slope_recent * years + intercept_recent

# Plot the line of best fit for the recent years
plt.plot(years, line_recent, color="g", label="Line of Best Fit (2000-Present)")

# Show the legend for the line of best fit for the recent years
plt.legend()

# Set the x label, y label, and title
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.title("Rise in Sea Level")

# Save the figure
plt.savefig("sea_level_rise.png")

# Show the plot
plt.show()
