LOGIN_PAGE_SIGNATURE = '//div[contains(@class,"login")]'
LOGIN_BUTTON = '//input[contains(@class,"login__button")]'

ACTIONS_PAGE_SIGNATURE = '//div[contains(@class, "view st2-actions")]'
ACTIONS_RUN_BUTTON = '//button[contains(@class, "forms__button")]'
ACTIONS_RUN_STATUS = '//span[contains(@status, "record.status")]'

HISTORY_PAGE_SIGNATURE = '//div[contains(@class, "view st2-history")]'
HISTORY_EXECUTION_RESULT_STDOUT = '//div[contains(@code, "execution.result.stdout")]'
HISTORY_EXECUTION_RESULT_STATUS = '//div[contains(@class, "action-reporter")]/span[contains(@status, "record.status")]'
HISTORY_EXECUTION_RESULT_TRIGGER_PAYLOAD = '//dd[contains(@ng-if, "record.trigger_instance.payload")]'

RULES_PAGE_SIGNATURE = '//div[contains(@class, "view st2-rules")]'
RULES_RULE_STATUS = '//div[contains(@class, "details") and contains(@class, "header-name")]/span'

COMMON_VIEW_TITLE = '//div[contains(@class,"panel__toolbar-title") and contains(text(), "%s")]'
COMMON_MENU_VIEW_LINK = '//a[contains(@href, "%s")]'
COMMON_COLUMN_NAME_AND_VALUE = '//div[contains(@class, "column-%s") and contains(@title, "%s")]'
COMMON_FORM = '//div[contains(@class, "form__title") and contains(text(), "%s")]'
