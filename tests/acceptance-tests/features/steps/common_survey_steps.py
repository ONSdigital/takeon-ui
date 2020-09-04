from behave import given, when, then
from pages.common.contributor_details_page import ContributorDetailsPage
from pages.common.contributor_search_page import ContributorSearchPage
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


@given(u'I search for the {survey} with {reference} for the {period_type} period {period}')
@given(u'I search for the survey "{survey}" with {reference} for the {period_type} period {period}')
@given(
    u'I search for the survey "{survey}" with {reference} for the {period_type} period {period} with SIC code {sic_code}')
@when(u'I search for the survey "{survey}" with {reference} for the {period_type} period {period}')
@when(u'I search for the {survey} with {reference} for the period {period}')
def step_impl(context, reference, survey, period_type, period, sic_code=None):
    context.survey = survey
    context.period_type = period_type
    context.contributor_page = ContributorSearchPage()
    context.contributor_page.select_the_reference_view_form(context.survey, reference, period, sic_code)


@given(u'I submit the "{value_type}" {values} for questions')
def step_impl(context, value_type, values):
    context.question_codes = []
    for row in context.table.rows:
        for cell in row.cells:
            context.question_codes.append(cell)
    if context.survey == '999A':
        TestSurveyContributorDetailsPage().submit_the_sales_values_for_survey(context.survey, context.question_codes,
                                                                              values)
    else:
        ContributorDetailsPage().submit_values_for_survey_questions(context.survey, context.question_codes, values)


@given(u'I submit the "{value_type}" {comment_value} for question {question}')
@when(u'I submit the "{value_type}" {comment_value} for question {question}')
def step_impl(context, value_type, comment_value, question):
    context.question_codes = question.upper()
    if context.survey == '999A':
        TestSurveyContributorDetailsPage().submit_question_value(value_type, comment_value, question)
    else:
        ContributorDetailsPage().submit_question_value(context.survey, value_type, comment_value, question)


@when(u'I trigger the validation process')
def step_impl(context):
    ContributorDetailsPage().save_the_application()


@when(u'I run the validation process for {question_value} against the {derived_value}')
@when(u'I run the validation process against the {derived_value}')
def step_impl(context, derived_value, question_value=None):
    if context.survey == '023':
        context.total_turnover_value = question_value
        RsiContributorDetailsPage().run_the_validation_process(question_value, derived_value)
    elif context.survey == '999A':
        context.total_turnover_value = 0
        TestSurveyContributorDetailsPage().run_the_validation_process(derived_value)
    else:
        context.comparison_value_one = question_value
        context.comparison_value_two = derived_value

        context.codes = []
        for row in context.table.rows:
            for cell in row.cells:
                context.codes.append(cell)
        context.question_code = context.codes
        ContributorDetailsPage().run_the_validation_process(context.question_code, question_value, derived_value,
                                                            context.survey)


@then(u'the {validation_message} message should {is_validation_exists} displayed')
@then(u'the "{validation_message}" message should {is_validation_exists} displayed')
@then(u'the {validation_message} message should {is_validation_exists} displayed for question code "{question_codes}"')
@then(
    u'the "{validation_message}" message should {is_validation_exists} displayed for question code "{question_codes}"')
def step_impl(context, validation_message, is_validation_exists, question_codes=None):
    if not question_codes:
        question_codes = context.question_codes
    page = ContributorDetailsPage()
    page.check_validation_message(context.survey, question_codes, validation_message,
                                  is_validation_exists)


@then(u'the {validation_message} message should {is_validation_exists} displayed for question codes')
@then(u'the "{validation_message}" message should {is_validation_exists} displayed for question codes')
def step_impl(context, validation_message, is_validation_exists):
    if context.table is not None:
        context.question_codes = []
        for row in context.table.rows:
            for cell in row.cells:
                context.question_codes.append(cell)

    ContributorDetailsPage().check_multiple_questions_validation_messages(context.survey, context.question_codes,
                                                                          validation_message,
                                                                          is_validation_exists)


@then(
    u'the validation should return {result} if the "{validation_check}" {operator_type} threshold value {threshold_value}')
def step_impl(context, result, validation_check, operator_type, threshold_value):
    page = ContributorDetailsPage()
    if validation_check == 'turnover ratio is':
        page.check_turnover_ratio(operator_type, context.internet_sales,
                                  context.total_sales, threshold_value, result)

    elif validation_check == 'absolute difference between the values are':

        if context.survey == '023':
            rsi_page = RsiContributorDetailsPage()
            context.value_one = context.total_turnover_value
            context.value_two = rsi_page.get_derived_question_value()
        elif context.survey == '999A':
            test_survey_page = TestSurveyContributorDetailsPage()
            context.value_one = context.total_turnover_value
            context.value_two = test_survey_page.get_derived_question_value()
        else:
            context.value_one = context.comparison_value_one
            context.value_two = context.comparison_value_two

        page.check_absolute_difference_validation(operator_type, context.value_one,
                                                  context.value_two, threshold_value, result)

    elif validation_check == 'period on period ratio of ratios movement is':
        RsiContributorDetailsPage().check_pop_ratio_of_ratios_validation(context.factor_type, operator_type,
                                                                         threshold_value, result)


@when(u'I override the validation for the question {question}')
def step_impl(context, question):
    if not question:
        question = context.question_codes
    page = ContributorDetailsPage()
    page.override_the_validation(question)


@then(u'the validation message should change to {override_message}')
def step_impl(context, override_message):
    page = ContributorDetailsPage()
    page.check_the_override_message(context.question_codes, override_message)
