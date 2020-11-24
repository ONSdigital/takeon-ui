from behave import given, then
from base.driver_context import DriverContext


@then(u'{ref} and {period} and {survey} will be displayed')
def check_survey_period_details(context, ref, period, survey):
    table = DriverContext.driver.find_element_by_id("ResultsTable")
    rows = table.find_elements_by_tag_name("tr")
    failed = []
    # True if ref is found
    found = False
    # Ignore the first row
    for i in range(1, len(rows)):
        cols = rows[i].find_elements_by_tag_name("td")
        # Check to see if any references appear that shouldn't be there
        if (cols[context.columns["reference"]].text != ref):
            failed.append("Column " + str(context.columns["reference"]) + " is " +
                          str(cols[1].text) + " but expecting " + str(ref))
        elif (cols[context.columns["period"]].text == period and cols[context.columns["survey"]].text == survey):
            found = True
    if (not found):
        failed.append("Did not find " + str(ref))
    if (len(failed) > 0):
        assert False, "failed due to these reasons - " + str(failed)


@then(u'no table should appear')
def check_survey_data_table(context):
    table = DriverContext.driver.find_elements_by_id("ResultsTable")
    if (len(table) > 1):
        assert False, "Survey table should not be shown"


@given(u'a {surveyId} has been entered into the survey search input')
def submit_survey_details(context, surveyId):
    elem = DriverContext.driver.find_element_by_name("survey")
    elem.clear()
    elem.send_keys(surveyId)
