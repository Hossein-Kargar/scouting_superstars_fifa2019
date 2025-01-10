"""
scouting_superstars_fifa2019.py

This script processes and visualizes FIFA 2019 player data, focusing on player wages and values.
It uses pandas for data manipulation, Seaborn for visualization, and Bokeh for interactive plots.

Author: Hossein Kargar
Date: 2023-10-25
"""

import pandas as pd
import seaborn as sns
from bokeh.plotting import figure, show
from bokeh.models import HoverTool

# Constants for multipliers
SUFFIX_MULTIPLIERS = {"K": 1_000, "M": 1_000_000, "B": 1_000_000_000}


# Helper function to convert string values to floats
def convert_to_float(x):
    """
    Convert a value to a float.

    This function attempts to convert a given value `x` to a float. If the input is
    already of type `float` or `int`, it is returned as is. If the input is a string,
    the function checks for specific suffixes defined in the global
    `SUFFIX_MULTIPLIERS` dictionary. If a matching suffix is found, it converts
    the numerical part of the string to a float and multiplies it by the corresponding
    multiplier. If no condition is met, it defaults to returning `0.0`.

    :param x: The input value to be converted to a float. It can be of type `float`,
        `int`, or `str`.
    :return: The converted float value. If conversion is not possible, it returns 0.0.
    :rtype: float
    """
    if isinstance(x, (float, int)):
        return x
    for suffix, multiplier in SUFFIX_MULTIPLIERS.items():
        if suffix in x:
            return float(x.replace(suffix, "")) * multiplier
    return 0.0


# Load and preprocess data
data_frame = pd.read_csv("data.csv")
df1 = pd.DataFrame(data_frame, columns=["Name", "Wage", "Value"])

# Convert wage and value columns
converted_wage = df1["Wage"].replace("[\€]", "", regex=True).apply(convert_to_float)
converted_value = df1["Value"].replace("[\€]", "", regex=True).apply(convert_to_float)
df1["Wage"], df1["Value"] = converted_wage, converted_value

# Calculate difference between value and wage
df1["difference"] = df1["Value"] - df1["Wage"]
df1.sort_values("difference", ascending=False, inplace=True)

# Visualize with Seaborn
sns.set_theme()
sns.scatterplot(x="Wage", y="Value", data=df1)


# Visualize with Bokeh
tooltips = HoverTool(
    tooltips=[
        ("index", "$index"),
        ("(Wage, Value)", "(@Wage, @Value)"),
        ("Name", "@Name"),
    ]
)
plot = figure(
    title="Soccer 2019",
    x_axis_label="Wage",
    y_axis_label="Value",
    width=700,
    height=700,
    tools=[tooltips],
)
plot.scatter("Wage", "Value", size=10, source=df1)
show(plot)
