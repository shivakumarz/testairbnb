from common.config import *
from common.common import airbnb_setup
from pages.main_page import mainPage
from pages.experiences_page import experiencesPage


class test_scenarios():
    def setUp(self):
        self.driver = airbnb_setup(browser="Chrome")  # Firefox

    def test_airbnb_scenario(self):
        """Select experiences, add guests, filter on price"""
        self.main_page_object = mainPage(self.driver)
        self.main_page_object.select_experiences()
        self.main_page_object.search_experiences_by_city()

        self.experience_page_object = experiencesPage(self.driver)
        self.experience_page_object.add_date()
        self.experience_page_object.select_guests()

        self.experience_page_object.price_filter()
        self.experience_page_object.search_result1()
        self.experience_page_object.search_result2()

        # self.experience_page_object.assert_results()

    def tearDown(self):
        self.driver.quit()
