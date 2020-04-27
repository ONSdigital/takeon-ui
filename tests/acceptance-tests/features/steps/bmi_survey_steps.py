from behave import given, when, then
from pages.contributor_search_page import ContributorSearchPage
from pages.sand_and_gravel_land_details_page import SandAndGravelLandDetails
from pages.search_by_page import SearchByPage


@given(u'As a BMI user I search for the form returned by the contributor with {reference_number} number')
def step_impl(context, reference_number):
    context.reference_number = reference_number
    page = SearchByPage(context.driver)
    page.select_search_by(context.reference_number)


@given(u'I run the validation process on {question_code} for the "{period_type}" {period} with {period_value}')
@when(u'I run the validation process on {question_code} for the "{period_type}" {period} with {period_value}')
def step_impl(context, question_code, period_type, period, period_value):
    context.question_code = question_code
    if period_type == 'previous period':
        page = ContributorSearchPage(context.driver)
        page.select_the_reference_view_form(context.reference_number, period)
        context.land_page = SandAndGravelLandDetails(context.driver)
        context.previous_period_value = period_value
        context.land_page.validate_the_previous_period_details(context.question_code, context.previous_period_value)
    elif period_type == 'current period':
        page = ContributorSearchPage(context.driver)
        page.select_the_reference_view_form(context.reference_number, period)
        context.land_page = SandAndGravelLandDetails(context.driver)
        context.current_period_value = period_value
        context.land_page.validate_the_current_period_details(context.question_code, context.current_period_value)


@then(u'the validation should return {result} if the absolute difference between the periods doesnt meet the {threshold} value')
def step_impl(context, result, threshold):
    context.land_page.check_the_threshold_value(context.previous_period_value, context.current_period_value, threshold)


@then(u'the form status should change to {status_type}')
def step_impl(context, status_type):
    context.land_page.check_validation_message()
    status = context.land_page.check_status(status_type)
    assert status.text.lower() == status_type.lower()
