from pages.base_page import BasePage


class ContributorSearchPage(BasePage):

    def select_the_reference_view_form(self, reference):
        table = self.driver.find_element_by_id("ResultsTable")
        rows = table.find_elements_by_tag_name("tr")
        # Ignore the first row
        for i in range(1, len(rows)):
            cols = rows[i].find_elements_by_tag_name("td")
            # Check to see if any references appear that shouldn't be there
            if (cols[i].text == reference):
                window_before = self.driver.window_handles[0]
                cols[i - 1].click()
