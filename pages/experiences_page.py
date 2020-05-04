import time

from selenium.webdriver.common import actions

from common.common import *
from pages.a_base_page import basePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class experiencesPageLocators(object):
    ADD_DATE = (By.XPATH, "//span[text()='Date']/parent::button")
    SELECT_FROM = (
    By.XPATH, "//*[contains(text(),'May 2020')]/parent::div/following-sibling::table//*[contains(text(),'20')]")
    SELECT_TO = (
    By.XPATH, "//*[contains(text(),'August 2020')]/parent::div/following-sibling::table//*[contains(text(),'20')]")
    NEXT_BUTTON = (By.XPATH, "//div[@class='_13tn83am']//button[@class='_1dn9uje']")
    DATE_SEARCH = (By.XPATH, "//body/div/section/div/div/div/div/div/div/form/div/div/button/span[1]/span[1]")
    MENU_GUESTS = (By.XPATH, "//span[text()='Guests']")
    ADD_ADULTS = (By.XPATH, "//button[@aria-describedby='subtitle-label-filterItem-stepper-adults-0'][2]")
    ADD_CHILDREN = (By.XPATH, "//button[@aria-describedby='subtitle-label-filterItem-stepper-children-0'][2]")
    GUESTS_SAVE = (By.ID, "filter-panel-save-button")
    PRICE_FILTER = (By.ID, "menuItemButton-price_range")
    LEFT_SLIDER = (
    By.XPATH, "//body//div[@id='ExploreLayoutController']//div//div//div//div//div//div//div//button[1]//div[2]")
    RIGHT_SLIDER = (By.XPATH, "//button[2]//div[2]")
    DATE_FILTER = (By.XPATH, "//span[text()='Date']/parent::button")
    SAVE_PRICE = (By.ID, "filter-panel-save-button")

    ClICK_RESULT1 = (By.XPATH,
                     "//body[@class='with-new-header']/div/div/div/div/div[@class='_16grqhk']/main[@id='site-content']/div[@class='content-container']/div[@id='ExploreLayoutController']/div[@class='_e296pg']/div[@class='_1j0asm57']/div[@class='_twmmpk']/div[@class='_19qnt1y']/div[@class='_1gw6tte']/div[@class='_uhpzdny']/div/div[@class='_aov0j6']/div/div/div[2]/a[1]/div[1]/div[2]")
    CLICK_RESULT2 = (By.XPATH,
                     "//body/div/div/div/div/div/main[@id='site-content']/div/div[@id='ExploreLayoutController']/div/div/div/div/div/div/div/div/div/div/div[8]/a[1]/div[1]/div[2]")
    TEXT_RESULT1 = (By.XPATH, "//*[@id='ExploreLayoutController']/div/div[1]/div[2]/div/div[4]/div/div/div/div[2]/div/div[2]/a/div/div[2]/div[1]/div[2]")
    TEXT_RESULT3 = (By.XPATH, "//*[@id='ExploreLayoutController']/div/div[1]/div[2]/div/div[4]/div/div/div/div[2]/div/div[8]/a/div/div[2]/div[1]/div[2]")


class experiencesPage(basePage):
    def __init__(self, driver):
        super(experiencesPage, self).__init__(driver)

    def add_date(self, ):
        time.sleep(10)
        add_date = self.driver.find_element(*experiencesPageLocators.ADD_DATE)
        add_date.click()
        time.sleep(2)
        select_from = self.driver.find_element(*experiencesPageLocators.SELECT_FROM)
        select_from.click()
        next_button = self.driver.find_element(*experiencesPageLocators.NEXT_BUTTON)
        next_button.click()
        time.sleep(2)
        select_to = self.driver.find_element(*experiencesPageLocators.SELECT_TO)
        select_to.click()
        search_date = self.driver.find_element(*experiencesPageLocators.DATE_SEARCH)
        search_date.click()

    def select_guests(self):
        guests = self.driver.find_element(*experiencesPageLocators.MENU_GUESTS)
        guests.click()
        add_adults = self.driver.find_element(*experiencesPageLocators.ADD_ADULTS)
        add_adults.click()
        time.sleep(1)
        add_children = self.driver.find_element(*experiencesPageLocators.ADD_CHILDREN)
        add_children.click()
        guests_save = self.driver.find_element(*experiencesPageLocators.GUESTS_SAVE)
        guests_save.click()

    def price_filter(self):
        price_filter = self.driver.find_element(*experiencesPageLocators.PRICE_FILTER)
        price_filter.click()
        act = ActionChains(self.driver)
        sliderleft = self.driver.find_element(*experiencesPageLocators.LEFT_SLIDER)
        act.click_and_hold(sliderleft).move_by_offset(40, 0).release().perform()
        time.sleep(4)
        sliderright = self.driver.find_element(*experiencesPageLocators.RIGHT_SLIDER)
        act.click_and_hold(sliderright).move_by_offset(-120, 0).release().perform()
        save_price = self.driver.find_element(*experiencesPageLocators.SAVE_PRICE)
        save_price.click()

    def search_result1(self):
        time.sleep(5)
        txt_result1 = self.driver.find_element(*experiencesPageLocators.TEXT_RESULT1).text
        print(txt_result1)
        txt_result3 = self.driver.find_element(*experiencesPageLocators.TEXT_RESULT3).text
        print(txt_result3)
        result1 = self.driver.find_element(*experiencesPageLocators.ClICK_RESULT1)
        result1.click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        txt_in_result1 = self.driver.title
        print(txt_in_result1)
        self.driver.switch_to.window(self.driver.window_handles[0])

    def search_result2(self):
        result2 = self.driver.find_element(*experiencesPageLocators.CLICK_RESULT2)
        result2.click()
        self.driver.switch_to.window(self.driver.window_handles[2])
        txt_in_result3 = self.driver.title
        print(txt_in_result3)

    def assert_results(self,):
        assert self.search_result1.txt_result1 == self.search_result1.txt_in_result1, "RESULTS NOt MATCHING"
        assert self.search_result1.txt_result3 == self.search_result2.txt_in_result3, "RESULTS NOt MATCHING"

