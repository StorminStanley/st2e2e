import time
from selenium.webdriver.support.ui import WebDriverWait
from abstract_web_page import WebPage
from selenium_web_element import SeleniumWebElement
from selenium_wait_condition import SeleniumWaitForElementToBePresent
from selenium_wait_condition import SeleniumWaitForAlert


class SeleniumWebPage(WebPage):

    def __init__(self, browser, page_signature_xpath):
        WebPage.__init__(self, browser, SeleniumWaitForElementToBePresent(page_signature_xpath))

    def wait(self, condition):
        self.print_log(condition.getLabel())
        found = WebDriverWait(self.browser.get_native_driver(), WebPage.LONG_WAIT).until(condition.getObject())
        return SeleniumWebElement(found)

    def get(self, xpath):
        return self.wait(SeleniumWaitForElementToBePresent(xpath))

    def get_count(self, xpath):
        return len(self.browser.get_native_driver().find_elements_by_xpath(xpath))

    def confirm_alert(self):
        self.wait(SeleniumWaitForAlert())
        alert = self.browser.get_native_driver().switch_to_alert()
        alert.accept()
        time.sleep(WebPage.SHORT_WAIT)
        self.browser.get_native_driver().switch_to_default_content()
