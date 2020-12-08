from base.browser import Browser
from base.driver_context import DriverContext
from base.selenium_core import SeleniumCore
from base.utilities import Utilities


def before_feature(context, feature):
    context.screenshots_dir = Browser.initialize_the_browser(context)


def before_scenario(context, scenario):
    Browser.navigate_to_the_url()


def after_scenario(context, scenario):
    # take screenshot if test failed
    Utilities.take_screen_shot(scenario, context.screenshots_dir)
    SeleniumCore.close_the_current_window()


# After all the tests we need to close the browser
def after_feature(context, feature):
    DriverContext.driver.quit()
