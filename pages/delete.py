import time

import driver as driver
import location as location
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="//Users//shiva//Downloads//chromedriver 4")
driver.maximize_window()
driver.get("https://www.airbnb.co.in/")

time.sleep(2)


def select_exp():
    driver.find_element_by_xpath("//span[@class='_t8o8dg'][contains(text(),'Experiences')]").click()
    return


select_exp()


def select_location(location):
    edit_field = driver.find_element(By.XPATH, "//input[@placeholder='Add city, landmark, or address']")
    edit_field.clear()
    edit_field.send_keys(location)
    time.sleep(2)
    options = driver.find_elements(By.XPATH, "//li[@role='option']/div/div")
    for option in options:
        if option.text == location:
            option.click()
            time.sleep(2)
            return True
    if edit_field.text == location:
        return True
    return False


select_location("Sicily, Italy")


def clickSearch():
    search = driver.find_element_by_xpath(
        "//body/div/div/div/div/div/div/div/div/div/div/div/div/form/div/div/button/span[1]/span[1]")
    search.click()
    return
    time.sleep(3)


clickSearch()


def dateSelect():
    time.sleep(2)
    driver.find_element_by_xpath("//button[contains(text(),'Add date')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[contains(text(),'May 2020')]/parent::div/following-sibling::table//*[contains(text(),'20')]").click()

    datepickerr = driver.find_element_by_xpath("//div[@class='_13tn83am']//button[@class='_1dn9uje']")
    datepickerr.click()
    time.sleep(2)

    driver.find_element_by_xpath("//*[contains(text(),'August 2020')]/parent::div/following-sibling::table//*[contains(text(),'20')]").click()
    time.sleep(2)
    # for i in range(0, 3):
    #     ActionChains(driver).click(datepickerr).perform()
    # time.sleep(2)
    # driver.find_element_by_xpath(
    #     "//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div[2]//div[1]//table[1]//tbody[1]//tr[4]//td[3]//div[1]//div[1]//div[1]").click()
    driver.find_element_by_xpath("//body/div/section/div/div/div/div/div/div/form/div/div/button/span[1]/span[1]").click()


dateSelect()


def select_adult_child():
    time.sleep(2)
    guests = driver.find_element_by_xpath("//div[@id='menuItemButton-guest_picker']//button")
    guests.click()
    time.sleep(2)
    for x in range(0, 1):
        driver.find_element(By.XPATH,
                            "//body//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div[1]//div[1]//div[2]//button[2]//*[local-name()='svg']").click()
        time.sleep(1)
    for x in range(0, 1):
        driver.find_element(By.XPATH,
                            "//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div[2]//div[1]//div[2]//button[2]//*[local-name()='svg']").click()
        time.sleep(1)
    driver.find_element_by_xpath("//button[@id='filter-panel-save-button']").click()
    print(guests.text)

    # if str(guest).strip() == str(adults + children + infants) + " guests":
    #     return True
    # return False


select_adult_child()


def price_filter():
    driver.find_element_by_id("menuItemButton-price_range").click()
    act = ActionChains(driver)
    sliderleft = driver.find_element_by_xpath(
        "//body//div[@id='ExploreLayoutController']//div//div//div//div//div//div//div//button[1]//div[2]")
    act.click_and_hold(sliderleft).move_by_offset(40, 0).release().perform()

    time.sleep(4)

    sliderright = driver.find_element_by_xpath("//button[2]//div[2]")
    act.click_and_hold(sliderright).move_by_offset(-120, 0).release().perform()
    driver.find_element_by_id("filter-panel-save-button").click()


price_filter()


def select_result1():
    result1 = driver.find_element_by_xpath(
        "//body[@class='with-new-header']/div/div/div/div/div[@class='_16grqhk']/main[@id='site-content']/div[@class='content-container']/div[@id='ExploreLayoutController']/div[@class='_e296pg']/div[@class='_1j0asm57']/div[@class='_twmmpk']/div[@class='_19qnt1y']/div[@class='_1gw6tte']/div[@class='_uhpzdny']/div/div[@class='_aov0j6']/div/div/div[2]/a[1]/div[1]/div[2]")
    result1.click()


select_result1()

# driver.switch_to.window(driver.window_handles[1])


def select_result2():
    result2 = driver.find_element_by_xpath(
        "//body/div/div/div/div/div/main[@id='site-content']/div/div[@id='ExploreLayoutController']/div/div/div/div/div/div/div/div/div/div/div[8]/a[1]/div[1]/div[2]")
    result2.click()


driver.close()
