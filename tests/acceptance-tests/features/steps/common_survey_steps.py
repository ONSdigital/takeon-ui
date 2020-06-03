from behave import given, when, then

from pages.blocks_survey_details_page import BlocksSurveyDetailsPage
from pages.bricks_survey_details_page import BricksSurveyDetailsPage
from pages.contributor_details_page import ContributorDetailsPage
from pages.contributor_search_page import ContributorSearchPage
from pages.sand_and_gravel_land_details_page import SandGravelLandAndMarineDetailsPage
from pages.search_by_page import SearchByPage


@given(u'As a {survey} user I set the search criteria options for the forms returned by the contributor')
def step_impl(context, survey):
    context.survey = survey
    SearchByPage().set_search_criteria_options()


@given(u'I search for the {survey} with {reference} for the period {period}')
@given(u'I search for the survey "{survey}" with {reference} for the period {period}')
@when(u'I search for the {survey} with {reference} for the period {period}')
@when(u'I search for the survey "{survey}" with {reference} for the period {period}')
def step_impl(context, survey, reference, period):
    context.survey = survey
    context.contributor_page = ContributorSearchPage()
    context.contributor_page.select_the_reference_view_form(context.survey, reference, period)


@when(u'I submit the comment {comment_value} about reason for turnover changes')
def step_impl(context, comment_value):
    if context.survey == '0023':
        pass
    else:
        pass


@when(u'I trigger the validation process')
def step_impl(context):
    ContributorDetailsPage().save_the_application()


@then(u'the {validation_message} message should {is_validation_exists} displayed')
def step_impl(context, validation_message, is_validation_exists):
    if context.survey == '0073':
        BlocksSurveyDetailsPage().check_fixed_validations_exists(context.survey, validation_message,
                                                                 is_validation_exists)
    elif context.survey == '0074':
        BricksSurveyDetailsPage().check_fixed_validations_exists(context.survey, validation_message,
                                                                 is_validation_exists)
    elif context.survey == '0076':
        SandGravelLandAndMarineDetailsPage().check_fixed_validations_exists(context.survey, validation_message,
                                                                            is_validation_exists)
    elif context.survey == '0023':
        pass
