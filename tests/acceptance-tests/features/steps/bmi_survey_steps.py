from behave import given, when, then
from pages.bmi.blocks_survey_details_page import BlocksSurveyDetailsPage
from pages.bmi.bricks_survey_details_page import BricksSurveyDetailsPage
from pages.bmi.sand_and_gravel_land_marine_details_page import SandGravelLandAndMarineDetailsPage
from pages.common.contributor_details_page import ContributorDetailsPage


@given(u'I run the validation process on {question_codes} with {period_value}')
@when(u'I run the validation process on {question_codes} with {period_value}')
@given(u'I run the validation process with {period_value}')
@when(u'I run the validation process with {period_value}')
def step_impl(context, period_value,question_codes=None):
    if not question_codes:
        question_codes = context.question_codes
    page = ContributorDetailsPage()
    if context.period_type == "previous":
        context.previous_period_value = period_value
        page.validate_the_previous_period_details(question_codes, context.previous_period_value)
    elif context.period_type == "current":
        context.question_codes = question_codes
        context.current_period_value = period_value
        page.validate_the_current_period_details(context.question_codes, context.current_period_value)


@when(u'I change the {existing_value} to {new_value} for all the question codes')
def step_impl(context, existing_value, new_value):
    context.question_codes = 0
    if context.survey == '073':
        BlocksSurveyDetailsPage().submit_the_values_for_blocks_survey_question_codes(existing_value, new_value)

    elif context.survey == '074':
        BricksSurveyDetailsPage().submit_the_values_for_bricks_survey_question_codes(existing_value,
                                                                                     new_value)
    else:
        SandGravelLandAndMarineDetailsPage().submit_the_values_for_survey_question_codes(context.survey, existing_value,
                                                                                         new_value)


@when(u'I change the {existing_value} to {new_value} for the question codes')
def step_impl(context, existing_value, new_value):
    context.codes = []
    for row in context.table.rows:
        for cell in row.cells:
            context.codes.append(cell)
    if context.survey == '066':
        SandGravelLandAndMarineDetailsPage().submit_the_numeric_fields_values_for_survey(context.codes,
                                                                                         context.survey,
                                                                                         existing_value, new_value)
    elif context.survey == '076':
        SandGravelLandAndMarineDetailsPage().submit_the_numeric_fields_values_for_survey(context.codes,
                                                                                         context.survey,
                                                                                         existing_value,
                                                                                         new_value)
    elif context.survey == '074':
        BricksSurveyDetailsPage().submit_the_numeric_fields_values_for_survey(context.codes,
                                                                              context.survey, existing_value,
                                                                              new_value)
    elif context.survey == '073':
        BlocksSurveyDetailsPage().submit_the_numeric_fields_values_for_survey(context.codes,
                                                                              context.survey, existing_value,
                                                                              new_value)


@then(u'the fixed validation should {is_validation_exists} exists')
def step_impl(context, is_validation_exists):
    if context.survey == '066':
        SandGravelLandAndMarineDetailsPage().check_numeric_fields_fixed_validations_exists(context.survey,
                                                                                           is_validation_exists)
    elif context.survey == '076':
        SandGravelLandAndMarineDetailsPage().check_numeric_fields_fixed_validations_exists(context.survey,
                                                                                           is_validation_exists)
    elif context.survey == '073':
        SandGravelLandAndMarineDetailsPage().check_numeric_fields_fixed_validations_exists(context.survey,
                                                                                           is_validation_exists)
    elif context.survey == '074':
        BricksSurveyDetailsPage().check_numeric_fields_fixed_validations_exists(
            is_validation_exists)


@then(u'the fixed validation message {validation_message} should {is_validation_exists} displayed')
def step_impl(context, validation_message, is_validation_exists):
    if context.survey == '073':
        BlocksSurveyDetailsPage().check_fixed_validations_exists(context.survey, validation_message,
                                                                 is_validation_exists)
    elif context.survey == '074':
        BricksSurveyDetailsPage().check_fixed_validations_exists(context.survey, validation_message,
                                                                 is_validation_exists)
    elif context.survey == '076':
        SandGravelLandAndMarineDetailsPage().check_fixed_validations_exists(context.survey, validation_message,
                                                                            is_validation_exists)


@then(
    u'the validation should return {result} if the "{validation_check}"')
def step_impl(context, result, validation_check):
    page = ContributorDetailsPage()

    if validation_check == 'values are not equal':
        page.check_values_are_not_equal(context.question_codes, context.previous_period_value,
                                        context.current_period_value, result)
