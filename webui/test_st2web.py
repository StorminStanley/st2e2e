import sys
import unittest

from lib.st2web import St2web
from lib.web.browser_factory import BrowserType

class TestSt2web(unittest.TestCase):

    host = 'localhost'
    port = '9101'
    browser_type = BrowserType.FIREFOX

    def setUp(self):
        self.st2web = St2web(self.browser_type, self.host, self.port)
        self.st2web.get_login_page().login()

    def test_run_action(self):
        action_status = self.st2web.get_actions_page().run_action('core.local', cmd='uname')
        self.assertEqual("Succeeded", action_status)
        trigger_status = self.st2web.get_history_page().get_status_of_last_execution('core.local')
        self.assertEqual("Succeeded", trigger_status)
        run_result = self.st2web.get_history_page().get_output_of_last_execution('core.local')
        self.assertEqual("Linux", run_result)

    def test_web_trigger(self):
        rule_status = self.st2web.get_rules_page().get_rule_status('examples.webhook_file')
        self.assertEqual("Enabled", rule_status)
        trigger_id = self.st2web.post_to_web_hook()
        trigger_status = self.st2web.get_history_page().get_status_of_last_execution('core.local')
        self.assertEqual("Succeeded", trigger_status)
        trigger_payload = self.st2web.get_history_page().get_trigger_payload_of_last_execution('core.local')
        self.assertContains(trigger_payload, trigger_id)
        
    def tearDown(self):
        self.st2web.close()

    def assertContains(self, string, substring):
        if not substring in string:
            failure.fail()

if __name__ == "__main__":
    if len(sys.argv) > 3:
        TestSt2web.port = sys.argv.pop()
        TestSt2web.host = sys.argv.pop()
    unittest.main()

