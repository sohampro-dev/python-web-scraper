# -*- coding: utf-8 -*-
"""

@author: SOHAM
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

quotes_list = []
authors_list = []
page = 1

while True:
    url = f"http://quotes.toscrape.com/page/{page}/"

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("span", class_="text")
        authors = soup.find_all("small", class_="author")

        if not quotes:
            break

        for q in quotes:
            quotes_list.append(q.text)

        for a in authors:
            authors_list.append(a.text)

        print("Scraped page", page)

        page += 1

        time.sleep(2)

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        break

data = {"Quote": quotes_list, "Author": authors_list}

df = pd.DataFrame(data)
df.to_csv("quotes.csv", index=False)

print("Scraping finished")
