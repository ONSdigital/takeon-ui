from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# What occurs before all the tests
# For this, we just need to open the browser
def before_feature(context, feature):
    context.browser = webdriver.Chrome()
    
# After all the tests we need to close the browser
def after_feature(context, feature):
    context.browser.quit()
