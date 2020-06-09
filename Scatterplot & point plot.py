import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import classification_report
import seaborn as sns

data = pd.read_csv(r'C:\Users\Naqiya\Desktop\Python Project\project_data-1.csv')

x = data['age']
y = data['bwt']

plt.scatter(x , y , edgecolors='r')
plt.xlabel('Mothers age')
plt.ylabel('birth weight')
plt.title('Correlation of mothers age and birth weight')
plt.show()


sns.set(style="darkgrid")
sns.pointplot(x="ptl",y=y ,data=data)
plt.show()
sns.pointplot(x="race",y=y , data=data,)
plt.show()





