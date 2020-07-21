import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver=webdriver.Firefox()
driver.maximize_window()

driver.get('https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html')
element=driver.find_element_by_id('select-demo')

dropdown=Select(element)

time.sleep(3)

dropdown.select_by_value("Monday")

time.sleep(4)

print(len(dropdown.options))

all_options=dropdown.options

for  i in all_options:
    print(i.text)

driver.close()