from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
last_name  = driver.find_element(By.NAME, "lName")
email      = driver.find_element(By.NAME, "email")


first_name.send_keys("sufiyan",Keys.ENTER)
last_name.send_keys("khan",Keys.ENTER)
email.send_keys("sk@gmail.com",Keys.ENTER)
