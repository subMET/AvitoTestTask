from testpage import OperationsHelper
import logging

def test_step1(browser, favorite_url):
    logging.info("Test1 Starting")
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    header = test_page.get_ad_header_text()
    test_page.click_add_to_favorites_button()
    test_page.go_to_site(favorite_url)
    test_page.get_first_ad_title_text()
    assert test_page.get_first_ad_title_text() == header
