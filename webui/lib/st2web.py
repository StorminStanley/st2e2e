import urllib
import urllib2
import uuid
import st2web_locators
from st2web_common import St2webCommon
from lib.web.browser_factory import BrowserType
from lib.web.browser_factory import BrowserFactory
from st2web_login_page import St2webLoginPage
from st2web_actions_page import St2webActionsPage
from st2web_history_page import St2webHistoryPage
from st2web_rules_page import St2webRulesPage

class St2web(St2webCommon):

    def __init__(self, browser_type, host, port):

        if BrowserType.FIREFOX != browser_type:
            raise ValueError("Current implementation only supports Firefox (%s), while %s was requested" % (BrowserType.FIREFOX, browser_type))
        self.host = host
        self.port = port
        self.url = "http://%s:%s/webui" % (host, port)
        self.print_step("Start st2web on Firefox at " + self.url)
        self.browser = BrowserFactory().get_firefox()
        self.browser.navigate_to_page(self.url, st2web_locators.LOGIN_PAGE_SIGNATURE)

    def close(self):
        self.print_step("Close browser")
        self.browser.close()

    def get_login_page(self):
        return St2webLoginPage(self)

    def get_actions_page(self):
        self.switch_to_view(self.browser, "Actions")
        return St2webActionsPage(self)

    def get_history_page(self):
        self.switch_to_view(self.browser, "History")
        return St2webHistoryPage(self)

    def get_rules_page(self):
        self.switch_to_view(self.browser, "Rules")
        return St2webRulesPage(self)

    def post_to_web_hook(self):
        trigger_id = uuid.uuid1()
        url = "http://%s:%s/v1/webhooks/sample" % (self.host, self.port)
        values = '{"foo": "%s", "name": "st2"}' % trigger_id
        headers = {'Content-type': 'application/json'}
        req = urllib2.Request(url, values, headers)
        self.print_step('Post to webhook: {}\n{}\n{}\n\n{}\n{}\n'.format(
            '-----------START-----------',
            req.get_method() + ' ' + req.get_full_url(),
            '\n'.join('{}: {}'.format(k, v) for k, v in req.header_items()),
            req.get_data(),
            '-------------END-----------'
        ))
        response = urllib2.urlopen(req)
        result = response.read()
        self.print_actual("Received result: " + result)
        return str(trigger_id)
