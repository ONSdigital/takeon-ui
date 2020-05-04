from behave import given, when, then
from pages.contributor_search_page import ContributorSearchPage
from pages.sand_and_gravel_land_details_page import SandAndGravelLandDetails
from pages.search_by_page import SearchByPage


@given(u'As a BMI user I set the search criteria options for the forms returned by the contributor')
def step_impl(context):
    page = SearchByPage(context.driver)
    page.set_search_criteria_options()


# @given(u'I search for the survey with {reference} for previous period {period}')
@given(u'I search for the {survey} with {reference} for period {period}')
@when(u'I search for the {survey} with {reference} for period {period}')
def step_impl(context, survey, reference, period):
    context.search_page = ContributorSearchPage(context.driver)
    context.search_page.select_the_reference_view_form(survey, reference, period)


@given(u'I run the validation process on {question_code} for {period_type} period with {period_value}')
@when(u'I run the validation process on {question_code} for {period_type} period with {period_value}')
def step_impl(context, period_type, question_code, period_value):
    context.page = SandAndGravelLandDetails(context.driver)
    if period_type == "previous":
        context.previous_period_value = period_value
        context.page.validate_the_previous_period_details(question_code, context.previous_period_value)
    elif period_type == "current":
        context.current_period_value = period_value
        context.page.validate_the_current_period_details(question_code, context.current_period_value)


@when(u'I change the {existing_value} to {new_value} for all the question codes')
def step_impl(context, existing_value, new_value):
    pass


@when(u'I trigger the validation process')
def step_impl(context):
    pass


@then(u'the {validation_message} message should {is_validation_exists} displayed')
def step_impl(context, validation_message, is_validation_exists):
    pass


@then(
    u'the validation should return {result} if the absolute difference between the periods doesnt meet the {threshold_value}')
def step_impl(context, result, threshold_value):
    previous_value = context.previous_period_value
    current_value = context.current_period_value
    threshold_result = context.page.check_threshold_value(previous_value, current_value, threshold_value)
    assert threshold_result == result


@then(u'the form status should change to {status_type}')
def step_impl(context, status_type):
    validation_message = context.page.get_validation_message()
    assert validation_message == 'This has changed significantly since the last submission'
    status = context.page.get_status(status_type)
    assert status.lower() == status_type.lower()
