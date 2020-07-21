from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("http://qxf2.com/selenium-tutorial-main")

name=driver.find_element_by_xpath("//input[@id='name']")
name.send_keys('Harsh Bardhan Mishra')

email=driver.find_element_by_xpath("//input[@name='email']")
email.send_keys('erbeusgriffincasper@gmail.com')

phone=driver.find_element_by_id('phone')
phone.send_keys('+919799053844')

time.sleep(10)

driver.close()