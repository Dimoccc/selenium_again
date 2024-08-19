import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  

def test_language(browser):
    time.sleep(5)
    browser.implicitly_wait(5)
    try:
            browser.find_element('xpath', "//button[@class = 'btn btn-lg btn-wishlist']")
            print("Ok")
    except:
            print("button - 'btn btn-lg btn-wishlist' NO FOUND")
    
    assert browser.find_element('xpath', "//button[@class = 'btn btn-lg btn-wishlist']"), 'Not found'