from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# What occurs before all the tests
# For this, we just need to open the browser
from base.browser import Browser
from base.driver_context import DriverContext


def before_feature(context, feature):
    Browser.initialize_the_browser(context)


# After all the tests we need to close the browser
def after_feature(context, feature):
    DriverContext.driver.quit()
