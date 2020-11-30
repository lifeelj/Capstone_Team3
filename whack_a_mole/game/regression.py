from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

filepath = "C:/Users/KKW/Desktop/캡스톤/Fittsdata.csv"
df = pd.read_csv(filepath, sep=",")
fittstask = df[0:755]
fitts = df[755:]

fittstask_1 = fittstask[(fittstask['Transform'] == 1) | (
    fittstask['Transform'] == 2) | (fittstask['Transform'] == 3)]
fittstask_1['Width'] = 40
fittstask_2 = fittstask[(fittstask['Transform'] == 4) | (
    fittstask['Transform'] == 5) | (fittstask['Transform'] == 6)]
fittstask_2['Width'] = 60

fitts_1 = fitts[(fitts['Transform'] == 1) | (
    fitts['Transform'] == 2) | (fitts['Transform'] == 3)]
fitts_1['Width'] = 50
fitts_2 = fitts[(fitts['Transform'] == 4) | (
    fitts['Transform'] == 5) | (fitts['Transform'] == 6)]
fitts_2['Width'] = 60

df = pd.concat([fittstask_1, fittstask_2, fitts_1, fitts_2])
df['ID'] = np.log2((2*df['Distance'])/df['Width'])
df = df[df['ID'] > 1.5]
df = df[df['Time'] < 3000]

df = df.groupby(['Transform', 'Email']).mean()
df = df.reset_index()
df = df[['Age', 'ID', 'Time']]
df = df[(df['ID'] > 2.0) & (df['ID'] < 4.1)]

df_10to20 = df[df['Age'] < 30]
df_30to40 = df[(df['Age'] >= 30) & (df['Age'] < 50)]
df_50to60 = df[df['Age'] >= 50]

df_10to20 = df_10to20.drop('Age', axis=1)
df_30to40 = df_30to40.drop('Age', axis=1)
df_50to60 = df_50to60.drop('Age', axis=1)

X_10to20 = df_10to20[['ID']]
Y_10to20 = df_10to20[['Time']]
X_30to40 = df_30to40[['ID']]
Y_30to40 = df_30to40[['Time']]
X_50to60 = df_50to60[['ID']]
Y_50to60 = df_50to60[['Time']]

LR_10to20 = LinearRegression()
LR_10to20.fit(X_10to20, Y_10to20)
LR_10to20.coef_
LR_10to20.intercept_
LR_30to40 = LinearRegression()
LR_30to40.fit(X_30to40, Y_30to40)
LR_30to40.coef_
LR_30to40.intercept_
LR_50to60 = LinearRegression()
LR_50to60.fit(X_50to60, Y_50to60)
LR_50to60.coef_
LR_50to60.intercept_

g = sns.regplot(x='ID', y='Time', data=df_10to20)
g = sns.regplot(x='ID', y='Time', data=df_30to40)
g = sns.regplot(x='ID', y='Time', data=df_50to60)

plt.scatter(X_10to20, Y_10to20)
plt.scatter(X_30to40, Y_30to40)
plt.scatter(X_50to60, Y_50to60)
