import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('C:\\Users\\19440\\Documents\\GitHub\\2023-Python-language-programming\\Homework\\Exercise matplotlib\\Iris.csv')
sns.barplot(x='species', y='petal_length', hue = 'species',data=data)
plt.show()