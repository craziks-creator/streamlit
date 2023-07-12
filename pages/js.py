from selenium import webdriver
import requests
from bs4 import BeautifulSoup
my_url="https://ssc.nic.in/"
response = requests.get(my_url)
soup = BeautifulSoup(response.text)
soup.find(id="error_message")
# Result:
'Yay! Supports javascript'

driver = webdriver.Chrome()
driver.get(my_url)
p_element = driver.find_element_by_id(id_='error_message')
print(p_element.text)
# result:
'Yay! Supports javascript'
