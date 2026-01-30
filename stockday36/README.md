# 📈 Stock News Alert System (Python + APIs)

A Python automation script that monitors a stock’s daily price movement and sends **SMS alerts with top news headlines** when the price changes beyond a defined threshold.

This project combines **real-time financial data**, **news aggregation**, and **SMS notifications**, and is meant as a practical backend/API-integration exercise.

---

## 🚀 What This Project Does

1. Fetches daily stock prices from Alpha Vantage  
2. Compares yesterday vs day-before-yesterday closing prices  
3. Calculates percentage change  
4. Detects price direction (⬆️ up / 🔻 down)  
5. If change exceeds a threshold (default: 2%):
   - Fetches top 3 related news articles
   - Sends SMS alerts using Twilio

---

## 🧠 Why This Project Exists

- Learn how real-world APIs work together  
- Practice environment variable management  
- Handle JSON responses safely  
- Build an automation + notification system  
- Understand backend alert workflows  

---

## 🗂️ Project Structure

```
stockday36/
├── main.py        # Core logic
├── .env           # Secrets (not committed)
├── README.md
└── venv/          # Virtual environment
```

---

## 🔧 Tech Stack

- Python 3  
- requests  
- python-dotenv  
- Twilio SDK  
- Alpha Vantage API  
- NewsAPI  

---

## 🔑 APIs & Docs

- Alpha Vantage: https://www.alphavantage.co/documentation/  
- NewsAPI: https://newsapi.org/docs  
- Twilio SMS: https://www.twilio.com/docs/sms  

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/stock-news-alert.git
cd stock-news-alert
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
```

Activate:
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

### 3️⃣ Install Dependencies
```bash
pip install requests python-dotenv twilio
```

### 4️⃣ Create `.env` File
Create a `.env` file in the project root:

```env
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=your_auth_token_here
```

Add to `.gitignore`:
```
.env
```

---

### 5️⃣ Configure API Keys
In `main.py`:
```python
mynewkey = "YOUR_ALPHA_VANTAGE_API_KEY"
newsapi = "YOUR_NEWS_API_KEY"
```

---

### 6️⃣ Configure Phone Numbers
```python
from_="+1XXXXXXXXXX"   # Twilio number
to="+91XXXXXXXXXX"     # Your phone number
```

---

### 7️⃣ Run the Script
```bash
python main.py
```

You’ll receive SMS alerts when the stock changes more than **2%** 📩

---

## 🧮 Core Logic Explained

```
Difference = Yesterday Close − Day Before Yesterday Close
Percentage Change = |Difference| / Yesterday Close × 100
```

Direction:
- ⬆️ Price increased
- 🔻 Price decreased

Trigger:
```python
if diff_percent > 2:
```

---

## 📩 SMS Format Example

```
TSLA:⬆️3.12%
Headline: Tesla, Inc. (TSLA): A Bull Case Theory
Brief: Analysts highlight strong growth prospects...
```

---

## 🛑 Common Errors

### ❌ KeyError: TWILIO_ACCOUNT_SID
✔️ `.env` not loaded  
✔️ Ensure:
```python
from dotenv import load_dotenv
load_dotenv()
```

---

## 🔮 Future Improvements

- Prevent duplicate alerts
- Support multiple stocks
- Add email / WhatsApp alerts
- Store data in a database
- Schedule with cron
- Dockerize the project

---

## 📚 Notes for Future Me

- Start with `main.py`
- Check `.env` first if errors occur
- Review API limits if data looks wrong

This project demonstrates solid backend fundamentals and API integration patterns.
