'''
My first Script to automate the behaviour on Weather App 

For: Qxf2

'''

from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get('https://weathershopper.pythonanywhere.com/')

# temperature=driver.find_element_by_xpath("//span[@id='temperature']")
temperature=driver.find_element_by_id('temperature')
print(temperature.text)

temp=int(temperature.text[:-2])

if temp < 19:
    driver.find_element_by_xpath("//button[text()='Buy moisturizers']").click()
    print("I am buying Moisturizers")

elif temp > 34:
    driver.find_element_by_xpath("//button[text()='Buy sunscreens']").click()
    print("I am buying Sunscreens now")

else: 
    print("You are all Cool.")
time.sleep(10)

driver.close()