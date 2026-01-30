# 📸 Instagram Auto-Follow Bot

A Python-based automation tool using **Selenium** to log in to Instagram, navigate to a specific target profile, and automate the process of following their followers.

This bot includes specific workarounds for Instagram's React-based UI (using JavaScript executors for clicks) and implements human-like delays to mitigate bot detection.

## ⚠️ Important Disclaimer

**Use this tool at your own risk.**

Automating actions on Instagram (following, liking, commenting) violates their [Terms of Service](https://help.instagram.com/581066165581870). Excessive use **will** lead to:
1.  **Temporary Action Blocks** ("Try Again Later" errors).
2.  **Shadowbans** (Your content becomes invisible).
3.  **Permanent Account Suspension**.

**Safety Tips:**
* Do not run this 24/7.
* Keep `MAX_USERS` low (start with 10-20 per day).
* Ensure random sleep timers are enabled in the code.

---

## 🚀 Features

* **Automated Login:** Handles credential entry securely using environment variables.
* **Smart Navigation:** Navigates directly to a target user's follower list.
* **Robust Selectors:** Uses advanced XPath strategies (`//div[text()='Follow']/ancestor::button`) to locate buttons reliably within Instagram's dynamic React DOM.
* **Click Interception Bypass:** Uses `driver.execute_script()` to force clicks on elements that standard Selenium methods fail to interact with.
* **Anti-Bot Measures:** (Recommended) Includes randomized sleep timers to mimic human behavior.

## 🛠️ Prerequisites

* [Python 3.x](https://www.python.org/downloads/)
* [Google Chrome](https://www.google.com/chrome/) installed.
* A valid Instagram account.

## 📦 Installation

1.  **Clone the repository** (or create your project folder):
    ```bash
    mkdir instagram-bot
    cd instagram-bot
    ```

2.  **Install required Python packages:**
    ```bash
    pip install selenium python-dotenv
    ```

## ⚙️ Configuration

1.  Create a file named `.env` in the root of your project folder.
2.  Add your Instagram credentials to the file:

    ```env
    INSTA_USERNAME=your_username_here
    INSTA_ACCOUNT_PASSWORD=your_password_here
    ```
    *(Note: This file should not be shared or committed to GitHub).*

3.  **Adjust Script Variables:**
    Open `main.py` and set your target account and limits:
    ```python
    TARGET_ACCOUNT = "chef_pillai" # The account whose followers you want to follow
    MAX_USERS = 10                 # Start small to avoid bans!
    ```

## 🏃 Usage

Run the script from your terminal:

```bash
python main.py
🐛 Troubleshooting
"Try Again Later" Error
If you see a popup saying "We restrict certain activity...", you have been flagged for spamming.

Solution: Stop the script immediately. Do not attempt to follow anyone (manually or automatically) for 24 to 48 hours.

Script finds buttons but doesn't click
If the logs say [ACTION] Clicking... but the UI doesn't change:

Ensure you are using the JavaScript executor method:

Python
driver.execute_script("arguments[0].click();", btn)
Standard .click() often fails on Instagram due to invisible overlays.

Crash: "Element not interactable" or "NoSuchElement"
Instagram updates its layout frequently. If the script breaks, check if the XPath //div[text()='Follow'] is still valid by inspecting the page source in Chrome Developer Tools (F12).

📄 License
Distributed under the MIT License. See LICENSE for more information.
