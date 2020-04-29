from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ContributorSearchPage(BasePage):
    REFERENCE_TEXT_FIELD = By.ID, 'reference'
    PERIOD_TEXT_FIELD = By.ID, 'period'
    SURVEY_TEXT_FIELD = By.ID, 'survey'
    SEARCH_BUTTON = By.XPATH, "//button[@class='btn btn--small']"

    def select_the_reference_view_form(self, reference, period):
        self.submit_search_details(reference, period)
        table = self.driver.find_element_by_id("ResultsTable")
        rows = table.find_elements_by_tag_name("tr")
        # Ignore the first row
        for i in range(1, len(rows)):
            cols = rows[i].find_elements_by_tag_name("td")
            # Check to see if any references appear that shouldn't be there
            if (cols[i].text == reference and cols[i + 1].text == period):
                window_before = self.driver.window_handles[0]
                cols[i - 1].click()
                break

    def submit_search_details(self, reference, period):
        ele = self.find_element_by(*ContributorSearchPage.REFERENCE_TEXT_FIELD)
        ele.send_keys(reference)
        ele = self.find_element_by(*ContributorSearchPage.PERIOD_TEXT_FIELD)
        ele.send_keys(period)
        self.driver.find_element(*ContributorSearchPage.SEARCH_BUTTON).click()

    def find_element_by(self, *element):
        ele = self.driver.find_element(*element)
        ele.clear()
        return ele
