#從網站輸入原物料價格及5個城市的天氣
#將數值與其他預設值帶入機器學習的模型輸出電價，再顯示到網頁

import numpy as np
import pandas as pd
import pickle

#下面這個方便用來新增表格用的
'''
data = pd.read_csv('espana8.csv',encoding = 'utf8')
ll = list(data)
aa=[]
co = data.loc[1]
x_web = pd.DataFrame(co,columns=ll)
for i in x_web:
    print( "\'" + i + "\'" + ":" + "\'\'" + ",")
'''

def price(x_gas,x_coal,x_oil,x_bio,x_u235,x_we,hours):
    
    #建立新一筆資料，將要由網頁填入的部分設成參數
    x_web = pd.DataFrame({
    'generation biomass':'290',
    'generation fossil brown coal/lignite':'113',
    'generation fossil gas':'6926',
    'generation fossil hard coal':'2166',
    'generation fossil oil':'163',
    'generation hydro pumped storage consumption':'108',
    'generation hydro run-of-river and poundage':'1069',
    'generation hydro water reservoir':'1686',
    'generation nuclear':'6075',
    'generation other':'61',
    'generation other renewable':'92',
    'generation solar':'31',
    'generation waste':'287',
    'generation wind onshore':'3651',
    'forecast solar day ahead':'26',
    'forecast wind onshore day ahead':'3117',
    'total load forecast':'24424',
    'total load actual':'24455',
    'price day ahead':'64.27',
    'tempba':'69.88',
    'temp_minba':'280.13',
    'temp_maxba':'277.15',
    'pressureba':'1028',
    'humidityba':'100',
    'wind_speedba':'5',
    'wind_directionba':'NW',
    'rain_1hba':'0',
    'snow_3hba':'0',
    'clouds_allba':'0',
    'weather_mainba':x_we,
    'weather_descriptionba':'sky is clear',
    'tempbi':'275.6',
    'temp_minbi':'275.15',
    'temp_maxbi':'276.15',
    'pressurebi':'1034',
    'humiditybi':'93',
    'wind_speedbi':'2',
    'wind_directionbi':'E',
    'rain_1hbi':'0',
    'snow_3hbi':'0',
    'clouds_allbi':'0',
    'weather_mainbi':x_we,
    'weather_descriptionbi':'sky is clear',
    'tempma':'275.15',
    'temp_minma':'275.15',
    'temp_maxma':'275.15',
    'pressurema':'1031',
    'humidityma':'74',
    'wind_speedma':'1',
    'wind_directionma':'N',
    'rain_1hma':'0',
    'snow_3hma':'0',
    'clouds_allma':'0',
    'weather_mainma':x_we,
    'weather_descriptionma':'sky is clear',
    'tempse':'283.97',
    'temp_minse':'282.15',
    'temp_maxse':'285.15',
    'pressurese':'1029',
    'humidityse':'70',
    'wind_speedse':'3',
    'wind_directionse':'NE',
    'rain_1hse':'0',
    'snow_3hse':'0',
    'clouds_allse':'0',
    'weather_mainse':x_we,
    'weather_descriptionse':'sky is clear',
    'tempva':'279.14',
    'temp_minva':'278.15',
    'temp_maxva':'280.15',
    'pressureva':'1029',
    'humidityva':'75',
    'wind_speedva':'2',
    'wind_directionva':'NW',
    'rain_1hva':'0',
    'snow_3hva':'0',
    'clouds_allva':'0',
    'weather_mainva':x_we,
    'weather_descriptionva':'sky is clear',
    'coal_price':x_coal,
    'fossil_oil_price':x_oil,
    'natgas_price':x_gas,
    'soybean_oil_price':x_bio,
    'u_235_price':x_u235,
    'hours':hours,
    'label':0,           #這邊是數值不是字串，字串會出錯
    },index=[0])

    #讀取既有資料，做one-hot-coding的前置作業
    data = pd.read_csv('espana8.csv',encoding = 'utf8')
    data =data.drop(['time'],axis=1,errors='ignore')
    data =data.drop(['price actual'],axis=1,errors='ignore')

    #合併新建資料跟既有資料
    x = pd.concat([data,x_web],ignore_index = True)

    #做one-hot-coding，不加入既有資料，one-hot-coding會失敗(參數過少)
    x = pd.get_dummies(x,columns=['label','weather_mainba','weather_descriptionba','weather_mainbi','weather_descriptionbi','weather_mainma','weather_descriptionma','weather_mainse','weather_descriptionse','weather_mainva','weather_descriptionva','wind_directionba','wind_directionbi','wind_directionma','wind_directionse','wind_directionva','hours'])

    #標準化
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    scaler.fit(x)
    x = pd.DataFrame(data=scaler.transform(x), columns=x.columns, index=x.index)

    #取最後一筆，就是新建的資料
    x = x.tail(1)


    #載入模型
    with open('model_ext.pickle', 'rb') as f:
        model = pickle.load(f)
    y = model.predict(x)

    return y
#price('10','10','10','10')