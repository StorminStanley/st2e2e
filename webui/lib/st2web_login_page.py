import st2web_locators
from lib.web.implementation_factory import ImplementationFactory
from st2web_common import St2webCommon


class St2webLoginPage(St2webCommon):

    DEFAULT_VIEW = "History"

    def __init__(self, st2web):
        self.st2web = st2web

    def login(self, username, password):
        self.print_step("Login as %s/%s" % (username, password))
        login_page = self.st2web.browser.navigate_to_page(self.st2web.url,
                                                          st2web_locators.LOGIN_PAGE_SIGNATURE)
  
        username_field = login_page.get(st2web_locators.LOGIN_USERNAME)
        username_field.type_value(username)
        
        password_field = login_page.get(st2web_locators.LOGIN_PASSWORD)
        password_field.type_value(password)

        wait_login_button = ImplementationFactory().get_wait_for_element_to_be_clickable(st2web_locators.LOGIN_BUTTON)
        login_button = login_page.wait(wait_login_button)
        login_button.click()
        login_button.click() # Temporary workaround for STORM-1253
        
        self.wait_for_view_to_load(self.st2web.browser, self.DEFAULT_VIEW)
        self.print_actual("Logged-in successfully")
