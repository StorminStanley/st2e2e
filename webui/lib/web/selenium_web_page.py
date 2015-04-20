from selenium.webdriver.support.ui import WebDriverWait
from abstract_web_page import WebPage
from selenium_web_element import SeleniumWebElement
from selenium_wait_condition import SeleniumWaitForElementToBePresent


class SeleniumWebPage(WebPage):

    def __init__(self, browser, page_signature_xpath):
        WebPage.__init__(self, browser, SeleniumWaitForElementToBePresent(page_signature_xpath))

    def wait(self, condition):
        self.print_log(condition.getLabel())
        found = WebDriverWait(self.browser.get_native_driver(), WebPage.LONG_WAIT).until(condition.getObject())
        return SeleniumWebElement(found)

    def get(self, xpath):
        return self.wait(SeleniumWaitForElementToBePresent(xpath))
