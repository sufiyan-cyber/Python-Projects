# ✈️ Flight Price Tracker (Capstone Project-1)

This project is a **flight price monitoring system** that checks live flight prices using the **Amadeus API**, compares them against predefined target prices stored in **Google Sheets**, and sends a **notification** when a cheaper flight is found.

The goal is not to book flights, but to **monitor prices automatically** and alert when a deal appears.

---

## 🧠 Core Idea (One Paragraph)

Destinations and target prices are stored in a Google Sheet.
The program reads this data, searches live flight offers for each destination using the Amadeus API, finds the **cheapest available flight**, and compares it with the target price.
If the live price is lower, a WhatsApp/SMS notification is sent using Twilio.

---

## 🔄 High-Level Flow

```
Google Sheet (target prices)
        ↓
Fetch destinations via Sheety API
        ↓
Search live flights via Amadeus
        ↓
Extract cheapest flight
        ↓
Compare with target price
        ↓
Send notification if cheaper
```

---

## 🗂️ Project Structure & Responsibilities

### `main.py` — Orchestrator

Controls the entire flow of the application:

* Fetches destination data from Google Sheets
* Triggers flight searches for each destination
* Compares live prices with stored prices
* Sends notifications when a deal is found

This file **does not handle API logic directly** — it coordinates other modules.

---

### `data_manager.py` — Google Sheets (Sheety API)

Responsible for **reading and updating data** in Google Sheets.

Key responsibilities:

* Fetch destination data (`city`, `iataCode`, `lowestPrice`)
* Update missing IATA codes back into the sheet
* Acts as persistent storage for target prices

---

### `flight_search.py` — Amadeus API Integration

Handles all interaction with the **Amadeus API**.

Key responsibilities:

* Authenticate using OAuth 2.0 (API key + secret → token)
* Convert city names to IATA airport codes
* Search for flight offers between two airports for a given date range

This module returns **raw flight data**, not business decisions.

---

### `flight_data.py` — Flight Analysis & Comparison

Processes raw flight data and extracts only what matters.

Key responsibilities:

* Parse Amadeus flight responses
* Identify the **cheapest flight** among available options
* Return structured flight data (price, airports, dates)

This keeps comparison logic separate and clean.

---

### `notification_manager.py` — Alerts (Twilio)

Handles sending notifications when a deal is found.

Supported channels:

* WhatsApp (via Twilio WhatsApp Sandbox)
* SMS (optional fallback)

This module is triggered **only when a cheaper flight is detected**.

---

## 🧮 How Price Comparison Works

1. For each destination, fetch live flight offers
2. Extract the **lowest available price**
3. Compare it with `lowestPrice` from Google Sheets
4. If:

   ```
   live_price < target_price
   ```

   → Trigger notification

This makes the system a **price monitor**, not just a search tool.

---

## ⚠️ Important Notes

* The project uses the **Amadeus Test API**, which has limited data
* Some routes may return no results (handled safely in code)
* IATA codes are fetched once and stored to avoid repeated API calls
* Notifications may fail if Twilio credentials or WhatsApp sandbox setup is incomplete

---

## 🧪 Environment Variables

Sensitive credentials are stored using environment variables.

Example (`.env.example`):

```env
AMADEUS_API_KEY=your_api_key
AMADEUS_SECRET=your_api_secret

SHEETY_USERNAME=your_username
SHEETY_PASSWORD=your_password

TWILIO_SID=your_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_WHATSAPP_NUMBER=number
TWILIO_VERIFIED_NUMBER=+91XXXXXXXXXX
```

---

## 🎯 What This Project Demonstrates

* Working with multiple external APIs
* OAuth 2.0 authentication
* REST API integration and error handling
* Parsing complex JSON responses
* Clean separation of concerns
* Real-world backend workflow design

---


## 📌 Summary

This project simulates a real-world backend service that:

* Monitors live data
* Compares it with stored expectations
* Notifies users only when action is needed

It focuses on **automation, comparison logic, and API integration**, rather than UI or booking functionality.

---

If you want next, I can:

* Tailor this README for **resume/portfolio**
* Simplify it for **course submission**
* Or add **architecture diagrams (ASCII)**

Just say 👍
