from abc import ABCMeta, abstractmethod


class WaitCondition(object):

    __metaclass__ = ABCMeta

    def __init__(self, xpath):
        self.xpath = xpath

    @abstractmethod
    def getLabel(self):
        """ Return a description of the wait object's logical condition """
        pass

    @abstractmethod
    def getObject(self):
        """ Return a wait object """
        pass


class WaitForElementToBePresent(WaitCondition):

    __metaclass__ = ABCMeta

    def getLabel(self):
        return "Wait for %s to be present" % self.xpath


class WaitForElementToBeClickable(WaitCondition):

    __metaclass__ = ABCMeta

    def getLabel(self):
        return "Wait for %s to be clickable" % self.xpath

class WaitForElementToBeVisible(WaitCondition):

    __metaclass__ = ABCMeta

    def getLabel(self):
        return "Wait for %s to be visible" % self.xpath

class WaitForAlert(WaitCondition):

    __metaclass__ = ABCMeta

    def getLabel(self):
        return "Wait for alert window to show up"
