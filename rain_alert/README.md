# 🌧 Rain SMS Alert — Python Automation Project

This project checks the weather forecast using the **OpenWeather API** and sends an **SMS alert using Twilio** if rain is expected in the next few forecast periods. It can be run manually or scheduled (e.g., on PythonAnywhere) to notify you once per day.



## 🚀 How It Works

1. The script calls the **5-day / 3-hour forecast API** from OpenWeather.
2. It reads the next 4 forecast entries.
3. If any weather condition ID is **< 700**, rain is expected.
4. On rainy days, an SMS is sent automatically using the Twilio API.




> ⚠️ The real `.env` file should not be uploaded to GitHub. Only `.env.example` is shared for reference.

---

## 🔧 Environment Variables

Create a `.env` file based on `.env.example` and add your own API credentials:

you can use twilio website sign up for a free account and get basic credits this is where u get ur account sid auth token api key u can 
find in weather api website make sure to verify ur account to avoid api failures also only verified phone numbers added in twilio website
can u send the sms to later u can use pythonanywhere to automate your task 

