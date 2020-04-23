# Config file to set up UI_URL, REFERENCE
# It assumes that chromedriver is already installed in $HOMEDIR/chromedriver
# UI_URL from ConfigTest is a placeholder only and tests will fail as there is no url.
# Follow the steps mentioned in selenium core class in order to run tests locally

import os.path

class ConfigTest:
    HOMEDIR = os.path.expanduser("~")
    CHROME_DRIVER_LOCATION = HOMEDIR + '/chromedriver'
    UI_URL = ''
