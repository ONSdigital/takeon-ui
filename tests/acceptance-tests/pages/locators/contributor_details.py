from selenium.webdriver.common.by import By

SAVE_AND_VALIDATE = By.ID, 'saveFormButton'
STATUS = By.XPATH, '//span[contains(@title,"Status")]'
ERROR_MESSAGES_ELEMENT = '//p[@class="panel__error u-mb-no"]'
OVERRIDE_MESSAGE_LABEL = '//label'
CURRENT_PERIOD_COLUMN = 'td[2]'
ERROR_MESSAGES_COLUMN = 'td[4]'
OVERRIDE_BUTTON = By.ID, 'override_button'
OVERRIDE_MESSAGE_ELEMENT = By.CLASS_NAME, 'checkbox__label to-u-bg'
CURRENT_DATA_TAB_ELEMENT = 'tabId1'
HISTORIC_DATA_TAB_ELEMENT = 'tabId2'
OVERRIDE_CHECKBOX_ELEMENT = 'override-checkbox'