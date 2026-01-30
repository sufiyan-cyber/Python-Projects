# Internet Speed Monitor Bot (Selenium + Python)

This project is a **real-world Selenium automation experiment** that measures internet speed using Speedtest.net and explores automated posting to X (formerly Twitter).

More importantly, this repository documents **what works, what breaks, and why** — which is a critical but often ignored part of automation engineering.

---

## 🧠 What This Project Is Actually Teaching

This is **not just a “tweet bot”**.

This project focuses on:
- Automating modern, JavaScript-heavy websites
- Handling cookie consent flows
- Designing Selenium code that survives UI changes
- Understanding why certain automation ideas fail
- Knowing when *not* to automate something

It treats Selenium as an **engineering tool**, not a hack.

---

## 📁 Repository Structure

.
├── main.py
└── README.md


> ⚠️ No browser profiles or credentials are committed.  
> This is intentional and follows best practices.

---

## ⚙️ Core Idea

The bot:
1. Opens Speedtest.net
2. Runs an internet speed test
3. Extracts download & upload speeds
4. (Conceptually) posts results to X / Twitter

Only **Steps 1–3 are executed**.  
Step 4 is **documented but intentionally disabled**.

---

## 🧩 File Breakdown

### `main.py`

The file is structured as a **class-based automation bot**, reflecting scalable design.

---

## 🏗️ Design Choices Explained

### 1. **Explicit Chrome Options**

```python
chrome_options.add_experimental_option("detach", True)
Purpose:

Keeps the browser open after script execution

Allows inspection and debugging

Useful during development and learning

2. Profile-Based Login (Commented Out — Intentionally)
# --user-data-dir
# --profile-directory
Why it exists:
Explored as a way to bypass X login restrictions

Why it is commented:
Causes Chrome–DevTools handshake issues

Unstable on Windows + Python 3.12

Can break Selenium sessions unexpectedly

Key learning:
Not every theoretically valid approach is practically stable.

Leaving this code commented serves as documentation of exploration, not dead code.

🚀 Speedtest Automation (get_internet_speed())
This is the fully working and stable part of the project.

What it demonstrates:
Handling cookie consent popups

Clicking dynamically loaded buttons

Waiting for long-running asynchronous operations

Extracting live-rendered results

Important Design Decisions:
Uses WebDriverWait, not blind sleeps

Uses robust CSS selectors

Only one controlled time.sleep() where unavoidable

Extracts values only after visibility confirmation

Output Example:
[RESULT] Download: 92.31 Mbps
[RESULT] Upload: 11.45 Mbps
🐦 Twitter / X Automation (Documented, Not Executed)
Why this part exists:
Demonstrates intended automation flow

Shows correct selectors and logic

Acts as reference code

Why it is NOT executed:
X actively blocks Selenium-based login

Automated posting violates platform defenses

Profile reuse caused instability

Engineering lesson:
Knowing when automation is blocked — and documenting it — is professional behavior.

This avoids brittle hacks and respects platform constraints.

🧠 Key Automation Lessons Embedded in This Project
Modern sites are hostile to automation

Cookie banners must be handled explicitly

Some waits cannot be avoided

Browser profiles are powerful but risky

Commented code can be educational documentation

Automation ≠ bypassing security

🛠 Technologies Used
Python 3

Selenium WebDriver

ChromeDriver

Google Chrome

Explicit waits (WebDriverWait, EC)

▶️ How to Run
pip install selenium
python main.py
Requirements:

Google Chrome installed

Compatible ChromeDriver in PATH

Stable internet connection
