import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt  


df = pd.read_excel('dataset.xlsx')

for column_name in list(df):
    q75, q25 = np.percentile(df.loc[:, column_name], [75, 25])
    avg = q75 - q25

    max = q75 + avg * 1.5
    min = q25 - avg * 1.5

    df.loc[df[column_name] > max, column_name] = np.nan
    df.loc[df[column_name] < min, column_name] = np.nan

    df = df.dropna(axis=0)

sns.pairplot(df)
plt.show()
