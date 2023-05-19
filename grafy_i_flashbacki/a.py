import pandas as pd
import numpy as np
from scipy import stats
# Create a sample DataFrame with 10 additional NaN values
df = pd.DataFrame({'A': [1, 2,2, 3, 4, 2, 3, 4, 2, 4, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]})

# Add 10 NaN values to column 'A'

# Get the mode of column 'A' excluding NaN values
mode = df['A'].mode(dropna=True)[0]
df['A'] = df['A'].fillna(mode)

print(df)