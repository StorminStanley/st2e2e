from abc import ABCMeta, abstractmethod


class WebElement:

    __metaclass__ = ABCMeta

    def print_log(self, message):
        print "      web element: " + message

    @abstractmethod
    def get_relative(self, xpath):
        """ Get a WebElement by a relative xpath to the current element """
        pass

    @abstractmethod
    def type_value(self, value):
        """ Type value into the lement """
        pass

    @abstractmethod
    def click(self):
        """ Click on the element """
        pass

    @abstractmethod
    def get_text(self):
        """ Get text from the element """
        pass
