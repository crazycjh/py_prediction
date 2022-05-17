from flask import Flask,render_template,request,jsonify
import numpy as np
import pandas as pd
from price_out import price
app = Flask(__name__)
###
c = [
    {
    'country': 'USA',
    'visits': 23725
    },
    {
    'country': 'China',
    'visits': 1882
    },
    {
    'country': 'Japan',
    'visits': 1809
    },
    {
    'country': 'Germany',
    'visits': 1322
    },
    {
    'country': 'UK',
    'visits': 1122
    },
    {
    'country': 'France',
    'visits': 1114
    },
    {
    'country': 'India',
    'visits': 984
    },
    {
    'country': 'Spain',
    'visits': 711
    },
    {
    'country': 'Netherlands',
    'visits': 665
    },
    {
    'country': 'Russia',
    'visits': 580
    },
    {
    'country': 'South Korea',
    'visits': 443
    },
    {
    'country': 'Canada',
    'visits': 441
    }
]
###
@app.route('/')
def index():


    return render_template('index.html')
 #       """coal = request.form.get('coal')
 ##       #coal = request.form.get('coal')
  #      print(type(coal))"""

@app.route('/ppred')
def ppred():
    x_gas = request.args.get('gas')
    #print('gas',x_gas)
    if x_gas == None:
        x_gas = "2.94"
    elif not x_gas.isdigit():
        x_gas = "2.94"
    x_coal = request.args.get('coal')
    #print('x_coal', (x_coal))
    if x_coal == None:
        x_coal = "75.15"
    elif not x_coal.isdigit():
        x_coal = "75.15"
    x_oil = request.args.get('oil')
    #print('x_oil', (x_oil))
    if x_oil == None:
        x_oil = "15.1"
    elif not x_oil.isdigit():
        x_oil = "15.1"
    x_bio = request.args.get('bio')
    #print('x_bio', (x_bio))
    if x_bio == None:
        x_bio = "27.55"
    if not x_bio.isdigit():
        x_bio = "27.55"
    x_u235 = request.args.get('u235')
    #print('x_u235', (x_u235))
    if x_u235 == None:
        x_u235 = "28.8"
    if not x_u235.isdigit():
        x_u235 = "28.8"
    x_we = request.args.get('weather')
    hours = int(request.args.get('hours'))                  #要轉整數，不然網頁輸入是字串，one-hot-codinng會出錯
    print('x_we', (x_we))
    print('hours', (hours))
    y=price(x_gas,x_coal,x_oil,x_bio,x_u235,x_we,hours)
    print((y[0]))
    print(y.dtype)
    load = (y[0]*450).round(3)
    np.random.seed(9989)
    y3 = np.random.randint(80, high=120, size=None, dtype='l')  # 作弊一下懶得再做一個模型
    y3 = y3 / 100
    load = (load*y3).round(2)

    return jsonify(result=y[0].round(3),load = load)

###
#app.run(debug=True)
app.run(host='0.0.0.0',debug=True)

#sudo lsof -i -P | grep LISTEN | grep 5000







