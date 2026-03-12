# 🕸️ Python Web Scraper Tool

## 📌 Project Overview

This project is a **Python Web Scraper** that extracts quotes and author names from a website and saves the data into a CSV file.

The scraper automatically navigates through multiple pages, handles request headers, adds delays to avoid blocking, and stores extracted data in a structured format.

This project demonstrates **web scraping, automation, data processing, and GUI development using Python**.

---

## 🚀 Features

- Extract quotes and author names from webpages
- Scrape multiple pages automatically
- Add HTTP headers to simulate a real browser
- Add delay between requests to avoid blocking
- Error handling for network issues
- Save extracted data into CSV format
- Simple GUI interface for user interaction

---

## 🧰 Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- Tkinter

---

## 📁 Project Structure
```
python-web-scraper
│
├── src
│ ├── scraper.py
│ └── scraper_gui.py
│
├── data
│ └── quotes.csv
│
├── screenshots
│ ├── gui_interface.png
│ └── output_file.png
│
├── requirements.txt
├── README.md
└── .gitignore
```


---

## ⚙️ Installation

### 1. Clone the repository
git clone https://github.com/sohampro-dev/python-web-scraper.git

### 2. Go to the project directory
cd python-web-scraper


### 3. Install required libraries
pip install -r requirements.txt


---

## 📦 Requirements

- requests
- beautifulsoup4
- pandas


---

## ▶️ Running the Project

# Run command-line scraper:
python scraper.py


# Run GUI version:
python scraper_gui.py


---

## 🧠 How the Scraper Works

1. Send an HTTP request to the website  
2. Download the HTML page  
3. Parse the HTML using BeautifulSoup  
4. Extract quotes and author names  
5. Move to the next page automatically  
6. Store the extracted data  
7. Save the results to a CSV file  

---

## 💻 Example Code Snippet

```python
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

The extracted data is saved in: quotes.csv
```

## 💻 GUI Interface

- The GUI tool allows users to:
- Enter a website URL
- Click a button to start scraping
- Automatically export results
- The interface is built using Tkinter.

## 🛡 Error Handling

The program uses try-except blocks to handle errors such as:

- Network errors
- Invalid URLs
- Request failures

```python
try:
    response = requests.get(url)
except requests.exceptions.RequestException:
    print("Request failed")
```

# ⚖ Ethical Web Scraping

When scraping websites:

- Respect website terms of service
- Avoid sending too many requests
- Add delays between requests
- Do not scrape restricted data

# 🔮 Future Improvements

Possible improvements:

- Export data to Excel
- Add rotating user agents
- Add proxy support
- Create an advanced GUI dashboard
- Schedule automatic scraping

# 👨‍💻 Author

Soham Dey

Python Developer | Automation | Web Scraping

# ⭐ Support

If you found this project helpful, consider starring the repository.
