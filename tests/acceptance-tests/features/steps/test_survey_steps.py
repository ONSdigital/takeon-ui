from behave import given, when, then

from pages.common.contributor_search_page import ContributorSearchPage
from pages.test_survey.test_survey_contributor_details_page import TestSurveyContributorDetailsPage


@given(u'I have all the back period details including the current period {period}')
def step_impl(context, period):
    context.periods = ContributorSearchPage().get_all_the_periods(context.reference, period, sic_code=None)


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


@then(u'I should be able to view all the back periods in historic data tab')
def step_impl(context):
    TestSurveyContributorDetailsPage().check_historic_data_back_periods(context.periods)


@then(u'the values {values} should be matching to the corresponding questions in {tab_name} tab')
def step_impl(context, values, tab_name):
    TestSurveyContributorDetailsPage().check_historic_data_matches_with_current_period_data(context.survey,
                                                                                            context.question_codes,
                                                                                            values, tab_name)
