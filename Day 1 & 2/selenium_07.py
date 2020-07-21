from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.maximize_window()

driver.get("https://qxf2.com/selenium-tutorial-main")

checkbox=driver.find_element_by_xpath("//input[@type='checkbox']")
checkbox.click()

time.sleep(5)

driver.close()