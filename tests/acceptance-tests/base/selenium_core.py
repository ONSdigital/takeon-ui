"""
Module containing common function used in several tests-tests.
Functions that are not test or feature specific.
"""
from selenium import webdriver

from config_files.config_test import ConfigTest


# Create a class called url_configs in config_files package folder
# and create a dictionary list URL_CONFIG add a env_url as key and url as value
# locally to able to run the tests against that environment
# uncomment the below import after doing the above steps
# IMPORTANT: add url_configs.py to git exclude in order to ignore the class by git
from config_files.url_configs import URL_CONFIG


class SeleniumCore:

    def initialize_the_browser(context, browser_type=None):
        """
        Function to start instance of the specified browser and navigate to the specified url.
        :param url: the url to navigate to
        :param browser_type: the type of browser to start (Default is Chrome)
        :return: driver: browser instance
        """
        if not browser_type:
            # create instance of the Chrome driver
            context.driver = webdriver.Chrome(ConfigTest.CHROME_DRIVER_LOCATION)
        elif browser_type.lower() == 'firefox':
            # create instance of Firefox driver the browser type is not specified
            context.driver = webdriver.Firefox()
        else:
            raise Exception("The browser type '{}' is not supported".format(browser_type))

        # clean the url and go to the url
        # Create a class called url_configs in config_files package folder
        # and create a dictionary list URL_CONFIG add a env_url as key and url as value
        # locally to able to run the tests against that environment
        # uncomment the below url and use instead of the url from ConfigTest
        url = URL_CONFIG.get('env_url').strip()
        # url from ConfigTest is a placeholder tests will fail as there is no url
        # url = ConfigTest.UI_URL
        context.driver.get(url)
        context.driver.implicitly_wait(2)
        return context.driver

    def navigate_to_the_url(context):
        pass
        # url = URL_CONFIG.get('env_url').strip()
        # context.driver.get(url)
        # context.driver.implicitly_wait(2)
