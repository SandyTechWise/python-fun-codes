import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/page/1/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = []

tables = soup.find_all("div", attrs={"class": "quote"})

for table in tables:
    quote = table.find("span").text
    quotes.append(quote)

print(quotes)
