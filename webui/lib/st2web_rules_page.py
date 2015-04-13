import st2web_locators
from lib.web.implementation_factory import ImplementationFactory
from st2web_common import St2webCommon

class St2webRulesPage(St2webCommon):

    def __init__(self, st2web):
        self.st2web = st2web

    def get_rule_status(self, rule_name):
        self.print_step("Check the status of %s rule" % rule_name)
        rules_page = self.st2web.browser.get_page(st2web_locators.RULES_PAGE_SIGNATURE)
        self.select_list_item_by_column_value(rules_page, 'name', rule_name)
        rule_status_element = rules_page.wait(ImplementationFactory().get_wait_for_element_to_be_present(st2web_locators.RULES_RULE_STATUS))
        rule_status = rule_status_element.get_text()
        self.print_actual("Rule status is: " + rule_status)
        return rule_status
