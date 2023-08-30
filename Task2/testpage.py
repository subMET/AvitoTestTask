from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import time
import yaml

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)



class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])

class OperationsHelper(BasePage):

    def get_text(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator[1]
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception("Exception while click")
            return None
        logging.debug(f"Find text '{text}' in {element_name}")
        return text

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator[1]
        button = self.find_element(locator, time=3)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception while click")
            return False
        logging.debug(f"Click {element_name}")
        return True

    # Click
    def click_add_to_favorites_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_ADD_TO_FAVORITE"], description="add to favorites button")

    def click_to_favorites_page(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_TO_FAVORITES_PAGE"], description="redirect button to favorites page")

    # Get
    def get_ad_header_text(self):
        return self.get_text(TestSearchLocators.ids["LOCATOR_AD_HEADER"], description="header field on ad page")

    def get_first_ad_title_text(self):
        return self.get_text(TestSearchLocators.ids["LOCATOR_FIRST_AD_TITLE"], description="first ad title field")