import st2web_locators
from lib.web.implementation_factory import ImplementationFactory
from st2web_common import St2webCommon


class St2webActionsPage(St2webCommon):

    def __init__(self, st2web):
        self.st2web = st2web

    def run_action(self, action_name, **kwargs):
        self.print_step("Run action %s and get its status" % action_name)
        actions_page = self.st2web.browser.get_page(st2web_locators.ACTIONS_PAGE_SIGNATURE)
        self.select_list_item_by_column_value(actions_page, 'name', action_name)
        for name, value in kwargs.items():
            self.fill_form_input_field(actions_page, name, value)

        wait_button = ImplementationFactory().get_wait_for_element_to_be_clickable(st2web_locators.ACTIONS_RUN_BUTTON)
        run_button = actions_page.wait(wait_button)
        run_button.click()

        wait_result = ImplementationFactory().get_wait_for_element_to_be_present(st2web_locators.ACTIONS_RUN_STATUS)
        result = self.st2web.current_view.wait(wait_result)
        status = result.get_text()
        self.print_actual("Action status is: " + status)
        return status
