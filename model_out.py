import numpy as np
import pandas as pd

#讀取csv檔，espana8有做Kmean
data = pd.read_csv('espana8.csv',encoding = 'utf8')

#用pandas的get_dummies做標籤數值化
da=pd.get_dummies(data,columns=
['label','weather_mainba','weather_descriptionba',
'weather_mainbi','weather_descriptionbi','weather_mainma',
'weather_descriptionma','weather_mainse','weather_descriptionse',
'weather_mainva','weather_descriptionva','wind_directionba',
'wind_directionbi','wind_directionma','wind_directionse','wind_directionva','hours'])

#移除時間欄位
da =da.drop(['time'],axis=1,errors='ignore')

#決定預測變數為電價
y=da['price actual']

#特徵變數移除電價
x =da.drop(['price actual',],axis=1)

#標準常態係數
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(x)
x = pd.DataFrame(data=scaler.transform(x), columns=x.columns, index=x.index)


#決定特徵變數及預測變數
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y,test_size=0.7, random_state=101)

#帶入ExtraTrees模型
from sklearn.ensemble import ExtraTreesRegressor
extreg = ExtraTreesRegressor(n_estimators=100, random_state=0)

#測試

extreg.fit(X_train, y_train)
y_pred_ETR_train=extreg.predict(X_train)

print(y_pred_ETR_train)


#輸出訓練好的模型
import pickle

model = extreg.fit(X_train, y_train)
with open('model_ext.pickle', 'wb') as f:
    pickle.dump(model, f)

