# Config file to set up UI_URL, REFERENCE
# It assumes that chromedriver is already installed in $HOMEDIR/chromedriver
# After setting the variables run concurrent_test.sh

import os.path
HOMEDIR = os.path.expanduser("~")
CHROME_DRIVER_LOCATION = HOMEDIR + '/chromedriver'
UI_URL = ''
REFERENCE = ''
