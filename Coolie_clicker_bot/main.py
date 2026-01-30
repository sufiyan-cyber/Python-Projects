import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://ozh.github.io/cookieclicker/")

wait = WebDriverWait(driver, 20)

wait.until(EC.element_to_be_clickable((By.ID, "langSelect-EN"))).click()
big_cookie = wait.until(EC.element_to_be_clickable((By.ID, "bigCookie")))

start = time.time()

while True:
    # click cookie fast
    for _ in range(50):
        big_cookie.click()

    # every 5 seconds try buying
    if time.time() - start >= 5:
        products = driver.find_elements(By.CSS_SELECTOR, "#products .product")

        affordable = [
            p for p in products
            if "enabled" in p.get_attribute("class")
        ]

        if affordable:
            affordable[-1].click()

        start = time.time()
