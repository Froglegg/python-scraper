# Import libraries; make sure to run `pip install BeautifulSoup time shutil` and to run `python -m venv env` before beginning
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import shutil

# Set the URL you want to webscrape from
url = 'http://www.assurantsolutions.fr/actualites/page/5'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")
result = soup.find_all("div", class_="newsPageItems")
sourceFile= open('output.txt', 'w', encoding="utf-8")
print(result, file = sourceFile)
sourceFile.close()
shutil.move('output.txt', 'output-docs/fr_5.txt')
