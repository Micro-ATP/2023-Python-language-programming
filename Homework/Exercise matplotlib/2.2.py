import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('C:\\Users\\19440\\Documents\\GitHub\\2023-Python-language-programming\\Homework\\Exercise matplotlib\\Iris.csv')
sns.scatterplot(x='PetalLengthCm',y='SepalLengthCm',hue='Species',style='Species',s=90,data=data)
plt.show()
