from flask import Flask, jsonify
from stock_scrapper import get_stock_prices

app = Flask(__name__)

@app.route('/stock-prices')
def stock_prices():
    tickers = ['INFY','RELIANCE','TCS','HDFCBANK','HDFC','ITC','WIPRO','HCLTECH','ICICIBANK','KOTAKBANK','LT','SBIN','AXISBANK','BAJFINANCE','BAJAJFINSV','MARUTI','BHARTIARTL','TECHM','NESTLEIND','UPL',"ZOMATO"]
    stock_prices = get_stock_prices(tickers)
    return jsonify(stock_prices)





if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
