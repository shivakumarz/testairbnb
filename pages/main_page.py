

import time
from common.common import *
from pages.a_base_page import basePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class mainPageLocators(object):
    MENU_EXPERIENCES = (By.XPATH, "//span[text()='Experiences']")
    SEARCH_BY_CITY = (By.ID, "bigsearch-query-attached-query")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")

    PAGE_SYNC = SEARCH_BUTTON

class mainPage(basePage):
    def __init__(self, driver):
        super(mainPage, self).__init__(driver)


    def select_experiences(self):
        experiences = self.driver.find_element(*mainPageLocators.MENU_EXPERIENCES)
        experiences.click()

    def search_experiences_by_city (self):
        place_to_search = "Sicily, Italy"
        city = self.driver.find_element(*mainPageLocators.SEARCH_BY_CITY)
        city.send_keys(place_to_search + Keys.ENTER)

        search = self.driver.find_element(*mainPageLocators.SEARCH_BUTTON)
        search.click()
