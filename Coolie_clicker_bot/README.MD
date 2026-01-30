# Cookie Clicker Automation with Selenium (Python)

This project demonstrates **automating a real-time browser game** using Selenium WebDriver.  
The goal is not to “win” the game, but to **learn timing, waits, element state detection, and decision-making logic** in browser automation.

This script uses *Cookie Clicker* as a controlled environment to practice **continuous interaction + periodic evaluation**, which is a common automation pattern.

---

## 🧠 Core Learning Objectives

By reading and running this script, you will learn:

- How to wait for dynamic elements to load properly
- How to interact with frequently changing DOM elements
- How to automate repetitive actions efficiently
- How to implement time-based decision logic
- How to detect element state using CSS classes
- How Selenium behaves in long-running loops

---

## 📁 File Overview

### `main.py`

This file automates gameplay on Cookie Clicker using Selenium.

---

## 🔍 Key Concepts Demonstrated

### 1. **Explicit Waits (Critical Selenium Skill)**

Instead of relying on `time.sleep()`, the script uses:

- `WebDriverWait`
- `expected_conditions (EC)`

This ensures Selenium:
- Waits only as long as necessary
- Interacts with elements *only when they are ready*

This is essential for **reliable automation**.

---

### 2. **Handling Dynamic Pages**

Cookie Clicker loads content dynamically.  
The script waits for:

- Language selection button
- Main cookie element

This teaches how to:
- Handle JavaScript-rendered pages
- Avoid `ElementNotInteractableException`

---

### 3. **High-Frequency Actions (Rapid Clicking)**

```python
for _ in range(50):
    big_cookie.click()
Learning outcome:

Selenium can perform fast, repeated interactions

Loops can be tuned for performance vs stability

Useful for stress-testing UI behavior

4. Time-Based Decision Making
The script tracks time using:

start = time.time()
Every 5 seconds, it:

Evaluates available upgrades

Makes a purchase decision

This pattern is extremely important for:

Bots

Monitoring scripts

Periodic automation tasks

5. Element State Detection via CSS
Instead of reading text or prices, the script checks:

"enabled" in p.get_attribute("class")
This teaches:

How modern web apps encode state in CSS classes

Why class-based detection is often more reliable than text parsing

6. Priority-Based Selection Logic
affordable[-1].click()
This ensures:

The most expensive affordable upgrade is purchased

A simple but effective strategy logic is implemented

Learning takeaway:
Automation is not just clicking — it’s decision logic.

7. Infinite Automation Loop
while True:
This demonstrates:

Long-running Selenium sessions

Continuous monitoring + action cycles

How bots behave differently from one-shot scripts

Important note:
Such loops must be controlled carefully in real projects.

🧪 Practical Skills You Gain
After this project, you understand how to:

Automate non-static, real-time web apps

Combine waits, loops, and conditions

Build logic-driven browser bots

Handle performance-sensitive Selenium tasks

These skills directly transfer to:

Test automation

Web scraping

Bot development

QA engineering

Security automation

🔧 Tools & Technologies Used
Python 3

Selenium WebDriver

Google Chrome

ChromeDriver

JavaScript-heavy web applications

🚀 How to Run
pip install selenium
python main.py
Requirements:

Chrome installed

Compatible ChromeDriver in PATH

📌 Key Takeaway
This project teaches real automation thinking, not just Selenium syntax.

You learn how to:

Observe application state

React at the correct time

Make decisions based on live DOM data

This is a foundational pattern for any serious automation work.
