#%%
import pandas as pd
#%%
import matplotlib.pyplot as plt 
# %%
df_diamond = pd.read_csv('diamonds.csv')
#%%
df_diamond.head()
# The first rows already show `NaN` values in price column.
# %%
df_diamond.info()
# 7 columns are numeric (carat, depth, table, price, x, y, z) and 3 are string (cut, color, clarity).
# %%
df_diamond.shape
# - The dataset has 53,940 rows and 10 columns.
# %%
df_diamond.columns
# %%
df_diamond.dtypes
# all types are correct (numbers are float64, categories are text).
# %%
df_diamond.describe()
#The mean of price is much higher than the median
# 'x','y' and 'z' have minimum of 0, which is impossible.
# there is too much gap between the max of 'y' with other value which can be error. 
#%%
df_diamond['price'].plot(kind='hist')
plt.title('Distribution of price')
plt.xlabel('Price')
plt.show()
#We can see that most diamonds are cheap which is the reason that the mean is higher than median.
#%%
df_diamond.plot(kind='scatter', x='carat', y='price')
plt.title('Carat vs. price')
plt.show()
#This shows that heavier diamonds are more expensive.
#%%
df_diamond.boxplot(column=['x', 'y', 'z'])
plt.title('Size of the diamonds (mm)')
plt.show()
#Here we can see 'y' has far above point than all the others which is probably an error.
# %%
df_diamond.duplicated().sum()
# 57 rows are exact duplicates. 
# %%
df_diamond.isnull().sum().plot(kind='bar')
plt.title('Missing values per column')
plt.ylabel('Number of missing values')
plt.show()
# Every column has  missing values about 5%.
# They are spread evenly over all columns, including `price`, so they look random.
# %%
(df_diamond[['x', 'y', 'z']] == 0).sum()
# `x` has 7 zeros, `y` has 6 and `z` has 18. A diamond cannot have a size of 0.
# `isnull()` does not detect these, so they are hidden errors.
# %%
df_diamond[(df_diamond['x'] == 0) | (df_diamond['y'] == 0) | (df_diamond['z'] == 0)]
# These rows still have a carat weight and a price, so the zeros are probably missing
# measurements coded as 0. Rows 49556 and 49557 are also duplicates of each other.
# %%
df_diamond['cut'].unique()
# %%
df_diamond['color'].unique()
# %%
df_diamond['clarity'].unique()
# The categories are clean: `cut` has 5 levels, `color` runs from D to J and `clarity` from I1 to IF.
# There are no typos or inconsistent spellings. The only issue is `nan`.


## SUMMARY ##
# 1. About 5% of the values are missing in every column.
# 2. Zeros in `x`, `y` and `z` are hidden errors.
# 3. There are 57 duplicate rows.
# 4. The categories are clean, so the problems are in the numeric columns.
# 5. `price` is skewed: the mean is much higher than the median.
# 6. `y` has a very large outlier (58.9), which is probably an error.
# 7. Heavier diamonds are more expensive.