import st2web_locators
from lib.web.implementation_factory import ImplementationFactory
from st2web_common import St2webCommon
import time

class St2webRulesPage(St2webCommon):

    def __init__(self, st2web):
        self.st2web = st2web

    def get_rule_status(self, rule_name):
        self.print_step("Check the status of %s rule" % rule_name)
        rules_page = self.st2web.browser.get_page(st2web_locators.RULES_PAGE_SIGNATURE)
        self.select_list_item_by_column_value(rules_page, 'name', rule_name)

        wait_rule_status_element = ImplementationFactory().get_wait_for_element_to_be_present(st2web_locators.RULES_RULE_STATUS)
        rule_status_element = rules_page.wait(wait_rule_status_element)
        rule_status = rule_status_element.get_text()
        self.print_actual("Rule status is: " + rule_status)
        return rule_status

    def create_rule(self, rule_name, trigger_name, action_name, **kwargs):
        self.print_step("Create a rule '%s' (with trigger '%s' and action '%s')" % (rule_name, trigger_name, action_name))

        rules_page = self.st2web.browser.get_page(st2web_locators.RULES_PAGE_SIGNATURE)
        
        add_rule_button = self.wait_and_get_element(rules_page, st2web_locators.RULES_ADD_RULE_BUTTON)
        add_rule_button.click()

        ImplementationFactory().get_wait_for_element_to_be_visible(st2web_locators.RULES_NEW_RULE_NAME)

        rule_name_field = self.wait_and_get_element(rules_page, st2web_locators.RULES_NEW_RULE_NAME)
        rule_name_field.type_value(rule_name)
        
        trigger_name_field = self.wait_and_get_element(rules_page, st2web_locators.RULES_NEW_RULE_TRIGGER)
        trigger_name_field.type_value_in_list(trigger_name)
        
        action_name_field = self.wait_and_get_element(rules_page, st2web_locators.RULES_NEW_RULE_ACTION)
        action_name_field.type_value_in_list(action_name)

        for name, value in kwargs.items():
            self.fill_form_input_field(rules_page, name, value)

        action_save_button = self.wait_and_get_element(rules_page, st2web_locators.RULES_NEW_RULE_SAVE)
        action_save_button.click()

    def delete_all_rules(self):

        rules_page = self.st2web.browser.get_page(st2web_locators.RULES_PAGE_SIGNATURE)

        number_rules = rules_page.get_count(st2web_locators.RULES_TABLE_ROW)
        self.print_step("Delete %d existing rules" % number_rules)
        i = 0
        while i < number_rules:
            rule = self.wait_and_get_element(rules_page, st2web_locators.RULES_TABLE_ROW)
            rule.click()
            delete_button = self.wait_and_get_element(rules_page, st2web_locators.RULES_DELETE)
            delete_button.click()
            rules_page.confirm_alert()
            i = i + 1
