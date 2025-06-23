import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from sklearn import metrics

print("pandas:",pd.__version__)
print("numpy:",np.__version__)

data ={
    "experience":[1,3,5,7,9,11,13,15,17,20,18,10],
    "Education":[2,3,3,4,4,5,5,5,6,6,2,5],
    "GPA":[4.5,4.72,4.3,4.32,4.56,4.75,4.74,4.7,4.67,4.61,4.45,4.87],
    "Certification":[0,1,1,2,1,2,3,3,4,5,2,0],
    "Score":[60,65,70,75,80,85,87,90,92,95,70,88],
    "Salary":[3000,4000,5000,6000,7000,7500,8000,9000,9500,11000,10000,9780]
}
df=pd.DataFrame(data)

print(df)

print("mean:\n",df.mean())

plt.xlabel('Salary')
plt.ylabel('count')
plt.hist(df['Salary'],bins=20)
plt.show()

x=df.drop('Salary',axis=1)
y=df['Salary']
x.shape
y.shape

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=23)

lm=LinearRegression()
lm.fit(x_train,y_train)

print("intercept: ",lm.intercept_)

pred=lm.predict(x_test)
print(pred)

real=np.array(y_test)
print(real)

plt.scatter(real,pred)
plt.show()

print("MAE: ",metrics.mean_absolute_error(y_test,pred))
print("MSE: ",metrics.mean_squared_error(y_test,pred))
print("RMSE: ",metrics.root_mean_squared_error(y_test,pred))
print("R^2: ",metrics.r2_score(y_test,pred))
