from selenium import webdriver
import requests
from bs4 import BeautifulSoup
my_url="https://sscnrs.streamlit.app/~/+/"
response = requests.get(my_url)
html = response.text
soup = BeautifulSoup(html, "html.parser")

soup.find(id="error_message")
# Result:
print(my_url)

