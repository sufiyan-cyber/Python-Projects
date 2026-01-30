from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
#driver.get("https://www.amazon.in/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/ref=sr_1_1_sspa?crid=2L7AQUYQQH2RM&dib=eyJ2IjoiMSJ9.Zh0ArnH7y6ioO2avMXjZu-srQAvhOxgCtfPQWAIUJwDmIUk9HNbIIzMZPMwquZSP5PvTFO_ArvTXRpqsSjKryxkzkpQxNR4bknMk1ss5jeEFPRFSkxr1VLaDv4DIxhpahmbtQOGDpob6Hnz7tYpVzJXkvuWSzj42UNSLQ3ZCno04ueN2q32bTSbJtEXv_WafDe0NRtO4Pu0bIEEUdGfxHh3ms6olpAxIn9cR1dDgjHU.RHiv9Mr_hsCb0SXBrwPZ-VodK-SxyylfR9Tf9ukLyNs&dib_tag=se&keywords=instant%2Bpot&qid=1768646934&sprefix=instant%2Bp%2Caps%2C379&sr=8-1-spons&aref=q8Q6DM4EHe&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")

#price_rupees=driver.find_element(By.CLASS_NAME,"a-price-whole")
#print(price_rupees.text)

driver.get("https://www.python.org/")
'''
search_bar=driver.find_element(By.NAME,"q")
print(search_bar.get_attribute("placeholder"))

button=driver.find_element(By.ID,value="submit")
print(button.size)

the_link=driver.find_element(By.CSS_SELECTOR,value=".documentation-widget a")
print(the_link.text)

x_path_Way=driver.find_element(By.XPATH,'//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(x_path_Way.text)'''

time_element = driver.find_elements(By.TAG_NAME, "time")
dates=[]
# Get the full text content of the time element
for text in time_element:

    dates.append(text.text)

needed_dates = dates[5:]
print(needed_dates)

events_container = driver.find_element(
    By.XPATH,
    "//*[@id='content']//h2[normalize-space()='Upcoming Events']/following-sibling::ul[@class='menu']"
)

anchors = events_container.find_elements(By.TAG_NAME, "a")
text_data=[]
for a in anchors:
    text_data.append(a.text.strip())

print(text_data)

dict_events = {}

for idx, (date, text) in enumerate(zip(needed_dates, text_data)):
    dict_events[idx] = {
        "time": date,
        "name": text
    }

print(dict_events)



driver.quit()


