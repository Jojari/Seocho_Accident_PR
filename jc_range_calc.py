# -*- coding: utf-8 -*-
"""JC_Range_Calc.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BrXmApK-MynPHPhyBUZ88YoOm6BQr096
"""

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv("/content/drive/My Drive/Colab Notebooks/jc_correlation_factor.csv", encoding = 'UTF-8')

X = df.iloc[:,:-1]
Y = df.iloc[:,-1]

leg = LinearRegression()
leg.fit(X = pd.DataFrame(X), y = Y)
prediction = leg.predict(X = pd.DataFrame(X))

#a value는 Y절편, b value는 각 독립변수별 기울기
print('a value = ', leg.intercept_)
print('b value = ', leg.coef_)

a_value = leg.intercept_
b_value = leg.coef_

#실제 활용할 함수
lanes = float(input('차로 수를 입력하세요 : '))
wth = float(input('차로 폭을 입력하세요 : '))

r = (b_value[0] * lanes) + (b_value[1] * wth) + a_value
print("해당 조건에서의 교차로 반경 : %d"%(r))