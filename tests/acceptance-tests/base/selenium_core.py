import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.driver_context import DriverContext


class SeleniumCore:

    @staticmethod
    def set_element_text(element, value):
        elements = DriverContext.driver.find_elements_by_id(element)
        if len(elements) == 1:
            ele = elements[0]
        else:
            ele = SeleniumCore.set_element_text_by_name(element)
        ele.clear()
        return ele.send_keys(value)

    @staticmethod
    def set_current_data_text(element, value):
        table_element = DriverContext.driver.find_element_by_id('CurrentData')
        if len(table_element.find_elements_by_id(element)) == 1:
            ele = table_element.find_elements_by_id(element)[0]
        elif len(table_element.find_elements_by_name(element)) == 1:
            ele = table_element.find_elements_by_name(element)[0]
        ele.clear()
        return ele.send_keys(value)

    @staticmethod
    def set_element_text_by_name(element):
        elements = DriverContext.driver.find_elements_by_name(element)
        if len(elements) == 1:
            return elements[0]

    @staticmethod
    def click_element(*element):
        ele = WebDriverWait(DriverContext.driver, 5).until(
            EC.element_to_be_clickable(element))
        ele.click()

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
    def find_elements_by(*element):
        return DriverContext.driver.find_elements(element[0], element[1])

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
