import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
alphaapi=os.environ["alphaapi"]
newsapi=os.environ["newsapi"]
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

stockparams={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":alphaapi

}
response=requests.get(STOCK_ENDPOINT,stockparams)
jsonform=response.json()

data=jsonform['Time Series (Daily)']
data_items=[value for (key,value) in data.items()]
yesterdays_data=data_items[0]
yesterdays_closing=yesterdays_data["4. close"]
print(yesterdays_closing)

day_before_yesterday_data=data_items[1]
day_before_yesterdays_closing=day_before_yesterday_data["4. close"]
print(day_before_yesterdays_closing)

newdiff=float(yesterdays_closing)-float(day_before_yesterdays_closing)
up_down=None
if newdiff>0:
    up_down="⬆️"
else:
    up_down="🔻"

diff_percent = abs(((newdiff) / float(yesterdays_closing)))* 100

print(diff_percent)

if diff_percent>2:
    news_params={
        "apikey":newsapi,
        "q":COMPANY_NAME,
        "searchIn":"title"

    }
    response=requests.get(NEWS_ENDPOINT,params=news_params)
    articles=response.json()["articles"]
    three_articles=articles[:3]
    print(three_articles)




formatted_articles=[f"{STOCK_NAME}:{up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief:{article['description']}    " for article in three_articles]
client = Client(account_sid, auth_token)


for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_="your_twilio_trial_number",
        to="your_number",
    )








