from behave import given, when, then

from pages.test_survey.test_survey_contributor_details_page import TestSurveyContributorDetailsPage


@when(u'I switch to the "{tab_name}" tab on the contributor details page')
def step_impl(context, tab_name):
    TestSurveyContributorDetailsPage().switch_to_the_tab(tab_name)


@then(u'I can able to view the questions and current period values')
def step_impl(context):
    TestSurveyContributorDetailsPage().check_current_period_data_exists()
