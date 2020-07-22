from selenium import webdriver
import time

'''
Function Name: createPage()
Task: Initiative the Webdriver and start the Webpage and verify it
Returns: driver
'''

def createPage():
    driver=webdriver.Firefox()
    driver.get('https://weathershopper.pythonanywhere.com/moisturizer')
    if driver.title == "The Best Moisturizers in the World!":
        print("We have opened the Page sucessfully")
    else:
        print("There has been an error")

    return driver 

'''
Function Name: createInterval()
Task: Uses the time.sleep() function to halt the code for a few seconds as the Page Loads
Returns: None
'''

def createInterval(duration):
    time.sleep(duration)

'''
Function Name: closePage()
Task: Closes the Page after passing a Console Statement and waiting for five seconds
Returns: None
'''

def closePage(driver):
    print("Closing the Page now")
    createInterval(5)
    driver.quit()

'''
Function Name: getPrice()
Task: Get the Price Text and parses the Price using split() functions and List Slicing
Returns: price
'''

def getPrice(productText):
    price=productText.split("Price:")[-1]
    price=price.split("Rs.")[-1]
    price=price.split("\n")[0]
    price=int(price)
    return price

'''
Function Name: extractPriceAloe()
Task: Extracts out the Price for Products tagged with Aloe/aloe and passes them to a List
Returns: list of prices for aloevera product
'''

def extractPriceAloe(driver):
    productList=[]
    priceList=[]
    productList=driver.find_elements_by_xpath("//*[contains(text(),'Aloe') or contains(text(),'aloe')]/following-sibling::p") 
    for i in productList:
        priceText=i.text  
        priceEx=getPrice(priceText)
        priceList.append(priceEx)
    return priceList


'''
Function Name: extractPriceAlmond()
Task: Extracts out the Price for Products tagged with Almond/almond and passes them to a List
Returns: list of prices for Almond product
'''

def extractPriceAlmond(driver):
    productList=[]
    priceList=[]
    productList=driver.find_elements_by_xpath("//*[contains(text(),'Almond') or contains(text(),'almond')]/following-sibling::p") 
    for i in productList:
        priceText=i.text  
        priceEx=getPrice(priceText)
        priceList.append(priceEx)
    return priceList


'''
Function Name: leastExpensive()
Task: Get the least value among a list
Returns: Minimum Value
'''

def leastExpensive(listPrices):
    min=500
    for i in listPrices:
        if i < min:
            min=i
    return min

'''
Function Name: addCartAloe()
Task: Passes on the Least Expensive Product and click the Button to add it to Cart
Returns: None
'''

def addCartAloe(leastExpensive, driver):
    le=str(leastExpensive)
    driver.find_element_by_xpath("//div[contains(@class,'col-4') and contains(.,'{}')]/descendant::button[text()='Add']".format(le)).click()
    createInterval(5)

'''
Function Name: addCartAlmond()
Task: Passes on the Least Expensive Product and click the Button to add it to Cart
Returns: None
'''

def addCartAlmond(leastExpensive, driver):
    le=str(leastExpensive)
    driver.find_element_by_xpath("//div[contains(@class,'col-4') and contains(.,'{}')]/descendant::button[text()='Add']".format(le)).click()
    createInterval(5)

'''
Function Name: goCart()
Task: Clicks on Cart Button and goes to Checkout
Returns: None
'''

def goCart(driver):
    cart=driver.find_element_by_xpath("//button[contains(text(),'Cart')]")
    cart.click()
    createInterval(5)
    if(driver.title == "Cart Items"):
        print("Success. You did it!")
    else:
        print("Failure. You should try again. You can!")

'''
Function Name: getLeastExpensiveAloe()
Task: Gets the least expensive Aloevera Product and adds it to Cart
Returns: None
'''

def getLeastExpensiveAloe(driver):
    aloeProduct=extractPriceAloe(driver)
    aloeLeast=leastExpensive(aloeProduct)
    print("The Least Expensive Aloevera Product is %r" %(aloeLeast))
    addCartAloe(aloeLeast,driver)

'''
Function Name: getLeastExpensiveAlmond()
Task: Gets the least expensive Almond Product and adds it to Cart
Returns: None
'''

def getLeastExpensiveAlmond(driver):
    almondProduct=extractPriceAlmond(driver)
    almLeast=leastExpensive(almondProduct)
    print("The Least Expensive Almond Product is %r" %(almLeast))
    addCartAlmond(almLeast,driver)

# Driver Code

if __name__=="__main__":
    driver=createPage()
    getLeastExpensiveAloe(driver)
    getLeastExpensiveAlmond(driver)
    goCart(driver)
    closePage(driver)
