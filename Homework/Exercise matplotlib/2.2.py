import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('C:\\Users\\19440\\Documents\\GitHub\\2023-Python-language-programming\\Homework\\Exercise matplotlib\\Iris.csv')
sns.scatterplot(x='petal_length',y='sepal_length',hue='species',style='species',s=90,data=data)
plt.show()
