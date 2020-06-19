from behave import given, when, then

from base.reporting_helper import ReportingHelper
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


@given(u'I submit the commodity {values} for questions')
def step_impl(context, values):
    context.codes = []
    for row in context.table.rows:
        for cell in row.cells:
            context.codes.append(cell)
    if context.survey == '0023':
        RsiContributorDetailsPage().submit_the_sales_values_for_survey(context.codes, values)
    elif context.survey == '999A':
        TestSurveyContributorDetailsPage().submit_the_sales_values_for_survey(context.codes, values)


@when(u'I submit the comment {comment_value} for question {question}')
@when(u'I submit the comment {comment_value} for question "{question}"')
def step_impl(context, comment_value, question):
    context.question_code = question.upper()
    if context.survey == '0023':
        RsiContributorDetailsPage().submit_comment_value(comment_value, question)
    elif context.survey == '999A':
        TestSurveyContributorDetailsPage().submit_comment_value(comment_value, question)
    elif context.survey == '0066' or context.survey == '0076':
        SandGravelLandAndMarineDetailsPage().submit_comment_value(comment_value, question)


@when(u'I trigger the validation process')
def step_impl(context):
    ContributorDetailsPage().save_the_application()


@when(u'I run the validation process for {total_turnover_value} against the {derived_value}')
@when(u'I run the validation process against the {derived_value}')
def step_impl(context, derived_value, total_turnover_value=None):
    if context.survey == '0023':
        context.total_turnover_value = total_turnover_value
        RsiContributorDetailsPage().run_the_validation_process(total_turnover_value, derived_value)
    elif context.survey == '999A':
        context.total_turnover_value = 0
        TestSurveyContributorDetailsPage().run_the_validation_process(derived_value)


@then(u'the {validation_message} message should {is_validation_exists} displayed')
@then(u'the {validation_message} message should {is_validation_exists} displayed for question code "{question_code}"')
def step_impl(context, validation_message, is_validation_exists, question_code=None):
    if not question_code:
        question_code = context.question_code

    # if context.survey == '0073':
    #     BlocksSurveyDetailsPage().check_fixed_validations_exists(context.survey, validation_message,
    #                                                              is_validation_exists)
    # elif context.survey == '0074':
    #     BricksSurveyDetailsPage().check_fixed_validations_exists(context.survey, validation_message,
    #                                                              is_validation_exists)
    # elif context.survey == '0076' or context.survey == '0066':
    #     SandGravelLandAndMarineDetailsPage().check_fixed_validations_exists(context.survey, validation_message,
    #                                                                         is_validation_exists)
    # else:
    ContributorDetailsPage().check_validation_msg(question_code, validation_message,
                                                is_validation_exists)


@then(
    u'the validation should return {result} if the "{validation_check}" {operator_type} threshold value {threshold_value}')
def step_impl(context, result, validation_check, operator_type, threshold_value):
    if context.survey == '0023':
        page = RsiContributorDetailsPage()
    else:
        page = TestSurveyContributorDetailsPage()

    if validation_check == 'turnover ratio is':
        context.comparison_val_one = int(context.pp_internet_sales)
        thre_val = float(threshold_value[:-1]) / 100
        context.comparison_val_two = thre_val * int(context.pp_total_sales)
    elif validation_check == 'absolute difference between the values are':
        context.total_turnover_value = int(context.total_turnover_value)
        context.derived_value = page.get_derived_question_value()
        context.comparison_val_one = abs(context.total_turnover_value - context.derived_value)
        context.comparison_val_two = int(threshold_value)

    ReportingHelper.compare_the_values(operator_type, context.comparison_val_one, context.comparison_val_two, result)
