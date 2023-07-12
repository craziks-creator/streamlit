from selenium import webdriver
driver = webdriver.PhantomJS()
my_url="https://ssc.nic.in/"
driver.get(my_url)
p_element = driver.find_element_by_id(id_='error_message')
print(p_element.text)
# result:
'Yay! Supports javascript'
