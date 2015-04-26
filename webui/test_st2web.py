import sys
import unittest
import uuid
import time

from lib.st2web import St2web
from lib.web.implementation_factory import BrowserType


class TestSt2web(unittest.TestCase):

    browser_type = BrowserType.FIREFOX
    host = 'localhost'
    port = '9101'
    auth_port = '9100'
    username = 'testu'
    password = 'testp'

    def setUp(self):
        self.st2web = St2web(self.browser_type, self.host, self.port, self.auth_port)
        self.st2web.get_login_page().login(self.username, self.password)

    def test_run_action(self):

        tested_action = 'core.local'
        action_arguments = {'cmd': 'uname'}
        expected_status = 'Succeeded'
        expected_output = 'Linux'

        action_status = self.st2web.get_actions_page().run_action(tested_action, **action_arguments)
        self.assertEqual(expected_status, action_status)
        trigger_status = self.st2web.get_history_page().get_status_of_last_execution(tested_action)
        self.assertEqual(expected_status, trigger_status)
        run_result = self.st2web.get_history_page().get_output_of_last_execution(tested_action)
        self.assertEqual(expected_output, run_result)

    def test_web_trigger(self):

        new_rule_name = 'rule' + str(uuid.uuid4())
        unique_echo = 'from' + new_rule_name
        tested_trigger = 'core.st2.webhook'
        tested_action = 'core.local'
        rule_arguments = {'url': 'sample', 'cmd': 'echo ' + unique_echo}
        expected_rule_status = 'Enabled'
        expected_status = 'Succeeded'

        self.st2web.get_rules_page().delete_all_rules()

        self.st2web.get_rules_page().create_rule(new_rule_name, tested_trigger, tested_action, **rule_arguments)

        rule_status = self.st2web.get_rules_page().get_rule_status(new_rule_name)
        self.assertEqual(expected_rule_status, rule_status)
        trigger_id = self.st2web.post_to_web_hook(self.username, self.password)

        history_page = self.st2web.get_history_page()
        history_page.wait_for_triggered_by_rule(new_rule_name)
        
        trigger_status = history_page.wait_for_execution_status(tested_action, expected_status)
        self.assertEqual(expected_status, trigger_status)
        
        trigger_payload = history_page.get_trigger_payload_of_last_execution(tested_action)
        self.assertContains(trigger_payload, trigger_id)
        
        run_result = self.st2web.get_history_page().get_output_of_last_execution(tested_action)
        self.assertEqual(unique_echo, run_result)

    def tearDown(self):
        self.st2web.close()

    def assertContains(self, string, substring):
        if not substring in string:
            self.fail("'%s' doesn't contain '%s'" % (string, substring))

if __name__ == "__main__":
    if len(sys.argv) > 5:
        TestSt2web.password = sys.argv.pop()
        TestSt2web.username = sys.argv.pop()
        TestSt2web.port = sys.argv.pop()
        TestSt2web.host = sys.argv.pop()
    unittest.main()
