import numpy as np
import pandas as pd
from sklearn import model_selection
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier


df = pd.read_csv(r'C:\Users\Naqiya\Desktop\Python Project\project_data-1.csv')

x = df.drop(['low','bwt','id'],axis=1)
y = df.iloc[:,1].values

X_train, X_test, Y_train, Y_test, = train_test_split(x,y, test_size = 0.3, random_state = 1)


logmod = LogisticRegression(solver = 'liblinear')
print (logmod.fit(X_train,Y_train))

predictions = logmod.predict(X_test)

print (classification_report(Y_test,predictions))

from sklearn.metrics import confusion_matrix

print (confusion_matrix(Y_test,predictions))

from sklearn.metrics import accuracy_score

print (accuracy_score (Y_test,predictions))


