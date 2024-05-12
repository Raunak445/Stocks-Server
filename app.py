from flask import Flask, jsonify, request
from stock_scrapper import get_stock_prices
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/stock-prices/*": {"origins": "*"}})  # Allow CORS for all stock-prices routes

@app.route('/stock-prices')
def stock_prices():
    page = int(request.args.get('page', 1))  # Get the requested page number from the query parameters
    items_per_page = 5  # Define the number of items per page
    tickers = ['INFY','RELIANCE','TCS','HDFCBANK','HDFC','ITC','WIPRO','HCLTECH','ICICIBANK','KOTAKBANK','LT','SBIN','AXISBANK','BAJFINANCE','BAJAJFINSV','MARUTI','BHARTIARTL','TECHM','NESTLEIND','UPL',"ZOMATO"]  # Example list of tickers

    # Calculate the total number of pages based on the total number of items and items per page
    total_pages = -(-len(tickers) // items_per_page)  # Round up to the nearest integer

    # Calculate the start and end indices for the current page
    start_index = (page - 1) * items_per_page
    end_index = min(start_index + items_per_page, len(tickers))

    # Get the tickers for the current page
    page_tickers = tickers[start_index:end_index]

    # Get stock prices for the tickers of the current page
    stock_prices = get_stock_prices(page_tickers)

    # Return the stock prices along with the total page information
    return jsonify({
        'data': stock_prices,
        'totalPages': total_pages-1
    })

if __name__ == '__main__':
    app.run(debug=True)
