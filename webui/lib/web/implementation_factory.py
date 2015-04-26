from selenium_browser import SeleniumFirefox
from selenium_wait_condition import SeleniumWaitForElementToBePresent
from selenium_wait_condition import SeleniumWaitForElementToBeClickable
from selenium_wait_condition import SeleniumWaitForElementToBeVisible


class BrowserType:
    FIREFOX = 1


class ImplementationFactory:

    def get_firefox(self):
        return SeleniumFirefox()

    def get_wait_for_element_to_be_present(self, xpath):
        return SeleniumWaitForElementToBePresent(xpath)

    def get_wait_for_element_to_be_clickable(self, xpath):
        return SeleniumWaitForElementToBeClickable(xpath)

    def get_wait_for_element_to_be_visible(self, xpath):
        return SeleniumWaitForElementToBeVisible(xpath)
