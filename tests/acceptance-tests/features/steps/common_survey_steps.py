from behave import given, when, then

from pages.blocks_survey_details_page import BlocksSurveyDetailsPage
from pages.bricks_survey_details_page import BricksSurveyDetailsPage
from pages.contributor_details_page import ContributorDetailsPage
from pages.contributor_search_page import ContributorSearchPage
from pages.sand_and_gravel_land_details_page import SandGravelLandAndMarineDetailsPage
from pages.search_by_page import SearchByPage
from pages.rsi_contributor_details_page import RsiContributorDetailsPage


@given(u'As a {survey} user I set the search criteria options for the forms returned by the contributor')
def step_impl(context, survey):
    context.survey = survey
    SearchByPage().set_search_criteria_options()


@given(u'I search for the {survey_value} with reference {reference}')
def step_impl(context, reference, survey_value=None, period=None):
    context.contributor_page = ContributorSearchPage()
    if survey_value == 'survey' and not period:
        context.contributor_page.submit_search_details(reference, 'empty', 'empty')
    elif not period:
        context.contributor_page.submit_search_details(reference, 'empty', survey_value)


@given(u'I search for the {survey} with {reference} for the period {period}')
@when(u'I search for the {survey} with {reference} for the period {period}')
def step_impl(context, reference, survey, period):
    context.survey = survey
    context.contributor_page = ContributorSearchPage()
    context.contributor_page.select_the_reference_view_form(context.survey, reference, period)


@when(u'I submit the comment {comment_value} about reason for turnover changes')
def step_impl(context, comment_value):
    if context.survey == '0023':
        RsiContributorDetailsPage().submit_comment_value(comment_value)


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
        RsiContributorDetailsPage().check_comment_present_val_msg(validation_message, is_validation_exists)
