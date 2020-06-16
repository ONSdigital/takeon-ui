from behave import given, when, then, use_step_matcher

from pages.bmi.blocks_survey_details_page import BlocksSurveyDetailsPage
from pages.bmi.bricks_survey_details_page import BricksSurveyDetailsPage
from pages.common.contributor_details_page import ContributorDetailsPage
from pages.common.contributor_search_page import ContributorSearchPage
from pages.bmi.sand_and_gravel_land_details_page import SandGravelLandAndMarineDetailsPage
from pages.common.search_by_page import SearchByPage
from pages.rsi.rsi_contributor_details_page import RsiContributorDetailsPage
from pages.test_survey.test_survey_contributor_details_page import TestSurveyContributorDetailsPage


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
@given(u'I search for the survey "{survey}" with {reference} for the period {period}')
@when(u'I search for the {survey} with {reference} for the period {period}')
@when(u'I search for the survey "{survey}" with {reference} for the period {period}')
def step_impl(context, reference, survey, period):
    context.survey = survey
    context.contributor_page = ContributorSearchPage()
    context.contributor_page.select_the_reference_view_form(context.survey, reference, period)


@when(u'I submit the comment {comment_value} for question {question}')
@when(u'I submit the comment {comment_value} for question "{question}"')
def step_impl(context, comment_value, question):
    context.question_code = question.upper()
    if context.survey == '0023':
        RsiContributorDetailsPage().submit_comment_value(comment_value, question)
    elif context.survey == '999A':
        TestSurveyContributorDetailsPage().submit_comment_value(comment_value, question)


@when(u'I trigger the validation process')
def step_impl(context):
    ContributorDetailsPage().save_the_application()


@then(u'the {validation_message} message should {is_validation_exists} displayed')
@then(u'the {validation_message} message should {is_validation_exists} displayed for question code "{question_code}"')
def step_impl(context, validation_message, is_validation_exists, question_code=None):
    if not question_code:
        question_code = context.question_code

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
    else:
        TestSurveyContributorDetailsPage().check_validation_msg(question_code, validation_message,
                                                                is_validation_exists)
