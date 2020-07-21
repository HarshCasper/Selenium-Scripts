from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get('http://cloudportal.sathyabama.ac.in/sist_results_may_2020/login.php')

name=driver.find_element_by_id('regno')
name.send_keys('38110196')

dob=driver.find_element_by_id('dob')
dob.send_keys('15/11/2000')

button=driver.find_element_by_id('btnLogin')
button.click()

time.sleep(20)

driver.close()