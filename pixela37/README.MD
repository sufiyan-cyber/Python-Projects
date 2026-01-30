# 📊 Habit & Activity Tracker using Pixela API (Python)

This project is a **Python-based habit/activity tracker** that logs daily activities (like running or cycling distance) as **pixels on a graph** using the **Pixela API**.

Each pixel represents one day of activity, helping build consistency through visual progress.

---

## 🚀 What This Project Does

- Creates a Pixela user account (one-time setup)
- Creates a graph for an activity (one-time setup)
- Adds daily activity data automatically
- Updates previously logged data
- Deletes incorrect entries if required

After initial setup, **only one API call is needed daily**.

---

## 🛠️ Technologies Used

- Python 3
- Requests library
- Pixela REST API
- Datetime module

---

## 📁 Project Structure


pixela-habit-tracker/
│
├── main.py
├── README.md


---

## 🔐 Prerequisites

1. Python 3 installed
2. Install dependencies:
```bash
pip install requests

Create a Pixela account:
https://pixe.la/

⚙️ Initial Setup (Run Only Once)
1️⃣ Configure Credentials

Replace inside main.py:

TOKEN = "your_token_anything"
USERNAME = "your_username"


⚠️ Keep your token secret. Do not push real tokens to GitHub.

2️⃣ Create User (One-Time)
response = requests.post(url=pixel_endpoint, json=user_params)
print(response.text)


After successful execution, comment this line permanently.

3️⃣ Create Graph (One-Time)
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)


After graph creation, comment this permanently.

📆 Daily Usage (Main Feature)
Add Today’s Activity (Pixel Creation)
response = requests.post(
    url=pixel_posting1,
    json=posting_config,
    headers=headers
)
print(response.text)


This:

Automatically uses today’s date

Takes user input for distance

Creates a pixel on the graph

✅ This is the only code needed daily.

🔄 Update a Past Entry
response = requests.put(
    url=update_endpoint,
    json=update_config,
    headers=headers
)
print(response.text)


Use when:

You forgot to log a day

Wrong data was entered

❌ Delete an Entry
response = requests.delete(
    url=delete_endpoint,
    headers=headers
)
print(response.text)


Use to remove incorrect or test data.

🧹 Why So Many Commented Lines?

This project follows phase-based execution:

Feature	Frequency
User Creation	One-time
Graph Creation	One-time
Daily Pixel Entry	Daily
Update Pixel	Occasional
Delete Pixel	Rare

Commented code is kept for:

Learning reference

API reuse

Future expansion

🧠 Concepts Learned
Python

Dictionaries and JSON handling

f-strings

User input handling

Date formatting using strftime()

API & Backend

REST API usage

HTTP methods: POST, PUT, DELETE

Header-based authentication

JSON request bodies

Software Engineering

One-time setup vs recurring logic

Clean API-driven design

Maintainable and readable code

📌 Possible Improvements

Use .env file for tokens

Add error handling

Add multiple graphs

Convert to CLI tool

Automate daily logging

📖 Learning Resources

Python Requests Docs
https://docs.python-requests.org/

REST API Basics
https://restfulapi.net/

Pixela API Documentation
https://docs.pixe.la/
