import logging
import yaml
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = testdata["ad"]

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                            message=f"Can't find element by locator {locator}")
        except:
            logging.exception("Find element exception")
            element = None
        return element


    def go_to_site(self, url=None):
        try:
            if url == None:
                start_browsing = self.driver.get(self.base_url)
            else:
                start_browsing = self.driver.get(url)
        except:
            logging.exception("Exception while open site.")
            start_browsing = None
        return start_browsing