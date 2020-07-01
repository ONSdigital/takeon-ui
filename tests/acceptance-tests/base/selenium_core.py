import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.driver_context import DriverContext


class SeleniumCore:

    @staticmethod
    def set_element_text_by_id(element, value):
        ele = DriverContext.driver.find_element_by_id(element)
        ele.clear()
        return ele.send_keys(value)

    @staticmethod
    def set_element_text(*element):
        ele = DriverContext.driver.find_element(element[0], element[1])
        ele.clear()
        return ele.send_keys(element[2])

    @staticmethod
    def get_element_text(*element):
        ele = DriverContext.driver.find_element(element[0], element[1])
        return ele.text

    @staticmethod
    def get_attribute_element_text(*element):
        ele = DriverContext.driver.find_element(element[0], element[1])
        return ele.get_attribute("value")

    @staticmethod
    def find_elements_by_xpath(element):
        return DriverContext.driver.find_elements_by_xpath(element)

    @staticmethod
    def switch_to_alert_box():
        # Click on the "Refresh" button to generate the Confirmation Alert
        driver = DriverContext.driver
        driver.refresh()
        try:
            # Switch the control to the Alert window
            WebDriverWait(driver, 5).until(EC.alert_is_present(), 'Timed out waiting for alert')
            alert = driver.switch_to.alert
            alert.accept()
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
                break
