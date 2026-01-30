import requests
from datetime import datetime
import os

from dotenv import load_dotenv

load_dotenv()

# current date & time
now = datetime.now()


# ---------------- HEALTH CHECK ----------------
urlhealth = "https://app.100daysofpython.dev/healthz"
health_check = requests.get(url=urlhealth)
print("Health check:", health_check.text)

appid=os.environ['appid']
appkey=os.environ['appkey']
sheetyendpoint=os.environ['sheetypoint']
auth=os.environ['auth']
# ---------------- ENDPOINTS ----------------
sheety_endpoint = sheetyendpoint
base_endpoint = "https://app.100daysofpython.dev"
posting_url = f"{base_endpoint}/v1/nutrition/natural/exercise"

# ---------------- HEADERS ----------------
headers = {
    "Content-Type": "application/json",
    "x-app-id": appid,
    "x-app-key": appkey,
}

# ---------------- USER INPUT ----------------
payload = {
    "query": input("So what all did you do today? ")
}

# ---------------- NUTRITION API CALL ----------------
response = requests.post(posting_url, json=payload, headers=headers)
print("Nutrition API status:", response.status_code)

result = response.json()
print("RAW EXERCISES FROM API:")
for ex in result["exercises"]:
    print(ex["name"], ex["duration_min"], ex["nf_calories"])


# ---------------- DATE & TIME ----------------
date = now.strftime("%d/%m/%Y")
time = now.strftime("%I:%M:%S %p")

authorize_header={
"Authorization":auth,
}
# ---------------- LOOP THROUGH ALL EXERCISES ----------------
for activity in result["exercises"]:
    exercise = activity["name"].title()
    duration_min = activity["duration_min"]
    calories = activity["nf_calories"]

    sheety_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration": duration_min,
            "calories": calories
        }
    }

    response2 = requests.post(
        url=sheety_endpoint,
        json=sheety_params,
        headers=authorize_header,
    )

    print(
        f"Added → {exercise} | {duration_min} min | {calories} cal "
        f"| Status: {response2.status_code}"
    )
