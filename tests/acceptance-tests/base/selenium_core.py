"""
Class containing common functions used in several tests.
Functions that are not test or feature specific.
"""
from selenium import webdriver
from config_files.config_test import ConfigTest
# from config_files.url_configs import URL_CONFIG


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

        SeleniumCore.navigate_to_the_url(context)

    @staticmethod
    def navigate_to_the_url(context):

        # clean the url and go to the url
        # Create a class called url_configs in config_files folder
        # and create a dictionary list URL_CONFIG add a env_url as key and url as value
        # locally to able to run the tests against that environment
        # uncomment the below url and use instead of the url from ConfigTest
        # url = URL_CONFIG.get('env_url').strip()
        # url from ConfigTest is a placeholder and will fail as there is no url been set up
        # IMPORTANT: add url_configs.py to git exclude in order to ignore the class by git to stop accidentally committing it to repo
        url = ConfigTest.UI_URL
        try:

            if not url:
                context.driver.get(url)
                context.driver.maximize_window()
                context.driver.implicitly_wait(2)
                return context.driver
            else:
                raise ValueError(
                    'empty url.'
                    'Please set the url in url_configs file.'
                    ' Follow the steps mentioned in the comments')
        except ValueError as e:
            print(e)
