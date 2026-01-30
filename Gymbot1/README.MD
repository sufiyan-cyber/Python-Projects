# Advanced Selenium Automation – Gym Class Booking Bot (Python)

This project is a **deep, real-world Selenium automation script** that simulates how a human would log in, browse schedules, book classes, handle waitlists, and verify bookings on a dynamic web application.

Unlike simple Selenium demos, this project focuses on **robust automation design**, **state handling**, **error recovery**, and **post-action verification**.

---

## 🧠 What This Project Is Really About

This is **not just a Selenium script**.

It is an exercise in:
- Writing resilient automation
- Handling unpredictable UI states
- Designing automation like a system, not a macro
- Treating browser automation as software engineering

If someone reads this repository carefully, they should understand **how to think in automation**, not just how to write Selenium syntax.

---

## 📁 Repository Structure

.
├── main.py
└── Chrome_Profile/ (local only, NOT committed to GitHub)


> ⚠️ **Important**  
> The `Chrome_Profile` directory is intentionally **not uploaded** to GitHub.  
> It is created locally to persist browser session data and should be excluded via `.gitignore`.

---

## 🔐 Chrome Profile Usage (Important Design Choice)

This script uses a **custom Chrome user profile**:

```python
--user-data-dir=Chrome_Profile
Why this matters:
Preserves login sessions

Stores cookies and site data

Avoids repeated authentication challenges

Mimics real user behavior more accurately

Why it is NOT on GitHub:
Contains session data

Potentially sensitive browser state

Machine-specific

Violates best security practices if shared

This is an intentional professional automation practice, not an omission.

🧩 File Breakdown
main.py
This file is structured into clear functional phases, each representing a real automation concern.

🔑 Phase 1: Configuration & Setup
Concepts Learned:
Secure credential separation

Centralized constants

Browser lifecycle control

Explicit waits over static delays

Key ideas:

WebDriverWait is used everywhere

No time.sleep() abuse

Browser is detached for debugging and visibility

🔐 Phase 2: Login Automation (login())
This function handles:

UI-based authentication

Dynamic element loading

Login success validation

Timeout recovery

Key Learning Points:
Login success is verified, not assumed

TimeoutException is handled gracefully

Function always returns a value (critical design habit)

This avoids fragile “click and hope” automation.

📅 Phase 3: Class Discovery & Booking (bookaday())
This is the core logic engine of the project.

What it does:
Scans all available class cards

Identifies day group via DOM traversal

Filters classes by:

Day (Tuesday / Thursday)

Time (6:00)

Reacts differently based on button state

Button State Handling:
Button Text	Automation Action
Booked	Skip
Book Class	Book
Join Waitlist	Join
Waitlisted	Skip
Core Learning:
Automation must respond to state, not force actions.

This function also:

Tracks metrics

Logs outcomes

Returns total processed count for validation

✅ Phase 4: Verification (verifybookings())
Most automation scripts stop after clicking.
This one verifies results.

What it verifies:
Navigates to “My Bookings”

Extracts booked class cards

Confirms expected day & time

Cross-checks count with bookings attempted

Why this matters:
Automation without verification is unreliable

This mimics real QA automation practices

Introduces post-action validation logic

🔁 Phase 5: Retry Logic (retry())
Login is not assumed to succeed on first attempt.

What this teaches:
Retry strategies

Function references vs function calls

Controlled failure handling

Defensive automation design

retry(login)
This ensures:

No infinite loops

Clear failure conditions

Predictable behavior

🧠 Key Automation Principles Demonstrated
Explicit waits over implicit assumptions

DOM traversal using XPath intelligently

State-driven UI interaction

Defensive coding with exceptions

Modular automation design

Verification as a first-class concern
