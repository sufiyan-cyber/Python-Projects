import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


ACCOUNT_EMAIL = "your_email"
ACCOUNT_PASSWORD = "your_password"
GYM_URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "Chrome_Profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

wait = WebDriverWait(driver, 20)


# ---------------- LOGIN ---------------- #

def login():
    try:
        login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
        login_button.click()

        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-input")))
        email_input.send_keys(ACCOUNT_EMAIL)

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password-input")))
        password_input.send_keys(ACCOUNT_PASSWORD)

        submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit-button")))
        submit_button.submit()

        logout_button = wait.until(
            EC.presence_of_element_located((By.ID, "logout-button"))
        )

        if logout_button.text == "Logout":
            print("You are logged in successfully")
            return True

    except TimeoutException:
        pass

    return False   # ✅ ALWAYS return something


# ---------------- BOOK A DAY ---------------- #

def bookaday():
    class_cards = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "div[id^='class-card-']")
        )
    )

    print("Class cards found:", len(class_cards))

    booked_count = 0
    waitlisted_count = 0
    alrady_bookedcount = 0

    for card in class_cards:
        day_group = card.find_element(
            By.XPATH,
            "ancestor::div[contains(@id, 'day-group-')]"
        )
        day_title = day_group.find_element(By.TAG_NAME, "h2").text

        time_text = card.find_element(
            By.CSS_SELECTOR, "p[id^='class-time-']"
        ).text

        if ("Tue" in day_title or "Thu" in day_title) and "6:00" in time_text:
            class_name = card.find_element(
                By.CSS_SELECTOR, "h3[id^='class-name-']"
            ).text

            button = card.find_element(By.TAG_NAME, "button")
            text = button.text.strip()   # ✅ small safety

            if text == "Booked":
                print(f"✓ Already Booked: {class_name} on {day_title}")
                alrady_bookedcount += 1
                continue

            elif text == "Join Waitlist":
                button.click()
                print(f"✓ waitlisted: {class_name} on {day_title}")
                waitlisted_count += 1
                continue

            elif text == "Waitlisted":
                print(f"✓ Already on a waitlist for: {class_name} on {day_title}")
                alrady_bookedcount += 1
                continue

            elif text == "Book Class":
                button.click()
                print(f"✓ just booked a class for: {class_name} on {day_title}")
                booked_count += 1
                continue

    print(f"class booked : {booked_count}")
    print(f"classes waitlisted : {waitlisted_count}")
    print(f"classes already booked : {alrady_bookedcount}")
    print(f"Total classes processed : {booked_count + waitlisted_count + alrady_bookedcount}")

    return booked_count + waitlisted_count + alrady_bookedcount


# ---------------- VERIFY BOOKINGS ---------------- #

def verifybookings(total_booked):
    my_bookings_link = driver.find_element(By.ID, "my-bookings-link")
    my_bookings_link.click()

    wait.until(EC.presence_of_element_located((By.ID, "my-bookings-page")))

    verified_count = 0
    all_cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")

    for card in all_cards:
        try:
            when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
            when_text = when_paragraph.text

            if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
                class_name = card.find_element(By.TAG_NAME, "h3").text
                print(f"✓ Verified: {class_name}")
                verified_count += 1

        except NoSuchElementException:
            pass

    print("\n--- VERIFICATION RESULT ---")
    print(f"Expected: {total_booked}")
    print(f"Found: {verified_count}")

    if total_booked == verified_count:
        print("✅ SUCCESS: All bookings verified!")
    else:
        print(f"❌ MISMATCH: Missing {total_booked - verified_count} bookings")


# ---------------- RETRY ---------------- #

def retry(func, retries=7):
    for i in range(retries):
        print(f"Login attempt {i+1}")
        if func():           # ✅ call once
            total = bookaday()
            verifybookings(total)
            return

    raise Exception("Exceeded login retries")


# ---------------- RUN ---------------- #

retry(login)   # ✅ pass function, not result
