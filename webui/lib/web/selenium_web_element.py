from selenium.webdriver.common.keys import Keys
from abstract_web_element import WebElement

class SeleniumWebElement(WebElement):

    def __init__(self, element):
        self.element = element

    def get_relative(self, xpath):
        self.print_log("Get sub-element " + xpath)
        relative = self.element.find_element_by_xpath(xpath)
        return SeleniumWebElement(relative)

    def type_value(self, value):
        self.print_log("Type value " + value)
        self.element.click()
        self.element.send_keys(value)

    def type_value_in_list(self, value):
        self.type_value(value)
        self.element.send_keys(Keys.RETURN)

    def click(self):
        self.print_log("Click")
        self.element.click()

    def get_text(self):
        text = self.element.text
        self.print_log("Get text " + text)
        return text
