from behave import given, when, then
from pages.common.contributor_details_page import ContributorDetailsPage


@given(u'I run the validation process on {question_codes} with {period_value}')
@when(u'I run the validation process on {question_codes} with {period_value}')
@given(u'I run the validation process with {period_value}')
@when(u'I run the validation process with {period_value}')
def run_the_validation_process(context, period_value, question_codes=None):
    if not question_codes:
        question_codes = context.question_codes
    page = ContributorDetailsPage()
    if context.period_type == "previous":
        context.comparison_value_one = period_value
        page.validate_the_previous_period_details(context.survey, context.period_start_date, question_codes,
                                                  context.comparison_value_one)
    elif context.period_type == "current":
        context.question_codes = question_codes
        context.comparison_value_two = period_value
        page.validate_the_current_period_details(context.survey, context.period_start_date, context.question_codes,
                                                 context.comparison_value_two)


@then(
    u'the validation should return {result} if the "{validation_check}"')
def check_validation(context, result, validation_check):
    page = ContributorDetailsPage()
    if validation_check == 'values are not equal':
        page.check_values_are_not_equal(context.question_codes, context.comparison_value_one,
                                        context.comparison_value_two, result)
    elif validation_check == 'period vs previous frequency period movement to or from zero':
        page.check_values_movement_to_or_from_zero(context.question_codes, context.comparison_value_one,
                                                   context.comparison_value_two, result)
