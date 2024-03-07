import requests
import smtplib
from bs4 import BeautifulSoup

LOWEST_PRICE = 1700
ITEM_URL = "https://www.amazon.es/ASUS-ROG-Strix-GeForce-4090/dp/B0BHD6N2CK/ref=sr_1_3?crid=2R1YLIKFG9MYB&dib=eyJ2IjoiMSJ9.l-WSMbAI82pNW30n3w097B_cICglsKCjxCwBVXNubZ231llcWh7nNwu1Ko30ZUYFuSiftk_FxuvXBzqeCu3VPcx9mY7VeuB8XJk5MU2dQQaAjtpj_pGNgk1ivE1IDF8xsX8nL6RLjDVlYcE0SQ3VXawiqwn8lnL1KpOyHjZUiivjlDKk45Ss1ckHWfG3DXmgWj41aUaH_54bdpRfPMfWmPPEa1utLh5uGQnzN3Po55aXmRwfGY_HYuaPwDb4HB_JjC_qS4YJ2AlPCT8OeBJp2zqvCqVEqGxWJ2gu8cR7LYY.BNzPsxKKBVGA1jOO8ppBIyOYxWsq5wJETr7K6wiirwU&dib_tag=se&keywords=4090+ti&qid=1709808350&sprefix=4090%2Caps%2C320&sr=8-3"
headers = {
    "user": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "lan": "es-ES,es;q=0.9,en;q=0.8"
}
response = requests.get(ITEM_URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

price = soup.find("span", class_="a-price-whole").getText()
actual_price = int(price.split(",")[0])
if actual_price < LOWEST_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(f"{your email}", f"{your password}")
        connection.sendmail(from_addr=f"{your email}", to_addrs=f"{your email}", msg=f"Subject:Lower price on Amazon\n\nThe price on the product you are tracking has lowered. The price is now {actual_price} euros.")
