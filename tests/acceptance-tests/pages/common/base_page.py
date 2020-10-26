from base.driver_context import DriverContext
from base.utilities import Utilities


class BasePage:

    def __init__(self, title):
        self.driver = DriverContext.driver
        Utilities.check_page_title(title)
