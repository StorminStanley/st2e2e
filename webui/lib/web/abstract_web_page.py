from abc import ABCMeta, abstractmethod
from abstract_wait_condition import WaitForElementToBePresent

class WebPage:

    __metaclass__ = ABCMeta

    def print_log(self, message):
        print "      web page: " + message

    def __init__(self, browser, success_condition):
        self.browser = browser
        self.wait(success_condition)

    @abstractmethod
    def wait(self, condition):
        """ Waits for given WebCondition to be true on the current page """
        pass
