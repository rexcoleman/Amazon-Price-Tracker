from bs4 import BeautifulSoup
import requests
import smtplib
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
EMAIL_PORT  = os.environ.get("EMAIL_PORT")


url = "https://www.amazon.com/HOKA-ONE-Mach-Shoes-Color/dp/B09YTXS247/ref=sr_1_17?keywords=HOKA%2BONE%2BONE&sr=8-17&th=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url, headers=headers)
product = response.text
soup = BeautifulSoup(response.content,"lxml")
price = soup.find(class_="a-offscreen").getText()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)




if price_as_float < 150:
    print("true")
    message = f"Attencion! Achetez les HOKA chaussures. Price: ${price_as_float}.  Link: {url}"
    print(message)
    with smtplib.SMTP("smtp.gmail.com", port=int(EMAIL_PORT)) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Attencion! Achetez les HOKA Chaussures.\n\n{message}"
        )
        connection.close()
