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
        self.element.send_keys(value)

    def click(self):
        if(self.element.get_attribute('type') == 'submit'):
            self.print_log("Submit")
            self.element.send_keys(Keys.ENTER) # Selenium bug workaround
            self.element.submit()
        else:
            self.print_log("Click")
            self.element.click()

    def get_text(self):
        text = self.element.text
        self.print_log("Get text " + text)
        return text
