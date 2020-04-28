from behave import given, when, then
from pages.contributor_search_page import ContributorSearchPage
from pages.sand_and_gravel_land_details_page import SandAndGravelLandDetails
from pages.search_by_page import SearchByPage


@given(u'As a BMI user I want to set the search criteria options for the forms returned by the contributor')
def step_impl(context):
    page = SearchByPage(context.driver)
    page.set_search_criteria_options()


@given(u'I search for the survey with {reference} for previous period {period}')
def step_impl(context, reference, period):
    context.search_page = ContributorSearchPage(context.driver)
    context.search_page.select_the_reference_view_form(reference, period)


@given(u'I run the validation process on {question_code} for previous period with {previous_value}')
def step_impl(context, question_code, previous_value):
    context.page = SandAndGravelLandDetails(context.driver)
    context.page.previous_value = previous_value
    context.page.validate_the_previous_period_details(question_code, context.page.previous_value)


@when(u'I search for the survey with {reference} for current period {period}')
def step_impl(context, reference, period):
    context.search_page.select_the_reference_view_form(reference, period)


@when(u'I run the validation process on {question_code} for current period with {current_value}')
def step_impl(context, question_code, current_value):
    context.page.current_value = current_value
    context.page.validate_the_current_period_details(question_code, context.page.current_value)


@then(u'the validation should return {result} if the absolute difference between the periods doesnt meet the {threshold} value')
def step_impl(context, result, threshold):
    threshold_result = context.page. \
        check_threshold_value(context.page.previous_value,
                              context.page.current_value, threshold)
    assert threshold_result == result


@then(u'the form status should change to {status_type}')
def step_impl(context, status_type):
    validation_message = context.page.get_validation_message()
    assert validation_message == 'This has changed significantly since the last submission'
    status = context.page.get_status(status_type)
    assert status.lower() == status_type.lower()
