from selenium import webdriver
import requests
from bs4 import BeautifulSoup
my_url="https://sscnrs.streamlit.app/~/+/"
response = requests.get(my_url)
soup = BeautifulSoup(response.text)
soup.find(id="error_message")
# Result:
print(my_url)

