from abstract_wait_condition import WaitForElementToBePresent
from abstract_wait_condition import WaitForElementToBeClickable
from abstract_wait_condition import WaitForElementToBeVisible
from abstract_wait_condition import WaitForAlert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SeleniumWaitForElementToBePresent(WaitForElementToBePresent):

    def __init__(self, xpath):
        WaitForElementToBePresent.__init__(self, xpath)

    def getObject(self):
        return EC.presence_of_element_located((By.XPATH, self.xpath))


class SeleniumWaitForElementToBeClickable(WaitForElementToBeClickable):

    def __init__(self, xpath):
        WaitForElementToBeClickable.__init__(self, xpath)

    def getObject(self):
        return EC.element_to_be_clickable((By.XPATH, self.xpath))

class SeleniumWaitForElementToBeVisible(WaitForElementToBeVisible):

    def __init__(self, xpath):
        WaitForElementToBeVisible.__init__(self, xpath)

    def getObject(self):
        return EC.visibility_of_element_located((By.XPATH, self.xpath))

class SeleniumWaitForAlert(WaitForAlert):

    def __init__(self):
        WaitForAlert.__init__(self, '')

    def getObject(self):
        return EC.alert_is_present()
