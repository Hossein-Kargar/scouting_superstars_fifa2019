# Soccer Data Analysis and Visualization

---

## Overview

This project is a Python-based program that analyzes and visualizes soccer player data using **pandas**, **Seaborn**,
and **Bokeh**.
It processes data from a provided CSV file, cleans it, performs calculations, and generates both static and interactive
visualizations.

---

## Features

1. **Data Preprocessing**:
    - Converts player wages and market values from strings with currency symbols and suffixes (e.g., "€20K", "€1.5M")
      into numerical values.
    - Calculates a "difference" column that represents the gap between a player's market value and their wage.

2. **Data Analysis**:
    - Sorts players by the calculated wage-to-value difference to identify insights into underpaid/overpaid players.

3. **Visualization**:
    - Static scatter plot using **Seaborn**.
    - Interactive scatter plot using **Bokeh**, complete with hover functionality to display detailed information.

---

## Getting Started

### Prerequisites

Ensure you have Python 3.7 or later installed on your system along with the following libraries:

- **pandas**
- **seaborn**
- **bokeh**

Install these dependencies via pip:

```bash
pip install pandas seaborn bokeh
```

### Input Data

The program includes a sample CSV file, `data.csv`, located in the project's root directory. It contains the following
structure:

| Name     | Wage | Value |
|----------|------|-------|
| Player A | €50K | €2M   |
| Player B | €10K | €500K |

- **Name**: Name of the soccer player.
- **Wage**: Weekly wage, including currency symbol and suffix (e.g., "€50K").
- **Value**: Market value of the player, including currency symbol and suffix (e.g., "€2M").

You can use the provided file as a sample dataset or replace it with your own data by ensuring it matches the same
format.

---

## Usage

To run the program:

1. Ensure the provided `data.csv` file is in the root directory.
2. Execute the script:
   ```bash
   python scouting_superstars_fifa2019.py
   ```
3. The program will:
    - Load and preprocess the data from the `data.csv` file.
    - Generate a static scatter plot with Seaborn.
    - Open an interactive scatter plot in your browser using Bokeh.

---

## Output

1. **Seaborn Static Visualization**:
    - A scatter plot showing the relationship between players' wages and values.

2. **Bokeh Interactive Visualization**:
    - A dynamic scatter plot featuring hover functionality that displays player-specific information such as:
        - Name
        - Wage
        - Value

---

## Code Overview

1. **Constants**:
    - `SUFFIX_MULTIPLIERS`: Contains the conversion factors for numeric suffixes (`K`, `M`, `B`).

2. **Helper Functions**:
    - `convert_to_float(x)`: Converts string values like "€20K" into float values.

3. **Data Preprocessing**:
    - Cleans and converts columns (`Wage` and `Value`) into numerical formats.
    - Calculates the `difference` between `Value` and `Wage`.

4. **Visualization**:
    - **Seaborn**: Creates a static scatter plot of wages vs values.
    - **Bokeh**: Creates an interactive version of the plot with hover functionality.

---

## Example Visualizations

### Static Scatter Plot

The Seaborn plot shows the relationship between wages and values for all players in the dataset.

### Interactive Bokeh Plot

This downloadable HTML visualization includes hover tooltips, showing:

- Player name
- Wage
- Market value

---

## Modifications

You can easily modify the program to:

- Add new columns for analysis (e.g., wage-to-value ratio).
- Change visualization styles (e.g., color and marker size).
- Handle different datasets by parameterizing the input file name.

---

## Author

**Hossein Kargar**  
Created on: **2025-01-10**

---

## License

This project is open-source and distributed under the MIT License. Feel free to modify and adapt it to your needs!

---

Happy analyzing! If you have any questions or suggestions, feel free to reach out.