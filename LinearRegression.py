from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
from sklearn.metrics import r2_score

filepath = "C:/Users/KKW/Desktop/캡스톤/Fittsdata.csv"
df = pd.read_csv(filepath, sep=",")
fittstask = df[0:755]
fitts = df[755:]

fittstask_1 = fittstask[(fittstask['Transform'] == 1) | (fittstask['Transform'] == 2) | (fittstask['Transform'] == 3)]
fittstask_1['Width'] = 40
fittstask_2 = fittstask[(fittstask['Transform'] == 4) | (fittstask['Transform'] == 5) | (fittstask['Transform'] == 6)]
fittstask_2['Width'] = 60

fitts_1 = fitts[(fitts['Transform'] == 1) | (fitts['Transform'] == 2) | (fitts['Transform'] == 3)]
fitts_1['Width'] = 50
fitts_2 = fitts[(fitts['Transform'] == 4) | (fitts['Transform'] == 5) | (fitts['Transform'] == 6)]
fitts_2['Width'] = 60

fittstask = pd.concat([fittstask_1, fittstask_2])
fitts = pd.concat([fitts_1, fitts_2])

fittstask['ID'] = np.log2((2*fittstask['Distance'])/fittstask['Width'])
fitts['ID'] = np.log2((2*fitts['Distance'])/fitts['Width'])

fittstask = fittstask[fittstask['ID'] > 1.5]
fitts = fitts[fitts['ID'] > 1.5]
fittstask = fittstask[fittstask['Time'] < 3000]
fitts = fitts[fitts['Time'] < 3000]

fittstask = fittstask.groupby(['Transform', 'Email']).mean()
# fittstask = fittstask.groupby(['Transform']).mean() # Transform별 평균을 구할 때 사용
fittstask = fittstask.reset_index()
fittstask = fittstask[['Age', 'ID', 'Time', 'Transform', 'Email']]
fitts = fitts.groupby(['Transform', 'Email']).mean()
# fitts = fitts.groupby(['Transform']).mean()
fitts = fitts.reset_index()
fitts = fitts[['Age', 'ID', 'Time', 'Transform', 'Email']]
# fitts = fitts.drop([0])

fitts = fitts.drop([63, 117, 166, 265, 115, 164, 214, 263, 111, 260, 296, 252, 246, 231, 61])

df1 = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
df4 = pd.DataFrame()
df5 = pd.DataFrame()
df6 = pd.DataFrame()
df11 = pd.DataFrame()
df22 = pd.DataFrame()
df33 = pd.DataFrame()
df44 = pd.DataFrame()
df55 = pd.DataFrame()
df66 = pd.DataFrame()

fit = [df1, df2, df3, df4, df5, df6]
fitt = [df11, df22, df33, df44, df55, df66]

for i in range(6):
  fit[i] = fittstask[fittstask['Transform'] == i+1]
  fitt[i] = fitts[fitts['Transform'] == i+1]
  
  if(i == 0):
      fit[i]['ID'] = 3.32
      fitt[i]['ID'] = 3
  if(i == 1):
      fit[i]['ID'] = 3.90
      fitt[i]['ID'] = 3.58
  elif(i == 2):
      fit[i]['ID'] = 4.32
      fitt[i]['ID'] = 4
  elif(i == 3):
      fit[i]['ID'] = 2.73
      fitt[i]['ID'] = 2.73
  elif(i == 4):
      fit[i]['ID'] = 3.32
      fitt[i]['ID'] = 3.32
  else:
      fit[i]['ID'] = 3.73
      fitt[i]['ID'] = 3.73
 
"""  
  if(i == 0):
      fit[i]['ID'] = 3.32
      fitt[i]['ID'] = 3
  elif(i == 1):
      fit[i]['ID'] = 3.90
      fitt[i]['ID'] = 3.58
  elif(i == 2):
      fit[i]['ID'] = 4.32
      fitt[i]['ID'] = 4
  elif(i == 3):
      fit[i]['ID'] = 2.73
      fitt[i]['ID'] = 2.73
  elif(i == 4):
      fit[i]['ID'] = 3.32
      fitt[i]['ID'] = 3.32
  else:
      fit[i]['ID'] = 3.73
      fitt[i]['ID'] = 3.73
"""      
df = pd.concat([fit[1], fitt[1], fit[2], fitt[2],fit[3], fitt[3],fit[4], fitt[4],fit[5], fitt[5]])

# fitts만
"""
for i in range(6):
  fitt[i] = fitts[fitts['Transform'] == i+1]
  
  if(i == 0):
      fitt[i]['ID'] = 3
  elif(i == 1):
      fitt[i]['ID'] = 3.58
  elif(i == 2):
      fitt[i]['ID'] = 4
  elif(i == 3):
      fitt[i]['ID'] = 2.73
  elif(i == 4):
      fitt[i]['ID'] = 3.32
  else:
      fitt[i]['ID'] = 3.73
      
df = pd.concat([fitt[0], fitt[1], fitt[2], fitt[3], fitt[4], fitt[5]])
"""

df_10to20 = df[df['Age'] < 30]
df_30to40 = df[(df['Age'] >= 30) & (df['Age'] < 50)]
df_50to60 = df[df['Age'] >= 50]

df_10to20.describe()
df_30to40.describe()
df_50to60.describe()

df_10to20 = df_10to20.drop('Age', axis = 1)
df_30to40 = df_30to40.drop('Age', axis = 1)
df_50to60 = df_50to60.drop('Age', axis = 1)


X_10to20 = df_10to20[['ID']]
Y_10to20 = df_10to20[['Time']]
X_30to40 = df_30to40[['ID']]
Y_30to40 = df_30to40[['Time']]
X_50to60 = df_50to60[['ID']]
Y_50to60 = df_50to60[['Time']]

LR_10to20 = LinearRegression()
LR_10to20.fit(X_10to20, Y_10to20)
y_10to20 = LR_10to20.predict(X_10to20)
print("10~20 R_square: ", r2_score(Y_10to20, y_10to20))
round(float(LR_10to20.coef_))
int(LR_10to20.intercept_)

LR_30to40 = LinearRegression()
LR_30to40.fit(X_30to40, Y_30to40)
y_30to40 = LR_30to40.predict(X_30to40)
print("30~40 R_square: ", r2_score(Y_30to40, y_30to40))
LR_30to40.coef_ 
LR_30to40.intercept_

LR_50to60 = LinearRegression()
LR_50to60.fit(X_50to60, Y_50to60)
y_50to60 = LR_50to60.predict(X_50to60)
print("50~60 R_square: ", r2_score(Y_50to60, y_50to60))
LR_50to60.coef_ 
LR_50to60.intercept_

"""
fittsLR = LinearRegression()
X_all = fitts[['ID']]
Y_all = fitts[['Time']]
fittsLR.fit(X_all, Y_all)
y_all = fittsLR.predict(X_all)
print("All R_square: ", r2_score(Y_all, y_all))
fittsLR.coef_ 
fittsLR.intercept_
g = sns.regplot(x= 'ID', y='Time', data = fitts)
"""

g = sns.regplot(x='ID', y='Time', data = df_10to20)
g = sns.regplot(x='ID', y='Time', data = df_30to40)
g = sns.regplot(x='ID', y='Time', data = df_50to60)
g.set(xlim = (2.5, 4.5))

plt.scatter(X_10to20, Y_10to20)
plt.scatter(X_30to40, Y_30to40)
plt.scatter(X_50to60, Y_50to60)
