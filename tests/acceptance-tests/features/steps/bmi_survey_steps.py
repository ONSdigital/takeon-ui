from behave import given, when, then

from pages.blocks_survey_details_page import BlocksSurveyDetailsPage
from pages.bricks_survey_details_page import BricksSurveyDetailsPage
from pages.contributor_details_page import ContributorDetailsPage
from pages.contributor_search_page import ContributorSearchPage
from pages.sand_and_gravel_land_details_page import SandGravelLandAndMarineDetailsPage
from pages.search_by_page import SearchByPage


@given(u'As a BMI user I set the search criteria options for the forms returned by the contributor')
def step_impl(context):
    SearchByPage().set_search_criteria_options()


@given(u'I search for the {survey} with {reference} for the period {period}')
@when(u'I search for the {survey} with {reference} for the period {period}')
def step_impl(context, survey, reference, period):
    context.survey = survey
    context.contributor_page = ContributorSearchPage()
    context.contributor_page.select_the_reference_view_form(context.survey, reference, period)


@given(u'I run the validation process on {question_code} for {period_type} period with {period_value}')
@when(u'I run the validation process on {question_code} for {period_type} period with {period_value}')
def step_impl(context, period_type, question_code, period_value):
    context.sgl_page = SandGravelLandAndMarineDetailsPage()
    if period_type == "previous":
        context.previous_period_value = period_value
        context.sgl_page.validate_the_previous_period_details(question_code, context.previous_period_value)
    elif period_type == "current":
        context.current_period_value = period_value
        context.sgl_page.validate_the_current_period_details(question_code, context.current_period_value)


@when(u'I change the {existing_value} to {new_value} for all the question codes')
def step_impl(context, existing_value, new_value):
    if context.survey == '0073':
        BlocksSurveyDetailsPage().submit_the_values_for_blocks_survey_question_codes(existing_value, new_value)

    elif context.survey == '0074':
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
    if context.survey == '0066':
        SandGravelLandAndMarineDetailsPage().submit_the_numeric_fields_values_for_survey(context.codes,
                                                                                         context.survey,
                                                                                         existing_value, new_value)
    elif context.survey == '0076':
        SandGravelLandAndMarineDetailsPage().submit_the_numeric_fields_values_for_survey(context.codes,
                                                                                         context.survey,
                                                                                         existing_value,
                                                                                         new_value)
    elif context.survey == '0074':
        BricksSurveyDetailsPage().submit_the_numeric_fields_values_for_survey(context.codes,
                                                                              context.survey, existing_value,
                                                                              new_value)
    elif context.survey == '0073':
        BlocksSurveyDetailsPage().submit_the_numeric_fields_values_for_survey(context.codes,
                                                                              context.survey, existing_value,
                                                                              new_value)


@when(u'I trigger the validation process')
def step_impl(context):
    ContributorDetailsPage().save_the_application()


@then(u'the {validation_message} message should {is_validation_exists} displayed')
def step_impl(context, validation_message, is_validation_exists):
    if context.survey == '0073':
        BlocksSurveyDetailsPage().check_fixed_validations_exists(validation_message, is_validation_exists)
    elif context.survey == '0074':
        BricksSurveyDetailsPage().check_fixed_validations_exists(validation_message, is_validation_exists)
    else:
        SandGravelLandAndMarineDetailsPage().check_fixed_validations_exists(context.survey, validation_message,
                                                                            is_validation_exists)


@then(u'the fixed validation should {is_validation_exists} exists')
def step_impl(context, is_validation_exists):
    if context.survey == '0066':
        SandGravelLandAndMarineDetailsPage().check_numeric_fields_fixed_validations_exists(context.survey,
                                                                                           is_validation_exists)
    elif context.survey == '0076':
        SandGravelLandAndMarineDetailsPage().check_numeric_fields_fixed_validations_exists(context.survey,
                                                                                           is_validation_exists)
    elif context.survey == '0073':
        SandGravelLandAndMarineDetailsPage().check_numeric_fields_fixed_validations_exists(context.survey,
                                                                                           is_validation_exists)
    elif context.survey == '0074':
        BricksSurveyDetailsPage().check_numeric_fields_fixed_validations_exists(context.survey,
                                                                                is_validation_exists)


@then(
    u'the validation should return {result} if the absolute difference between the periods doesnt meet the {threshold_value}')
def step_impl(context, result, threshold_value):
    previous_value = context.previous_period_value
    current_value = context.current_period_value
    result_value = SandGravelLandAndMarineDetailsPage().check_threshold_value(previous_value, current_value)
    if result_value > int(threshold_value):
        assert True
    else:
        assert False


@then(u'the form status should change to {status_type}')
def step_impl(context, status_type):
    validation_message = SandGravelLandAndMarineDetailsPage().get_validation_message()
    assert validation_message == 'This has changed significantly since the last submission'
    status = SandGravelLandAndMarineDetailsPage().get_status()
    assert status.lower() == status_type.lower()
