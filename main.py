from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# creating driver
driver = Driver(uc=True, headless=True) 

# dict containing the food item we want to scrape and the URL we need to go to 
weis = {"beef": "https://www.weismarkets.com/shop/product/weis-fresh-from-the-farm-90-lean-ground-beef/147376",
        "milk": "https://www.weismarkets.com/shop/product/weis-quality-whole-milk-grade-a/131758",
        "eggs": "https://www.weismarkets.com/shop/product/weis-quality-eggs-grade-a-large/131783"}

wegmans = {"beef": "https://shop.wegmans.com/product/3285/wegmans-organic-grass-fed-ground-beef-93percent-lean7percent-fat",
           "milk": "https://shop.wegmans.com/product/19907/wegmans-milk-vitamin-d-whole", 
           "eggs": "https://shop.wegmans.com/product/3464/wegmans-grade-aa-large-eggs-18-count"}
# tag for wegmans
#<span class="css-1t6g1xs">$2.99</span>

# looping through weis urls 
print("Weis - ", end='')
maxAttempts = 3
for food, url in weis.items():
    attempt = 1
    while attempt <= maxAttempts:
        try:
            driver.get(url)
            # Had to add this code because if I didn't wait, the program was 
            price_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "mct-price"))
            )
            price = price_element.get_attribute("price-string")
            print(f"{food}: ${price}   ", end='')
            break;
        except TimeoutException:
            #print(f"Timeout occured, trying again (Attempt: {attempt})")
            attempt += 1
    if attempt == 4:
        print("Reached max attempts")
        driver.quit()
print()

# Loops through wegmans url
print("Wegmans - ", end='')
for food, url in wegmans.items():
    attempt = 1
    # Trys to scrape from url n amount of times
    while attempt <= maxAttempts:
        try:
            driver.get(url)
            # Had to add this code because if I didn't wait, the program was 
            price_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "css-1t6g1xs"))
            )
            print(f"{food}: {price_element.text}   ", end='')
            break;
        except TimeoutException:
            #print(f"Timeout occured, trying again (Attempt: {attempt})")
            attempt += 1
    if attempt == 4:
        print("Reached max attempts")
        driver.quit()
print()

driver.quit()


# Use arrays pertaining to a specific grocery store which contains URLS for each item we want 
#              beeef      milk       eggs
# weis : 
# wegmans : 