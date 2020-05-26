"""
Class containing common functions used in several tests.
Functions that are not test or feature specific.
"""
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException

from base.driver_context import DriverContext
from config_files.config_test import ConfigTest
from config_files.url_configs import URL_CONFIG


class Browser:

    def initialize_the_browser(self, browser_type=None):
        """
        Function to start instance of the specified browser and navigate to the specified url.
        :param url: the url to navigate to
        :param browser_type: the type of browser to start (Default is Chrome)
        :return: driver: browser instance
        """
        if not browser_type:
            # create instance of the Chrome driver
            DriverContext.driver = webdriver.Chrome(ConfigTest.CHROME_DRIVER_LOCATION)
            DriverContext.driver.maximize_window()

        elif browser_type.lower() == 'firefox':
            # create instance of Firefox driver the browser type is not specified
            DriverContext.driver = webdriver.Firefox()
        else:
            raise Exception("The browser type '{}' is not supported".format(browser_type))

        # Browser.navigate_to_the_url()

    @staticmethod
    def navigate_to_the_url():
        # clean the url and go to the url
        # Create a class called url_configs in config_files folder
        # and create a dictionary list URL_CONFIG add a env_url as key and url as value
        # locally to able to run the tests against that environment
        # uncomment the below url and use instead of the url from ConfigTest
        url = URL_CONFIG.get('env_url').strip()
        # url from ConfigTest is a placeholder and will fail as there is no url been set up
        # IMPORTANT: add url_configs.py to git exclude in order to ignore the class by git to stop accidentally committing it to repo
        # url = ConfigTest.UI_URL
        try:
            if url:
                t = time.time()
                DriverContext.driver.set_page_load_timeout(10)
                try:
                    current_url = DriverContext.driver.current_url
                    if url != current_url:
                        DriverContext.driver.get(url)
                        return DriverContext.driver
                except TimeoutException:
                    DriverContext.driver.execute_script("window.stop();")
                    assert False, 'Time taken to load the url: ' + str(time.time() - t)
            else:
                raise ValueError(
                    'empty url.'
                    'Please set the url in url_configs file.'
                    ' Follow the steps mentioned in the comments')

        except ValueError as e:
            print(e)
