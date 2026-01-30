import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv
load_dotenv()
import random




# ================== CREDENTIALS ==================
USERNAME = os.getenv("INSTA_USERNAME")
ACCOUNT_PASSWORD = os.getenv("INSTA_ACCOUNT_PASSWORD")

if not USERNAME or not ACCOUNT_PASSWORD:
    raise ValueError("USERNAME / ACCOUNT_PASSWORD env vars not set")

INSTA_URL = "https://www.instagram.com/"

# ================== BROWSER SETUP ==================
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(INSTA_URL)

wait = WebDriverWait(driver, 20)

# ================== LOGIN ==================
username_input = wait.until(
    EC.element_to_be_clickable((By.NAME, "email"))
)
username_input.send_keys(USERNAME)

password_input = wait.until(
    EC.element_to_be_clickable((By.NAME, "pass"))
)
password_input.send_keys(ACCOUNT_PASSWORD)

login_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//div[@role='button' and contains(., 'Log in')]")
    )
)
login_button.click()

# ================== SAVE LOGIN INFO ==================
not_now = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//div[@role='button' and contains(., 'Not now')]")
    )
)
not_now.click()

# ================== OPTIONAL NOTIFICATIONS ==================
try:
    not_now_2 = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[@role='button' and contains(., 'Not Now')]")
        )
    )
    not_now_2.click()
except TimeoutException:
    pass

# ================== OPEN SEARCH (WORKING METHOD) ==================
wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

body = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
body.send_keys("/")

search_input = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Search']")
    )
)
search_input.send_keys("chef_pillai")
time.sleep(1)

# ================== OPEN PROFILE ==================
first_result = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='chef_pillai']/ancestor::a")
    )
)
first_result.click()

# ================== OPEN FOLLOWERS ==================
followers_link = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(@href, '/followers/')]")
    )
)
followers_link.click()

print("Reached followers list successfully.")

import time
from selenium.common.exceptions import StaleElementReferenceException

MAX_USERS = 10
processed = 0

# ... (rest of your imports and setup)
print("\n[INFO] Scanning for 'Follow' buttons...\n")

while processed < MAX_USERS:
    try:
        # UPDATED LOCATOR: Finds the text "Follow" and selects the clickable button wrapping it
        # This bypasses complex class names or specific container roles
        buttons = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//div[text()='Follow']/ancestor::button")
            )
        )
    except TimeoutException:
        print("[INFO] No 'Follow' buttons found. (List might be empty or all followed)")
        break

    found_actionable_button = False

    for btn in buttons:
        try:
            # Double check the text just to be safe
            if "Follow" in btn.text:
                processed += 1
                found_actionable_button = True

                print(f"[ACTION] Clicking Follow for user #{processed}")

                # Use JavaScript click (essential for Instagram)
                driver.execute_script("arguments[0].click();", btn)

                # Small pause to look human and let the UI update from "Follow" -> "Following"
                sleep_time = random.randint(20, 60)
                print(f"[WAIT] Sleeping for {sleep_time} seconds...")
                time.sleep(sleep_time)

                # Break to re-scan the DOM (prevents 'Stale Element' errors)
                break

        except StaleElementReferenceException:
            continue

    # If we looped through all buttons and found nothing to click (or clicked nothing), stop.
    if not found_actionable_button:
        print("[INFO] No more actionable 'Follow' buttons found.")
        break

print(f"\n[COMPLETE] Successfully followed {processed} users.")