import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PROMISED_DOWN = 150
PROMISED_UP = 10

# ==============================
# CHROME OPTIONS (WORKING SETUP)
# ==============================
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# ------------------------------
# ❌ PROFILE-BASED SETUP (COMMENTED)
# This was explored to bypass X login,
# but causes Chrome–DevTools handshake
# issues on some Windows + Python setups.
# ------------------------------
# chrome_options.add_argument(
#     r"--user-data-dir=C:\Users\shuha\AppData\Local\Google\Chrome\User Data"
# )
# chrome_options.add_argument("--profile-directory=SeleniumProfile")
# chrome_options.add_argument("--no-first-run")


class TwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 30)
        self.down = None
        self.up = None

    # ==============================
    # SPEEDTEST (THIS WORKS)
    # ==============================
    def get_internet_speed(self):
        print("[INFO] Opening Speedtest...")
        self.driver.get("https://www.speedtest.net/")

        # Accept cookies if present
        try:
            self.wait.until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            ).click()
        except:
            pass

        # Start test (robust selector)
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.js-start-test"))
        ).click()

        print("[INFO] Running speed test...")
        time.sleep(45)

        self.down = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "span.result-data-value.download-speed")
            )
        ).text

        self.up = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "span.result-data-value.upload-speed")
            )
        ).text

        print(f"[RESULT] Download: {self.down} Mbps")
        print(f"[RESULT] Upload: {self.up} Mbps")

    # ==============================
    # TWITTER LOGIC (DOCUMENTED)
    # ==============================
    def send_tweet(self):
        """
        NOTE:
        Automated login to X (Twitter) using Selenium is blocked.
        Profile reuse was explored but caused instability on
        Windows + Python 3.12.

        This method is intentionally not executed.
        """

        # Example logic (not executed):
        # self.driver.get("https://x.com/home")
        # tweet_box = self.wait.until(
        #     EC.presence_of_element_located(
        #         (By.CSS_SELECTOR, 'div[data-testid="tweetTextarea_0"]')
        #     )
        # )
        #
        # tweet_text = (
        #     f"Internet Speed Test 🚀\n"
        #     f"Download: {self.down} Mbps\n"
        #     f"Upload: {self.up} Mbps\n"
        # )
        #
        # tweet_box.send_keys(tweet_text)
        #
        # self.wait.until(
        #     EC.element_to_be_clickable(
        #         (By.CSS_SELECTOR, 'button[data-testid="tweetButtonInline"]')
        #     )
        # ).click()
        pass


if __name__ == "__main__":
    bot = TwitterBot()
    bot.get_internet_speed()

