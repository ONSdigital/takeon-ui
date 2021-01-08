from base.browser import Browser
from base.driver_context import DriverContext
from base.selenium_core import SeleniumCore
from base.utilities import Utilities
from base.cognito import Cognito
from pages.common.login_page import LoginPage


def before_all(context):
    Utilities.delete_screenshots_folder()
    Browser.url()


def before_feature(context, feature):
    Browser.initialize_the_browser(context)


def before_scenario(context, scenario):
    Browser.navigate_to_the_url()


def after_scenario(context, scenario):
    # take screenshot if test failed
    Utilities.take_screen_shot(scenario)
    SeleniumCore.close_the_current_window()
    LoginPage().logout()



# After all the tests we need to close the browser
def after_feature(context, feature):
    DriverContext.driver.quit()

# Setup cognito so we can create users in step defs
def before_all(context):
    context.created_users = {}
    context.cognito = Cognito()

# Ensure all created users have been cleaned up
def after_all(context):
    for user in context.created_users.keys():
        if context.cognito.user_exists(user):
            context.cognito.delete_user(user)
