from abc import ABCMeta
from selenium import webdriver
from abstract_browser import Browser
from selenium_web_page import SeleniumWebPage
from abstract_web_page import WebPage

LOG_PREFIX = "  browser: "


class SeleniumBrowser(Browser):

    __metaclass__ = ABCMeta

    def __init__(self, webdriver_instance):
        self.driver = webdriver_instance
        self.driver.implicitly_wait(WebPage.SHORT_WAIT)

    def navigate_to_page(self, page_url, page_signature_xpath):
        self.print_log("Navigating to %s" % page_url)
        self.driver.get(page_url)
        page = SeleniumWebPage(self, page_signature_xpath)
        return page

    def get_page(self, page_signature_xpath):
        page = SeleniumWebPage(self, page_signature_xpath)
        return page

    def close(self):
        self.driver.quit()

    def get_cookie(self, name):
        return self.driver.get_cookie(name)

    def get_native_driver(self):
        return self.driver


class SeleniumFirefox(SeleniumBrowser):

    def __init__(self):
        SeleniumBrowser.__init__(self, webdriver.Firefox())
        self.print_log("Running on Firefox")
