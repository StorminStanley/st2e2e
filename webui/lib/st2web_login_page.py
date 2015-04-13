import st2web_locators
from lib.web.implementation_factory import ImplementationFactory
from st2web_common import St2webCommon

class St2webLoginPage(St2webCommon):

    DEFAULT_VIEW = "History"

    def __init__(self, st2web):
        self.st2web = st2web

    def login(self):
        self.print_step("Login")
        login_page = self.st2web.browser.navigate_to_page(self.st2web.url, st2web_locators.LOGIN_PAGE_SIGNATURE)
        login_button = login_page.wait(ImplementationFactory().get_wait_for_element_to_be_clickable(st2web_locators.LOGIN_BUTTON))
        login_button.click()
        self.wait_for_view_to_load(self.st2web.browser, self.DEFAULT_VIEW)
        self.print_actual("Logged-in successfully")

