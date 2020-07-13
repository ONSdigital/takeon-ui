from base.browser import Browser
from base.driver_context import DriverContext
from base.selenium_core import SeleniumCore


def before_feature(context, feature):
    Browser.initialize_the_browser(context)


def before_scenario(context, scenario):
    Browser.navigate_to_the_url()


# After all the tests we need to close the browser
def after_scenario(context, scenario):
    SeleniumCore.close_the_current_window()


# After all the tests we need to close the browser
def after_feature(context, feature):
    DriverContext.driver.quit()
