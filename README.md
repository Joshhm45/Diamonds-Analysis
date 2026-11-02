# Diamonds_Analysis Dataset: Exploratory Analysis

Assignment 01: exploring the structure, data quality and summary statistics of a diamonds dataset with Python and pandas.

Author: Joshua_Vanbawihumhim
Repository: https://github.com/Joshhm45/Diamonds-Analysis

## Project description

The dataset `diamonds.csv` contains 53,940 diamonds described by 10 columns:

| Column  | Description |
|-------- |-------------|
| carat   | Weight of the diamond |
| cut     | Cut quality (Fair, Good, Very Good, Premium, Ideal) |
| color   | Colour grade (D to J) |
| clarity | Clarity grade (I1 to IF) |
| depth   | Total depth percentage |
| table   | Width of the top of the diamond relative to its widest point |
| price   | Price in US dollars |
| x, y, z | Length, width and depth in mm |

The script diamond_analysis.py loads the data, checks its structure and quality, and computes summary statistics and shows charts that support the findings.
The findings are written in comments directly below the code that produced them.

## Project structure

```
Diamonds_Analysis/
├── diamond_analysis.py             # analysis  script, split into cells (# %%)
├── diamonds.csv       # dataset
├── requirements.txt   # Python packages needed
└── README.md          # this file
```

## Setup

You need Python 3.11 or newer (required by the pandas version in requirements.txt).

1. Open a terminal in the project folder.

2. Create a virtual environment:

   ```
   python3 -m venv .venv
   ```

3. Activate it:

   - macOS / Linux: `source .venv/bin/activate`
   - Windows: `.venv\Scripts\activate`

4. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

## How to run

The script is written in cells, so it is best run in VS Code:

1. Open the project folder in VS Code.
2. Install the Python extension if you don't have it yet.
3. Select the `.venv` interpreter (Command Palette, then "Python: Select Interpreter").
4. Open `diamond_analysis.py` and click **Run Cell** above each `# %%` block, or use **Run All Cells**.

   The output and the charts appear in the Interactive window.
   
   The file diamonds.csv must be in the same folder as `diamond_analysis.py`.

You can also run the whole file from the terminal with `python3 diamond_analysis.py`, but then
only `print(...)` output is shown, not the cell results.

## What The Analysis Contains

1. Structure: shape, columns, data types (head, info, shape, dtypes)
2. Summary Statistics: describe()
3. Data quality: duplicates, missing values, impossible values (zeros in x , y , z ), categories
4. Visualizations : 
    - Histogram of price
    - Scatter plot of carat vs. price
    - Box plot of x , y , and z
    - Bar chart of missing values per column

## Main findings

- The dataset has 53,940 rows and 10 columns (7 numeric, 3 text).
- About 5% of the values are missing in every column.
- `x`, `y` and `z` contain zeros, which are impossible sizes and are not found by `isnull()`.
- 57 rows are exact duplicates.
- price is skewed: the mean (3,935) is much higher than the median (2,407), because most diamonds are cheap and a few are very expensive.
- Heavier diamonds are more expensive (carat vs. price).
- y has a maximum of 58.9 mm, far above all other values, which is probably an error.
- The categories (`cut`, `color`, `clarity`) are clean, with no typos.

See the comments in `diamond_analysis.py` for the full explanation.
*The data was only analysed, not cleaned. The original diamonds.csv is not changed.*