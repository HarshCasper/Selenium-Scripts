from selenium import webdriver
import time

'''
Function Name: createPage()
Task: Initiatlizes the Webdriver and start the Webpage and verify it
Returns: driver
'''

def createPage():
    driver=webdriver.Firefox()
    driver.get('https://weathershopper.pythonanywhere.com/sunscreen')
    if driver.title == "The Best Sunscreens in the World!":
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
Function Name: extractPriceSPF50()
Task: Extracts out the Price for Products tagged with SPF/spf-50 and passes them to a List
Returns: list of prices for SPF-50 product
'''

def extractPriceSPF50(driver):
    productList=[]
    priceList=[]
    productList=driver.find_elements_by_xpath("//*[contains(text(),'SPF-50') or contains(text(),'spf-50')]/following-sibling::p") 
    for i in productList:
        priceText=i.text  
        priceEx=getPrice(priceText)
        priceList.append(priceEx)
    return priceList


'''
Function Name: extractPriceSPF30()
Task: Extracts out the Price for Products tagged with SPF/spf-30 and passes them to a List
Returns: list of prices for SPF-30 product
'''

def extractPriceSPF30(driver):
    productList=[]
    priceList=[]
    productList=driver.find_elements_by_xpath("//*[contains(text(),'SPF-30') or contains(text(),'spf-30')]/following-sibling::p") 
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
Function Name: addCartSPF50()
Task: Passes on the Least Expensive Product and click the Button to add it to Cart
Returns: None
'''

def addCartSPF50(leastExpensive, driver):
    le=str(leastExpensive)
    driver.find_element_by_xpath("//div[contains(@class,'col-4') and contains(.,'{}')]/descendant::button[text()='Add']".format(le)).click()
    createInterval(5)

'''
Function Name: addCartSPF30()
Task: Passes on the Least Expensive Product and click the Button to add it to Cart
Returns: None
'''

def addCartSPF30(leastExpensive, driver):
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
Function Name: getLeastExpensiveSPF50()
Task: Gets the least expensive SPF-50 Product and adds it to Cart
Returns: None
'''

def getLeastExpensiveSPF50(driver):
    spfProduct50=extractPriceSPF50(driver)
    spfLeast50=leastExpensive(spfProduct50)
    print("The Least Expensive SPF-50 Product is %r" %(spfLeast50))
    addCartSPF50(spfLeast50,driver)

'''
Function Name: getLeastExpensiveSPF30()
Task: Gets the least expensive SPF-30 Product and adds it to Cart
Returns: None
'''

def getLeastExpensiveSPF30(driver):
    spfProduct30=extractPriceSPF30(driver)
    spfLeast30=leastExpensive(spfProduct30)
    print("The Least Expensive SPF 30 Product is %r" %(spfLeast30))
    addCartSPF30(spfLeast30,driver)

# Driver Code

if __name__=="__main__":
    driver=createPage()
    getLeastExpensiveSPF50(driver)
    getLeastExpensiveSPF30(driver)
    goCart(driver)
    closePage(driver)
