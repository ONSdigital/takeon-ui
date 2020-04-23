from behave import given, when, then, model
from pages.contributor_search_page import ContributorSearchPage
from pages.search_by_page import SearchByPage


@given(u'As a BMI user I search for the form returned by the contributor with {reference_number} number')
def step_impl(context, reference_number):
    context.reference_number = reference_number
    page = SearchByPage(context.driver)
    page.select_search_by(context.reference_number)


@given(u'I run the validation process on {question_code} for the {period} with the {period_value}')
@when(u'I run the validation process on {questionCode} for the {period} with the {period_value}')
def step_impl(context, question_code, period_value):
    context.question_code = question_code
    page = ContributorSearchPage(context.driver)
    page.select_the_reference_view_form(context.referenceNumber)
    page.validate_the_previous_period_details(context.question_code, period_value)


@then(u'the validation should return {result} if the absolute difference between the periods doesnt meet the {threshold} value')
def step_impl(context, result, threshold):
    pass


@then(u'the form status should change to {status_type}')
def step_impl(context, status_type):
    pass
