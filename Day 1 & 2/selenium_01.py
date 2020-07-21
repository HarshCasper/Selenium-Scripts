'''
Navigating to a URL using Selenium

The Main Objective of this Exercise is to:

1. Importing Selenium and the Webdriver
2. Opening the Browser Window
3. Use the get() function to open a URL on the Firefox Window
4. Check if the title of Page is given correct

'''

from selenium import webdriver
browser=webdriver.Firefox()
browser.get("https://centralperk.social/")

if (browser.title == "Login Page"):
    print("Successfully Validated")
else:
    print("Could not open the Page")

browser.quit()