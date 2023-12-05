import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('Homework\\Exercise matplotlib\\Iris.csv')
sns.boxplot(x='Species',y='SepalLengthCm',data=data,hue='Species')
plt.show()
