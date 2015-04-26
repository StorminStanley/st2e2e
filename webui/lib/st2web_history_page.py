import time
import st2web_locators
from lib.web.abstract_web_page import WebPage
from lib.web.implementation_factory import ImplementationFactory
from st2web_common import St2webCommon


class St2webHistoryPage(St2webCommon):

    def __init__(self, st2web):
        self.st2web = st2web

    def get_output_of_last_execution(self, action_name):
        return self.get_last_execution_value(action_name, 'output',
                                             st2web_locators.HISTORY_EXECUTION_RESULT_STDOUT)

    def get_status_of_last_execution(self, action_name):
        return self.get_last_execution_value(action_name, 'status',
                                             st2web_locators.HISTORY_EXECUTION_RESULT_STATUS)

    def get_trigger_payload_of_last_execution(self, action_name):
        return self.get_last_execution_value(action_name, 'trigger payload',
                                             st2web_locators.HISTORY_EXECUTION_RESULT_TRIGGER_PAYLOAD)

    def get_last_execution_value(self, action_name, field_name, field_xpath):
        self.print_step("Get %s of last execution of %s action" % (field_name, action_name))
        history_page = self.st2web.browser.get_page(st2web_locators.HISTORY_PAGE_SIGNATURE)
        self.select_list_item_by_column_value(history_page, 'action', action_name)
        wait_field_panel = ImplementationFactory().get_wait_for_element_to_be_present(field_xpath)
        field_panel = history_page.wait(wait_field_panel)
        field_value = field_panel.get_text()
        self.print_actual("Last execution %s is: %s" % (field_name, field_value))
        return field_value

    def wait_for_triggered_by_rule(self, rule_name):
        self.print_step("Wait for action triggered by rule %s" % rule_name)
        history_page = self.st2web.browser.get_page(st2web_locators.HISTORY_PAGE_SIGNATURE)
        xpath = st2web_locators.HISTORY_EXECUTION_RESULT_TRIGGERED_BY % rule_name
        wait_new_execution = ImplementationFactory().get_wait_for_element_to_be_present(xpath)
        return

    def wait_for_execution_status(self, action_name, status):
        pause = WebPage.SHORT_WAIT
        wait_until = time.time() + WebPage.LONG_WAIT
        trigger_status = self.get_status_of_last_execution(action_name)
        while status != trigger_status and wait_until - time.time() >= 0:
            time.sleep(pause)
            print "%d" % (wait_until - time.time())
            trigger_status = self.get_status_of_last_execution(action_name)
        return trigger_status
