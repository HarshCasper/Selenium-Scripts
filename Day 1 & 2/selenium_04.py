import time
from selenium import webdriver

driver=webdriver.Firefox()
driver.maximize_window()

driver.get('https://qxf2.com/selenium-tutorial-main')
toggle_element=driver.find_element_by_xpath("//button[@data-toggle='dropdown']")
toggle_element.click()

time.sleep(1)

driver.find_element_by_xpath("//a[text()='Male']").click()
time.sleep(5)

driver.close()