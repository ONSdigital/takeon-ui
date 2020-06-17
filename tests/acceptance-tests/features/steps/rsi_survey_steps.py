from behave import given, when, then

from base.reporting_helper import ReportingHelper
from pages.test_survey.test_survey_contributor_details_page import TestSurveyContributorDetailsPage
from pages.rsi.rsi_contributor_details_page import RsiContributorDetailsPage


@given(u'the current period sales value is {current_internet_sales_val}')
def step_impl(context, current_internet_sales_val):
    context.internet_sales_value = current_internet_sales_val


@given(u'has the internet sales value {internet_sales} out of total turnover value {total_sales}')
def step_impl(context, internet_sales, total_sales):
    context.pp_internet_sales = internet_sales
    context.pp_total_sales = total_sales
    if context.survey == '0023':
        RsiContributorDetailsPage().submit_pp_sales_values(internet_sales, total_sales)
    else:
        TestSurveyContributorDetailsPage().submit_pp_sales_values(internet_sales, total_sales)


@given(u'I submit the commodity {values} for questions')
def step_impl(context, values):
    context.codes = []
    for row in context.table.rows:
        for cell in row.cells:
            context.codes.append(cell)
    if context.survey == '0023':
        RsiContributorDetailsPage().submit_the_sales_values_for_survey(context.codes, values)


@when(u'I validate the current period details')
def step_impl(context):
    if context.survey == '0023':
        RsiContributorDetailsPage().validate_the_current_period_details(context.internet_sales_value)
    else:
        TestSurveyContributorDetailsPage().validate_the_current_period_details(context.internet_sales_value)


@then(
    u'the validation should return {result} if the "{validation_check}" {operator_type} threshold value {threshold_value}')
def step_impl(context, result, validation_check, operator_type, threshold_value):
    if context.survey == '0023':
        page = RsiContributorDetailsPage()
        total_turnover_value = int(context.total_turnover_value)
        derived_value = page.get_derived_question_value()
        context.comparison_val_one = abs(total_turnover_value - derived_value)
    else:
        page = TestSurveyContributorDetailsPage()
        context.comparison_val_one = abs(page.get_derived_question_value())

    if validation_check == 'turnover ratio is':
        context.comparison_val_one = int(context.pp_internet_sales)
        thre_val = float(threshold_value[:-1]) / 100
        context.comparison_val_two = thre_val * int(context.pp_total_sales)

    elif validation_check == 'absolute difference between the values are':
        context.comparison_val_two = int(threshold_value)

    if operator_type == 'less than' or operator_type == 'equal to':
        if context.comparison_val_one < context.comparison_val_two or context.comparison_val_one == context.comparison_val_two:
            ReportingHelper.check_values_matches('', result, 'false')
        elif operator_type == 'greater than':
            if context.comparison_val_one > context.comparison_val_two:
                ReportingHelper.check_values_matches('', result, 'true')
