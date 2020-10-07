from behave import given, when, then

from pages.common.contributor_details_page import ContributorDetailsPage
from pages.test_survey.test_survey_contributor_details_page import TestSurveyContributorDetailsPage


@given(u'has {validation_type} value {primary_value} compared to value {comparison_value}')
@when(u'has {validation_type} value {primary_value} compared to value {comparison_value}')
def step_impl(context, validation_type, primary_value, comparison_value):
    context.internet_sales = primary_value
    context.total_sales = comparison_value

    TestSurveyContributorDetailsPage().submit_sales_values(validation_type, context.period_type, context.internet_sales,
                                                           context.total_sales)


@when(u'I switch to the "{tab_name}" tab on the contributor details page')
def step_impl(context, tab_name):
    TestSurveyContributorDetailsPage().switch_to_the_tab(tab_name)


@then(u'I should be able to view the historic data')
def step_impl(context):
    TestSurveyContributorDetailsPage().check_historic_data_exists()
