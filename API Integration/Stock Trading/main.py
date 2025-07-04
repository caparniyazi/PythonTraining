import os
import requests
from twilio.rest import Client

account_sid = os.environ.get("OWM_ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
STOCK_NAME = "TSLA"
COMPANY_NAME = "ORACLE"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

url = "https://www.alphavantage.co/query"
r = requests.get(url, params=stock_params)
data = r.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])
print(yesterday_closing_price)

day_before_yesterday_closing_price = float(data_list[1]["4. close"])
print(day_before_yesterday_closing_price)
price_diff = float(abs(yesterday_closing_price - day_before_yesterday_closing_price))
print(price_diff)
diff_percent = (price_diff / yesterday_closing_price) * 100
print(diff_percent)

if diff_percent > 0:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": os.environ.get("NEWS_API_KEY")
    }
    news_data = requests.get(
        NEWS_ENDPOINT,
        news_params
    )

    three_articles = news_data.json()["articles"][:3]
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in
                          three_articles]
    print(formatted_articles)

    # Send each article as a separate message via Twilio.
    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="whatsapp:+14155238886",
            to="whatsapp:+905355599567"
        )
