import time
from selenium import webdriver
import os
os.system('sudo apt-get install -y chromium-browser')
url = "https://sscnrs.streamlit.app/~/+/"
driver = webdriver.Chrome()
driver.get(url)

while True:
    get_title = driver.title
    print(get_title)
    time.sleep(30)  # Pause for 30 seconds before repeating the loop
