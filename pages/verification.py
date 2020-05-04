import time

import driver as driver
import location as location
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="//Users//shiva//Downloads//chromedriver 4")
driver.maximize_window()
# driver.get("https://www.airbnb.co.in/experiences/223963?location=Sicily%2C%20Italy&checkin=2020-05-19&checkout=2020-07-23&adults=1&children=1&source=p2")
driver.get("https://www.airbnb.co.in/s/Sicily--Italy/experiences?tab_id=experience_tab&refinement_paths%5B%5D=%2Fexperiences&place_id=ChIJs1lT0GhiEBMRUH22ZykECwE&source=structured_search_input_header&search_type=search_query&query=Sicily%2C%20Italy&adults=1&children=1&price_min=188&price_max=3426&checkin=2020-05-19&checkout=2020-07-23")

text1 = driver.find_element_by_xpath("//div[contains(text(),'The most beautiful sea spots')]").text

print(text1,"printing result 1")
time.sleep(5)
text2 = driver.find_element_by_xpath("//div[contains(text(),'Local Markets and Street Food Tour')]").text
print(text2,"printing result 2")

result1 = driver.find_element_by_xpath(
    "//body[@class='with-new-header']/div/div/div/div/div[@class='_16grqhk']/main[@id='site-content']/div[@class='content-container']/div[@id='ExploreLayoutController']/div[@class='_e296pg']/div[@class='_1j0asm57']/div[@class='_twmmpk']/div[@class='_19qnt1y']/div[@class='_1gw6tte']/div[@class='_uhpzdny']/div/div[@class='_aov0j6']/div/div/div[2]/a[1]/div[1]/div[2]")
result1.click()

driver.switch_to.window(driver.window_handles[1])

text11 = driver.find_element_by_xpath("//section[@id='Section5']//section//div//div//div//div//div[contains(text(),'The most beautiful sea spots')]").text
print(text11,"printing result 1")
driver.close()

# text1 = driver.find_element_by_xpath("//div[contains(text(),'Paused until 28 May. To protect the health of our')]").text
# print(text1)
driver.switch_to.window(driver.window_handles[0])

result2 = driver.find_element_by_xpath("//body/div/div/div/div/div/main[@id='site-content']/div/div[@id='ExploreLayoutController']/div/div/div/div/div/div/div/div/div/div/div[8]/a[1]/div[1]/div[2]")
result2.click()
time.sleep(5)

text22 = driver.find_element_by_xpath("//div[@class='_1r93ihzp']").text
print(text22)
# assert text1 == text11, "value not matching"
# assert text2 == text22, "value not matching"
