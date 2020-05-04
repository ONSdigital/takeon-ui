from base.driver_context import DriverContext


class SeleniumCore:

    def find_element_by(*element):
        ele = DriverContext.driver.find_element(*element)
        ele.clear()
        return ele

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
