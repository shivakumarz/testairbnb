from selenium import webdriver
from common.config import *

def airbnb_setup (browser="Chrome", url_to_open=site_url):
    if browser == "Firefox":
        driver = webdriver.Firefox()
    elif browser == "Chrome":
        driver = webdriver.Chrome(executable_path="//Users//shiva//Downloads//chromedriver 4")
    driver.implicitly_wait(30) # seconds
    driver.maximize_window()
    driver.get(url_to_open)

    return driver
