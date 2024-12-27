import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt  
import plotly.express as px

df = pd.read_excel('dataset.xlsx')

correlation_matrix = sns.heatmap(df.corr(), annot=True)
correlation_matrix.set(title="Correlation Matrix")
plt.show()

df.boxplot(grid=False)
plt.show()

sns.pairplot(df)
plt.show()

column_names = list(df)
fig = px.parallel_coordinates(
    title="Parallel Coordinate Plot",
    data_frame=df,
    dimensions=column_names,
    color=column_names[-1]
)
fig.show()
