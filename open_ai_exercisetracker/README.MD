# 🤖 Workout & Calorie Logging Automation (Python)

This project automates the process of **tracking workouts and calories** by converting natural language input into structured data and automatically logging it into a Google Sheet using APIs.

Instead of manually entering workouts, the entire flow is handled programmatically.

---

## 🚀 What This Project Does

- Takes natural language input (e.g. *“ran 5 km and cycled for 20 minutes”*)
- Uses an exercise API to:
  - Detect activities
  - Calculate duration
  - Estimate calories burned
- Automatically logs each activity into a Google Sheet
- Performs a health check to ensure the API service is running

---

## 🛠️ Tech Stack

- Python
- Requests
- Environment variables (`dotenv`)
- Nutrition / Exercise API
- Sheety API (Google Sheets automation)

---

## ⚙️ Automation Flow

1. User enters activities in plain English  
2. API converts text → structured workout data  
3. Script loops through all detected exercises  
4. Each exercise is automatically saved to Google Sheets  
5. No manual calculation or data entry needed  

---

## 🧠 What You Learn From This Project

### 🔁 Automation Concepts
- Eliminating repetitive manual work
- Turning user input into automated workflows
- API-to-API data pipelines

### 🌐 API Skills
- Making authenticated POST requests
- Handling JSON responses
- Chaining multiple APIs together
- Health check endpoints

### 🧱 Backend Engineering
- Environment variable management (`.env`)
- Secure handling of API keys
- Looping and processing dynamic API responses
- Clean separation of logic (input → processing → storage)

---

## 📌 Why This Project Matters

This is a **real-world automation use case**:
- Similar patterns are used in backend services, data pipelines, and SaaS tools
- Demonstrates how APIs can replace manual tracking apps
- Strong example of **practical Python + API integration**

---

## 🔮 Possible Extensions

- Add error handling and retries
- Add daily automation using cron / scheduler
- Add user authentication
- Build a simple frontend on top of this
- Generate weekly or monthly workout reports

---

## ✅ Summary

This project focuses on **automation, not just coding** —  
turning unstructured human input into **reliable, repeatable, automated data tracking** using Python and APIs.
