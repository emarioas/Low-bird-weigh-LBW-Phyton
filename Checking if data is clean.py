import pandas as pd


df = pd.read_csv(r'C:\Users\Naqiya\Desktop\Python Project\project_data-1.csv')


# try to get low row by your self from btw

df.drop (['id'],axis=1,inplace=True)

print (df.isnull())
print (df.isnull().sum())


