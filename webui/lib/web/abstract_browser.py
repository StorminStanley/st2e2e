from abc import ABCMeta, abstractmethod
from abstract_web_page import WebPage

class Browser:

    __metaclass__ = ABCMeta

    def print_log(self, message):
        print "      browser: " + message

    @abstractmethod
    def get_page(self, page_signature_xpath):
        """ Return the instance of the current WebPage, after waiting for the presence of the page signature """
        pass

    @abstractmethod
    def navigate_to_page(self, page_url, page_signature_xpath):
        """ Navigate to provided URL, and return the instance of the WebPage, which will wait for the provided page signatuire to appear """
        pass

    @abstractmethod
    def close(self):
        """ Close browser """
        pass

    @abstractmethod
    def get_native_driver(self):
        """ Returns the driver specific to implementation """
        pass
