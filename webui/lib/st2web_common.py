import st2web_locators
from lib.web.implementation_factory import ImplementationFactory

class St2webCommon:

    def print_step(self, message):
        print ">>> " + message

    def print_actual(self, message):
        print "<<< " + message

    def print_log(self, message):
        print "    " + message

    def wait_for_view_to_load(self, browser, view_name):
        self.print_log("Wait for %s to load" % view_name)
        self.current_view = browser.get_page(st2web_locators.COMMON_VIEW_TITLE % view_name)

    def switch_to_view(self, browser, view_name):
        self.print_log("Switch to %s" % view_name)
        menu_link_xpath = st2web_locators.COMMON_MENU_VIEW_LINK % view_name.lower()
        page_with_menu = browser.get_page(menu_link_xpath)
        menu_link = page_with_menu.wait(ImplementationFactory().get_wait_for_element_to_be_clickable(menu_link_xpath))
        menu_link.click()
        self.wait_for_view_to_load(browser, view_name)

    def select_list_item_by_column_value(self, page, column_name, column_value):
        self.print_log("Find the column %s with value %s in the list and click on its row" % (column_name, column_value))
        column = page.wait(ImplementationFactory().get_wait_for_element_to_be_present(st2web_locators.COMMON_COLUMN_NAME_AND_VALUE % (column_name, column_value)))
        row = column.get_relative('..')
        row.click()

    def fill_form_input_field(self, page, label, value):
        self.print_log("Fill the form field %s with value %s" % (label, value))
        form = page.wait(ImplementationFactory().get_wait_for_element_to_be_present(st2web_locators.COMMON_FORM % label))
        label = form.get_relative('..')
        input_element = label.get_relative('./input')
        input_element.type_value(value)
