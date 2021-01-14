"""
Class containing common functions used in several tests.
Functions that are not test or feature specific.
"""
import os
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, InvalidArgumentException, WebDriverException
from selenium.webdriver.chrome.options import Options
from base.driver_context import DriverContext
from config_files.config_test import ConfigTest


class Browser:

    @staticmethod
    def initialize_the_browser(context):
        """
        Function to start instance of the specified browser and navigate to the specified url.
        :param url: the url to navigate to
        :param browser: the type of browser to start (Default is Chrome)
        :return: driver: browser instance
        """
        browser = context.config.userdata.get('browser')

        if not browser:
            # create instance of the Chrome driver
            DriverContext.driver = webdriver.Chrome(executable_path=ConfigTest.CHROME_DRIVER_LOCATION)
            DriverContext.driver.maximize_window()
        elif browser.lower() == 'headless':
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("disable-infobars")
            chrome_options.add_argument("--disable-extensions")
            # create instance of the Chrome driver
            DriverContext.driver = webdriver.Chrome(executable_path=ConfigTest.CHROME_DRIVER_LOCATION,
                                                    chrome_options=chrome_options)
            DriverContext.driver.maximize_window()
        elif browser.lower() == 'docker-browser':
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_prefs = {}
            chrome_options.experimental_options["prefs"] = chrome_prefs
            chrome_prefs["profile.default_content_settings"] = {"images": 2}
            DriverContext.driver = webdriver.Chrome(chrome_options=chrome_options)
        else:
            raise Exception("The browser type '{}' is not supported".format(browser))

    @staticmethod
    def navigate_to_the_url():
        # clean the url and go to the url
        url = ConfigTest.UI_URL
        try:
            if url:
                t = time.time()
                DriverContext.driver.set_page_load_timeout(10)
                try:
                    current_url = DriverContext.driver.current_url
                    if url != current_url:
                        if 'http' not in url:
                            url = 'http://' + url
                            print('url with http is ' + url)
                        DriverContext.driver.get(url)
                        return DriverContext.driver
                except InvalidArgumentException:
                    assert False, 'Check the url.It needs to contain the http protocol in it: ' + url
                except TimeoutException:
                    DriverContext.driver.execute_script("window.stop();")
                    assert False, 'Time taken to load the url: ' + str(time.time() - t)
                except WebDriverException as ex:
                    print(ex)
                    if "unknown error: net::ERR_NAME_NOT_RESOLVED" in str(ex):
                        assert False, ('Unable to Navigate to URL:{} \n'
                                       'possibly because of the url is not valid'.format(url))
            else:
                raise ValueError(
                    'Test failed as there was no url been set.\n'
                    'To set the url.'
                    'Please follow the steps mentioned in the Readme file')

        except ValueError as e:
            print(e)

    @staticmethod
    def url():
        print('url is ' + ConfigTest.UI_URL)
