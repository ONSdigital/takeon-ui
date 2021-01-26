from behave import given, when, then

from pages.common.contributor_details_page import ContributorDetailsPage
from pages.common.contributor_search_page import ContributorSearchPage
from pages.common.search_by_page import SearchByPage
from pages.rsi.rsi_contributor_details_page import RsiContributorDetailsPage
from pages.test_survey.test_survey_contributor_details_page import TestSurveyContributorDetailsPage


@given(u'As a {survey} user I set the search criteria options for the forms returned by the contributor')
def search_criteria(context, survey):
    context.survey = survey
    SearchByPage().set_search_criteria_options()


@given(u'I search for the {survey_value} with reference {reference}')
def submit_search_details(context, reference, survey_value=None, period=None):
    context.survey = survey_value
    context.reference = reference
    context.contributor_page = ContributorSearchPage()
    if survey_value == 'survey' and not period:
        context.contributor_page.submit_search_details(reference, 'empty', 'empty')
    elif not period:
        context.contributor_page.submit_search_details(reference, 'empty', survey_value)


@given(u'I search for the {survey} with {reference} for the {period_type} period {period}')
@given(u'I search for the survey "{survey}" with {reference} for the {period_type} period {period}')
@given(
    u'I search for the survey "{survey}" with {reference} for the {period_type} period {period} '
    u'with SIC code {sic_code}')
@when(u'I search for the survey "{survey}" with {reference} for the {period_type} period {period}')
@when(u'I search for the {survey} with {reference} for the period {period}')
def select_the_reference_form(context, reference, survey, period_type, period, sic_code=None):
    context.survey = survey
    context.period_type = period_type
    context.contributor_page = ContributorSearchPage()
    context.contributor_page.select_the_reference_view_form(context.survey, reference, period, sic_code)


@given(u'I submit the "{value_type}" {values} for questions')
def submit_the_question_data_values(context, value_type, values):
    context.question_codes = []
    for row in context.table.rows:
        for cell in row.cells:
            context.question_codes.append(cell)
    context.values = values
    ContributorDetailsPage().submit_values_for_survey_questions(context.survey, context.question_codes, values)


@given(u'I submit the "{value_type}" {comment_value} for question {question}')
@when(u'I submit the "{value_type}" {comment_value} for question {question}')
def submit_the_question_type_values(context, value_type, comment_value, question):
    context.question_codes = question.upper()
    context.values = comment_value
    ContributorDetailsPage().submit_question_value(context.survey, value_type, comment_value, question)


@given(u'I trigger the validation process')
@when(u'I trigger the validation process')
def trigger_the_validation(context):
    ContributorDetailsPage().save_the_application()


@given(u'I run the validation process for {question_value} against the {derived_value}')
@when(u'I run the validation process for {question_value} against the {derived_value}')
@when(u'I run the validation process against the {derived_value}')
def run_the_validation_process(context, derived_value, question_value=None):
    if context.survey == '023':
        context.total_turnover_value = question_value
        RsiContributorDetailsPage().run_the_validation_process(question_value, derived_value)

    elif context.survey == '999A' and context.table is None:
        context.comparison_value_one = question_value
        context.comparison_value_two = derived_value
        TestSurveyContributorDetailsPage().run_the_validation_process(context.comparison_value_one,
                                                                      context.comparison_value_two)
    else:
        context.comparison_value_one = question_value
        context.comparison_value_two = derived_value

        context.codes = []
        for row in context.table.rows:
            for cell in row.cells:
                context.codes.append(cell)
        context.question_code = context.codes
        ContributorDetailsPage().run_the_validation_process(context.question_code, question_value,
                                                            derived_value, context.survey)


@then(u'the "{validation_message}" message should {is_validation_exists} displayed')
def check_validation_message(context, validation_message, is_validation_exists, question_codes=None):
    if not question_codes:
        question_codes = context.question_codes
    page = ContributorDetailsPage()
    page.check_validation_message(context.survey, question_codes, validation_message,
                                  is_validation_exists)


@then(u'the "{comment}" {validation_message} message should {is_validation_exists} displayed')
@then(u'the {validation_message} message should {is_validation_exists} displayed for question codes')
@then(u'the "{validation_message}" message should {is_validation_exists} displayed for question codes')
@then(
    u'the "{validation_message}" message should {is_validation_exists} displayed for question code "{question_codes}"')
def check_multiple_validation_messages(context, validation_message, is_validation_exists, question_codes=None,
                                       comment=None):
    if not question_codes and comment:
        question_codes = context.question_codes
        ContributorDetailsPage().check_multiple_comment_text_messages(context.survey, question_codes, context.values)
    elif not question_codes:
        question_codes = context.question_codes
        ContributorDetailsPage().check_multiple_questions_validation_messages(context.survey, question_codes,
                                                                              validation_message,
                                                                              is_validation_exists)
    else:
        ContributorDetailsPage().check_multiple_questions_validation_messages(context.survey, question_codes,
                                                                              validation_message,
                                                                              is_validation_exists)


@then(
    u'the validation should return {result} if the "{validation_check}" '
    u'{operator_type} threshold value {threshold_value}')
def check_validation_by_operator(context, result, validation_check, operator_type, threshold_value):
    page = ContributorDetailsPage()
    if validation_check == 'turnover ratio is':
        page.check_turnover_ratio(operator_type, context.internet_sales,
                                  context.total_sales, threshold_value, result)

    elif validation_check == 'absolute difference between the values are':

        if context.survey == '023':
            rsi_page = RsiContributorDetailsPage()
            context.value_one = context.total_turnover_value
            context.value_two = rsi_page.get_derived_question_value()
        else:
            context.value_one = context.comparison_value_one
            context.value_two = context.comparison_value_two

        page.check_absolute_difference_validation(operator_type, context.value_one,
                                                  context.value_two, threshold_value, result)

    elif validation_check == 'period on period ratio of ratios movement is':
        if context.survey == '023':
            RsiContributorDetailsPage().check_pop_ratio_of_ratios_validation(context.factor_type, operator_type,
                                                                             threshold_value, result)
        elif context.survey == '999A':
            TestSurveyContributorDetailsPage().check_pop_ratio_of_ratios_validation(context.factor_type, operator_type,
                                                                                    threshold_value, result)


@when(u'I override the validation for the question {question}')
def override_the_validation(context, question):
    if not question:
        question = context.question_codes
    else:
        context.question_codes = question
    page = ContributorDetailsPage()
    page.override_the_validation(question, 'override')


@then(u'the validation message should change to {override_message}')
@then(u'the validation message should change to "{override_message}"')
def check_override_validation_message(context, override_message):
    page = ContributorDetailsPage()
    page.check_the_override_message(context.survey, context.question_codes, override_message)


@then(u'the override checkbox should not be displayed for {question}')
def check_override_checkbox_displayed(context, question):
    page = ContributorDetailsPage()
    page.check_the_override_checkbox_displayed(question)
