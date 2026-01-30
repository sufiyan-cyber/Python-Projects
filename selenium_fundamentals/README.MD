# Selenium Automation Learning Project (Python)

This repository contains two Python scripts created while learning **browser automation using Selenium WebDriver**.  
The focus of this project is **understanding how Selenium interacts with real web pages**, how elements are located, and how extracted data can be structured meaningfully.

Rather than being a production-ready automation suite, this project is intentionally **learning-oriented**.

---

## 🧠 Core Learning Objectives

By studying and running these files, you will learn:

- How Selenium controls a real Chrome browser
- How to locate web elements using different strategies
- How to send keyboard input programmatically
- How to extract structured data from live websites
- How to convert scraped data into Python data structures
- Why and when certain Selenium approaches are commented out

---

## 📁 Project Files Overview

### 1. `challenge.py`

This script focuses on **form automation and user input simulation**.

#### What this file demonstrates:

- Initializing Chrome with custom options
- Preventing the browser from closing automatically
- Navigating to a live web application
- Locating form input fields using the `name` attribute
- Sending text input and simulating the ENTER key

#### Key Selenium Concepts Covered:

- `webdriver.ChromeOptions()`
- `add_experimental_option("detach", True)`
- `find_element(By.NAME, ...)`
- `send_keys()` with `Keys.ENTER`

#### Practical Learning Outcome:

You learn how automated scripts can:
- Mimic real user behavior
- Submit forms without clicking buttons
- Be used in testing, scraping, or QA workflows

This is a **foundation script** for understanding browser interaction.  
:contentReference[oaicite:0]{index=0}

---

### 2. `main.py`

This script is more **exploratory and data-oriented**, showcasing multiple Selenium techniques in a single file.

#### What this file demonstrates:

##### 1. **Navigation Control**
- Switching between different websites using `driver.get()`
- Understanding that Selenium sessions persist across page loads

##### 2. **Element Location Strategies (Commented Section)**

Several lines are intentionally commented out to show **alternative approaches** without executing them every time:

- Locating elements by:
  - `NAME`
  - `ID`
  - `CSS_SELECTOR`
  - `XPATH`
- Reading attributes like placeholders
- Inspecting element dimensions (`.size`)
- Extracting visible text from links

These comments act as a **reference notebook**, not dead code.

##### 3. **Real-World Web Scraping Example**

The active portion of the script:

- Extracts upcoming event dates from `python.org`
- Extracts corresponding event names
- Aligns dates with events using indexing
- Stores the final data in a Python dictionary

```python
{
  0: {'time': '2026-02-10', 'name': 'Event Name'},
  1: {'time': '2026-02-17', 'name': 'Another Event'}
}
4. Data Structuring
You learn how to:

Convert raw web elements into lists

Slice lists to remove irrelevant data

Combine multiple lists using zip()

Build dictionaries suitable for APIs or databases

5. Clean Resource Handling
Properly closing the browser using driver.quit()

Practical Learning Outcome:
This file teaches how scraping is more than just extracting text — it is about:

Selecting the correct DOM scope

Matching related data correctly

Producing structured, usable outputs


main


🔧 Tools & Technologies Used
Python 3

Selenium WebDriver

Google Chrome

ChromeDriver

HTML / DOM Inspection

🚀 Who This Project Is For
Beginners learning Selenium

Students exploring automation and scraping

Anyone transitioning from manual testing to automation

Developers wanting hands-on DOM interaction experience

📌 Key Takeaway
This project is not about “just running scripts”.
It is about understanding how browsers, DOM trees, and automation logic interact — which is essential for:

Test Automation

Web Scraping

QA Engineering

Cybersecurity Reconnaissance

Backend Data Collection

🧪 How to Run
pip install selenium
python challenge.py
python main.py
Ensure:

Chrome is installed

ChromeDriver version matches your Chrome browser
