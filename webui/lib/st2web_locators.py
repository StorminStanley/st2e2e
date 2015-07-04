LOGIN_PAGE_SIGNATURE = '//div[contains(@class,"login")]'
LOGIN_USERNAME = '//input[contains(@ng-model,"username")]'
LOGIN_PASSWORD = '//input[contains(@ng-model,"password")]'
LOGIN_BUTTON = '//input[contains(@value,"Connect")]'

ACTIONS_PAGE_SIGNATURE = '//div[contains(@class, "view st2-actions")]'
ACTIONS_RUN_BUTTON = '//button[contains(@class, "forms__button")]'
ACTIONS_RUN_STATUS = '//span[contains(@status, "record.status")]'
ACTIONS_RUN_TIMESTAMP = '//div[contains(@class, "actions__details-column-time")]'

HISTORY_PAGE_SIGNATURE = '//div[contains(@class, "view st2-history")]'
HISTORY_EXECUTION_RESULT_STDOUT = '//div[contains(@code, "execution.result.stdout")]'
HISTORY_EXECUTION_RESULT_STATUS = \
    '//div[contains(@class, "action-reporter")]/span[contains(@status, "record.status")]'
HISTORY_EXECUTION_RESULT_TRIGGER_PAYLOAD = \
    '//dd[contains(@ng-if, "record.trigger_instance.payload")]'
HISTORY_EXECUTION_RESULT_TRIGGERED_BY = \
    '//div[contains(@class, "column-triggered")]/span[contains(@title, "%s")]'

RULES_PAGE_SIGNATURE = '//div[contains(@class, "view st2-rules")]'
RULES_RULE_STATUS = '//div[contains(@class, "details") and contains(@class, "header-name")]/span'
RULES_ADD_RULE_BUTTON = '//button[contains(@class,"st2-panel__toolbar-button")]'
RULES_NEW_RULE_NAME = '//div[@ng-model="newRule"]/div[@name="name"]/label//textarea'
RULES_NEW_RULE_TRIGGER = '//div[@ng-model="newRule.trigger"]/div[@name="trigger"]/label/input'
RULES_NEW_RULE_ACTION = '//div[@ng-model="newRule.action"]/div[@name="action"]/label/input'
RULES_NEW_RULE_SAVE = '//form[@name="newform"]/input[@value="Save"]'
RULES_TABLE_ROW = '//div[@ng-repeat="rule in rules"]'
RULES_DELETE = '//div[contains(@class, "details__toolbar")]/input[@value="Delete"]'

COMMON_VIEW_TITLE = '//div[contains(@class,"panel__toolbar-title") and contains(text(), "%s")]'
COMMON_MENU_VIEW_LINK = '//a[contains(@href, "%s")]'
COMMON_COLUMN_NAME_AND_VALUE = '//div[contains(@class, "column-%s") and contains(@title, "%s")]'
COMMON_FORM = '//div[contains(@class, "form__title") and contains(text(), "%s")]'
