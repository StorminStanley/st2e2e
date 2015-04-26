from abc import ABCMeta, abstractmethod


class WebPage:

    __metaclass__ = ABCMeta

    LONG_WAIT = 180
    SHORT_WAIT = 5

    def print_log(self, message):
        print "      web page: " + message

    def __init__(self, browser, success_condition):
        self.browser = browser
        self.wait(success_condition)

    @abstractmethod
    def wait(self, condition):
        """ Waits for given condition to be true on the current page """
        pass

    @abstractmethod
    def get(self, xpath):
        """ Gets the element by provided xpath; should wait for element to appear on the page """
        pass

    @abstractmethod
    def get_count(self, xpath):
        """ Get number of elements with given xpath """
        pass

    @abstractmethod
    def confirm_alert(self):
        """ Allows to confirm and close alert dialog """
        pass
