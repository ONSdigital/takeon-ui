# Config file to set up UI_URL, REFERENCE
# It assumes that chromedriver is already installed in $HOMEDIR/chromedriver
# UI_URL from ConfigTest is a placeholder only and tests will fail as there is no url.
# Follow the steps mentioned in Readme file in order to run tests locally

import os.path


class ConfigTest:
    HOMEDIR = os.path.expanduser("~")
    CHROME_DRIVER_LOCATION = HOMEDIR + '/chromedriver'
    UI_URL = os.environ['TAKEON_URL']

    @staticmethod
    def file_path(file_name):
        dirpath = os.path.dirname(__file__)
        return os.path.join(dirpath, file_name)
