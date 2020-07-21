from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("https://qxf2.com/selenium-tutorial-main")

name=driver.find_element_by_xpath("//input[@id='name']")
name.send_keys('Harsh Bardhan Mishra')

email=driver.find_element_by_xpath("//input[@name='email']")
email.send_keys('erbeusgriffincasper@gmail.com')

phone=driver.find_element_by_id('phone')
phone.send_keys('+919799053844')

time.sleep(5)

toggle_element=driver.find_element_by_xpath("//button[@data-toggle='dropdown']")
toggle_element.click()

time.sleep(1)

driver.find_element_by_xpath("//a[text()='Male']").click()
time.sleep(5)

checkbox=driver.find_element_by_xpath("//input[@type='checkbox']")
checkbox.click()

time.sleep(5)

driver.close()
