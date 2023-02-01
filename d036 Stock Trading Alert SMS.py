import requests
from twilio.rest import Client
import datetime as dt

# ------------------------ constants ---------------------
STOCK = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_API_KEY = 'your api key'
NEWS_API_KEY = 'your api key'
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# ----------------------- Retrieve today and yesterday's date ------------------

today = dt.date.today()
current_date = str(today)
yesterday_date = str(today - dt.timedelta(days=1))

# ----------------------- Stock and News API Setup ----------------------

stock_params = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK,
    'apikey': STOCK_API_KEY
}
news_params = {
    'q': COMPANY_NAME,
    'searchIn': 'title',
    'lang': 'en',
    'sortBy': 'popularity',
    'apiKey': NEWS_API_KEY
}

stock_api = requests.get(STOCK_ENDPOINT, params=stock_params)
news_api = requests.get(NEWS_ENDPOINT, params=news_params)
stock_json = stock_api.json()
stock_data = stock_json["Time Series (Daily)"]
news_json = news_api.json()
news_data = news_json['articles']

# formatting stock api data into usable data
todays_closing_price = float(stock_data[current_date]["4. close"])
yest_closing_price = float(stock_data[yesterday_date]["4. close"])

# formatting news api data into usable data
article_title = news_data[0]['title'].title()
article_body = news_data[0]['description']


# ----------------------- Stock Change Calculator -------------------

# if a stock changes more than 5% of its price, send articles
def stock_change_calc():
    closing_price_dif = todays_closing_price - yest_closing_price
    percent_of_yest = round(abs(closing_price_dif) / yest_closing_price)
    if percent_of_yest > 5 and closing_price_dif >= 0:
        return f'''
        TSLA: 🔺{percent_of_yest}%
        {article_title}:
        {article_body}'''
    elif percent_of_yest > 5 and closing_price_dif < 0:
        return f'''
        TSLA: 🔻{percent_of_yest}%
        {article_title}:
        {article_body}'''
    elif closing_price_dif >= 0:
        return f'''TSLA: 🔺{percent_of_yest}%'''
    else:
        return f'''TSLA: 🔻{percent_of_yest}%'''


# ---------------------- Send SMS Update on Stock ----------------------

twilio_client = Client('your twilio acct sid', 'your twilio auth token')
message = twilio_client.messages \
    .create(
    body=f'{stock_change_calc()}',
    from_='your twilio #',
    to='your phone #'
)
