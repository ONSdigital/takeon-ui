import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.driver_context import DriverContext


class SeleniumCore:

    @staticmethod
    def set_element_text(*element):
        ele = DriverContext.driver.find_element(element[0], element[1])
        ele.clear()
        return ele.send_keys(element[2])

    @staticmethod
    def get_element_by_text(element):
        ele = DriverContext.driver.find_element(element[0], element[1])
        return ele.text

    @staticmethod
    def switch_to_alert_box():
        # Click on the "Refresh" button to generate the Confirmation Alert
        driver = DriverContext.driver
        driver.refresh()
        try:
            # Switch the control to the Alert window
            WebDriverWait(driver, 5).until(EC.alert_is_present(), 'Timed out waiting for alert')
            alert = driver.switch_to.alert
            # Retrieve the message on the Alert window
            message = alert.text
            print("Alert shows following message: " + message)
            time.sleep(2)
            # use the accept() method to accept the alert
            alert.accept()
            print("Alert accepted")
            # get the text returned when OK Button is clicked.
            txt = driver.find_element_by_id('msg')
            print(txt.text)
            time.sleep(2)
        except TimeoutException:
            print("No Alert")

    @staticmethod
    def switch_window():
        driver = DriverContext.driver
        handles = driver.window_handles
        current_handle = driver.current_window_handle
        for handle in handles:
            if handle != current_handle:
                driver.switch_to.window(handle)
                print(driver.title)
                break

    @staticmethod
    def close_the_current_window():
        driver = DriverContext.driver
        handles = driver.window_handles
        current_handle = driver.current_window_handle
        for handle in handles:
            if handle != current_handle:
                driver.close()
                driver.switch_to.window(handle)
                print(driver.title)
                break
