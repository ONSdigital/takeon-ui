from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# What occurs before all the tests
# For this, we just need to open the browser
from base.selenium_core import SeleniumCore


def before_scenario(context, scenario):
    SeleniumCore.initialize_the_browser(context)


# After all the tests we need to close the browser
def after_feature(context, feature):
    context.driver.quit()
