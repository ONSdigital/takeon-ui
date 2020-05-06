from behave import given, when, then
from pages.contributor_search_page import ContributorSearchPage
from pages.sand_and_gravel_land_details_page import SandAndGravelLandDetails
from pages.search_by_page import SearchByPage


@given(u'As a BMI user I set the search criteria options for the forms returned by the contributor')
def step_impl(context):
    SearchByPage().set_search_criteria_options()


@given(u'I search for the {survey} with {reference} for the period {period}')
@when(u'I search for the {survey} with {reference} for the period {period}')
def step_impl(context, survey, reference, period):
    context.contributor_page = ContributorSearchPage()
    context.contributor_page.select_the_reference_view_form(survey, reference, period)


@given(u'I run the validation process on {question_code} for {period_type} period with {period_value}')
@when(u'I run the validation process on {question_code} for {period_type} period with {period_value}')
def step_impl(context, period_type, question_code, period_value):
    context.sgl_page = SandAndGravelLandDetails()
    if period_type == "previous":
        context.previous_period_value = period_value
        context.sgl_page.validate_the_previous_period_details(question_code, context.previous_period_value)
    elif period_type == "current":
        context.current_period_value = period_value
        context.sgl_page.validate_the_current_period_details(question_code, context.current_period_value)


@when(u'I change the {existing_value} to {new_value} for all the question codes')
def step_impl(context, existing_value, new_value):
    SandAndGravelLandDetails().submit_the_values_for_all_question_codes(existing_value, new_value)


@when(u'I trigger the validation process')
def step_impl(context):
    SandAndGravelLandDetails().save_the_application()


@then(u'the {validation_message} message should {is_validation_exists} displayed')
def step_impl(context, validation_message, is_validation_exists):
    error_msg_elements = SandAndGravelLandDetails().get_the_validation_messages_for_all_question_codes()
    fixed_msg_elements = SandAndGravelLandDetails().get_the_fixed_validation_messages_for_all_question_codes()

    for i in range(0, len(error_msg_elements)):
        for j in range(0, len(fixed_msg_elements)):
            if len(fixed_msg_elements) > 0:
                error_msg_ele = error_msg_elements[i]
                fixed_ele = fixed_msg_elements[j]
                if validation_message in fixed_ele.text and validation_message not in error_msg_ele.text:
                    assert is_validation_exists == 'be'
                elif validation_message not in fixed_ele.text and validation_message not in error_msg_ele.text:
                    assert is_validation_exists == 'not be'


@then(
    u'the validation should return {result} if the absolute difference between the periods doesnt meet the {threshold_value}')
def step_impl(context, result, threshold_value):
    previous_value = context.previous_period_value
    current_value = context.current_period_value
    result_value = SandAndGravelLandDetails().check_threshold_value(previous_value, current_value)
    if result_value > int(threshold_value):
        assert True
    else:
        assert False


@then(u'the form status should change to {status_type}')
def step_impl(context, status_type):
    validation_message = SandAndGravelLandDetails().get_validation_message()
    assert validation_message == 'This has changed significantly since the last submission'
    status = SandAndGravelLandDetails().get_status(status_type)
    assert status.lower() == status_type.lower()
