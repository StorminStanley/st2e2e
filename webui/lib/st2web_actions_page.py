import time
import st2web_locators
from lib.web.implementation_factory import ImplementationFactory
from lib.web.abstract_web_page import WebPage
from st2web_common import St2webCommon


class St2webActionsPage(St2webCommon):

    def __init__(self, st2web):
        self.st2web = st2web

    def run_action(self, action_name, **kwargs):
        self.print_step("Run action %s and get its status" % action_name)
        actions_page = self.st2web.browser.get_page(st2web_locators.ACTIONS_PAGE_SIGNATURE)
        self.select_list_item_by_column_value(actions_page, 'name', action_name)

        previous_timestamp = self.get_last_timestamp()

        for name, value in kwargs.items():
            self.fill_form_input_field(actions_page, name, value)

        wait_button = ImplementationFactory().get_wait_for_element_to_be_clickable(st2web_locators.ACTIONS_RUN_BUTTON)
        run_button = actions_page.wait(wait_button)
        run_button.click()

        current_timestamp = self.get_last_timestamp()
        pause = WebPage.SHORT_WAIT
        wait_until = time.time() + WebPage.LONG_WAIT
        while current_timestamp == previous_timestamp and wait_until - time.time() >= 0:
            time.sleep(pause)
            print "%d" % (wait_until - time.time())
            current_timestamp = self.get_last_timestamp()
        if current_timestamp == previous_timestamp:
            raise LookupError("New action execution did not appear within %d seconds" % WebPage.LONG_WAIT)

        status = self.get_last_status()
        pause = WebPage.SHORT_WAIT
        wait_until = time.time() + WebPage.LONG_WAIT
        while (status == 'Scheduled' or status == 'Running' or status == 'Requested') and wait_until - time.time() >= 0:
            time.sleep(pause)
            status = self.get_last_status()
        self.print_actual("Action status is: " + status)
        return status

    def get_last_timestamp(self):
        wait_result = ImplementationFactory().get_wait_for_element_to_be_present(st2web_locators.ACTIONS_RUN_TIMESTAMP)
        for i in range(0, 10):
            try:
                result = self.st2web.current_view.wait(wait_result)
                return result.get_text()
            except StaleElementReferenceException:
                print "StaleElementReferenceException while getting timestamp. Retrying."
        return ""

    def get_last_status(self):
        wait_result = ImplementationFactory().get_wait_for_element_to_be_present(st2web_locators.ACTIONS_RUN_STATUS)
        result = self.st2web.current_view.wait(wait_result)
        return result.get_text()
        
