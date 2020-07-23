import time
from selenium import webdriver
import string
import random

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

'''
Function Name: getPayment()
Task: Clicks the Payment Option and opens up the IFrame
Returns: None
'''

def getPayment(driver):
    submitBttn=driver.find_element_by_xpath("//button[contains(@type,'submit')]")
    submitBttn.click()
    print("We clicked the Payment Option")
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

'''
Function Name: random_string()
Task: Generates a Random String given the length
Returns: A Random String given the length
'''

def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


'''
Function Name: get_one_random_domain()
Task: Generates a Random Domain to be used with the E-Mail Service
Returns: A Random Domain
'''

def get_one_random_domain():  
    domains = ["hotmail.com", "gmail.com", "aol.com", "mail.com" , "protonmail.com", "yahoo.com"]
    return random.choice(domains)

'''
Function Name: generate_random_email()
Task: Generates a Random E-Mail
Returns: A Random E-Mail 
'''

def generate_random_email():
    one_name = str(random_string(5))
    one_domain = str(get_one_random_domain())         
    email = one_name  + "@" + one_domain
    return email

'''
Function Name: get_number()
Task: Generates a Number given the length
Returns: A Random Number
'''

def get_number(length):
    sample_letters = '0123456789'
    result_str = ''.join((random.choice(sample_letters) for i in range(length)))
    return result_str


'''
Function Name: fillDetails()
Task: Fills in all the Option for the Purchase Form
Returns: None
'''

def fillDetails(driver):
    email = driver.find_element_by_xpath("//input[contains(@type,'email')]")
    email.send_keys(generate_random_email())
    card = driver.find_element_by_xpath("//input[contains(@placeholder,'Card number')]")
    card.send_keys('4242424242424242')
    year = driver.find_element_by_xpath("//input[contains(@placeholder,'MM / YY')]")
    year.send_keys('11/25')
    cvv=driver.find_element_by_xpath("//input[contains(@maxlength,'4')]")
    cvv.send_keys('1234')
    zipCode=driver.find_element_by_xpath("//input[contains(@placeholder,'ZIP Code')]")
    zipCode.send_keys(get_number(6))
    remMe=driver.find_element_by_xpath("//label[contains(@class,'Fieldset-label')]")
    remMe.click()
    phoneNumber=driver.find_element_by_xpath("//input[contains(@autocomplete,'mobile tel')]")
    phoneNumber.send_keys(get_number(10))
    submitButton=driver.find_element_by_xpath("//button[contains(@type,'submit')]")
    submitButton.click()
    createInterval(5)
    driver.switch_to.frame(0)
    createInterval(5)

# driver Code

if __name__=="__main__":
    driver=createPage()
    getLeastExpensiveAloe(driver)
    getLeastExpensiveAlmond(driver)
    goCart(driver)
    getPayment(driver)
    fillDetails(driver)
    closePage(driver)
