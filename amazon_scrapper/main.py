import requests
import os
import smtplib
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()

MY_EMAIL = os.environ["MY_EMAIL"]
recipient_email=os.environ["recipient_email"]
MY_PASSWORD = os.environ["MY_PASSWORD"]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response=requests.get("https://www.amazon.in/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/ref=sr_1_1_sspa?crid=2L7AQUYQQH2RM&dib=eyJ2IjoiMSJ9.Zh0ArnH7y6ioO2avMXjZu-srQAvhOxgCtfPQWAIUJwDmIUk9HNbIIzMZPMwquZSPewjvRztSefwP0lWsMHw0i2mTaW8MRf2EcHgl3Pwfg4Hjo6EsE-xwn7K8oxCLK5EdzznRwowW6Xqw_cVqSizRfcl7pv7X09VI37-eqtW-ngqx04vmjKh2g1nKbevh74CCrrvWHEbwUyxfpDofuFZRcCayOnC5lwh__jlTjun8MXQ.5bjSO0Mthzx17mybJE57toOAMFNpfeAFgXH40LwVtRg&dib_tag=se&keywords=instant%2Bpot&qid=1768575080&sprefix=instant%2Bp%2Caps%2C379&sr=8-1-spons&aref=q8Q6DM4EHe&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1",headers=headers)
print(response.status_code)

URL="https://www.amazon.in/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/ref=sr_1_1_sspa?crid=2L7AQUYQQH2RM&dib=eyJ2IjoiMSJ9.Zh0ArnH7y6ioO2avMXjZu-srQAvhOxgCtfPQWAIUJwDmIUk9HNbIIzMZPMwquZSPewjvRztSefwP0lWsMHw0i2mTaW8MRf2EcHgl3Pwfg4Hjo6EsE-xwn7K8oxCLK5EdzznRwowW6Xqw_cVqSizRfcl7pv7X09VI37-eqtW-ngqx04vmjKh2g1nKbevh74CCrrvWHEbwUyxfpDofuFZRcCayOnC5lwh__jlTjun8MXQ.5bjSO0Mthzx17mybJE57toOAMFNpfeAFgXH40LwVtRg&dib_tag=se&keywords=instant%2Bpot&qid=1768575080&sprefix=instant%2Bp%2Caps%2C379&sr=8-1-spons&aref=q8Q6DM4EHe&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
soup=BeautifulSoup(response.text,"html.parser")
price_Tags=soup.find(name="span",class_="a-price-whole")
actual_price=price_Tags.text

clean_data=actual_price.replace(",","").replace(".","")
int_data=int(clean_data)




if int_data<=8500:

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=recipient_email,
            msg=f"Subject:Price Alert!!!\n\nprice has crossed the link to product  is {URL} "
        )

