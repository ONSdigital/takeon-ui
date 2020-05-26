from base.driver_context import DriverContext


class BasePage:

    def __init__(self):
        self.driver = DriverContext.driver
