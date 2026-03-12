# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 11:47:51 2026

@author: SOHAM
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as tk
from tkinter import messagebox

def scrape():
    url = entry.get()

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("span", class_="text")
        authors = soup.find_all("small", class_="author")

        quote_list = []
        author_list = []

        for q in quotes:
            quote_list.append(q.text)

        for a in authors:
            author_list.append(a.text)

        data = {
            "Quote": quote_list,
            "Author": author_list
        }

        df = pd.DataFrame(data)
        df.to_csv("quotes_gui.csv", index=False)

        messagebox.showinfo("Success", "Data saved to CSV")

    except:
        messagebox.showerror("Error", "Scraping failed")

window = tk.Tk()
window.title("Web Scraper Tool")
window.geometry("400x200")

label = tk.Label(window, text="Enter Website URL")
label.pack(pady=10)

entry = tk.Entry(window, width=40)
entry.pack()

button = tk.Button(window, text="Scrape Data", command=scrape)
button.pack(pady=20)

window.mainloop()