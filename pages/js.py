from selenium import webdriver
import requests
from bs4 import BeautifulSoup
my_url="https://sscnrs.streamlit.app/~/+/"
response = requests.get(my_url)
html = requests.urlopen(my_url, context=ctx).read()
soup = BeautifulSoup( ..., "html.parser" )
soup.find(id="error_message")
# Result:
print(my_url)

