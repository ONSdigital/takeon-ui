from behave import given, when, then

from pages.test_survey_contributor_details_page import TestSurveyContributorDetailsPage
from pages.rsi_contributor_details_page import RsiContributorDetailsPage


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


@when(u'I validate the current period details')
def step_impl(context):
    if context.survey == '0023':
        RsiContributorDetailsPage().validate_the_current_period_details(context.internet_sales_value)
    else:
        TestSurveyContributorDetailsPage().validate_the_current_period_details(context.internet_sales_value)


@then(
    u'the validation should return {result} if the turnover ratio is {operator_type} threshold value {threshold_value}')
def step_impl(context, result, operator_type, threshold_value):
    inter_sales = int(context.pp_internet_sales)
    thre_val = float(threshold_value[:-1]) / 100
    total_sales = thre_val * int(context.pp_total_sales)

    if context.survey == '0023':
        page = RsiContributorDetailsPage()
    else:
        page = TestSurveyContributorDetailsPage()

    if operator_type == 'less than' or operator_type == 'equal to':
        if inter_sales < total_sales or inter_sales == total_sales:
            assert result == 'false'
            is_message_exists = page.check_validation_message()
            assert str(is_message_exists).lower() == 'false'
    elif operator_type == 'greater than':
        if inter_sales > total_sales:
            assert result == 'true'
            is_message_exists = page.check_validation_message()
            if not is_message_exists:
                assert False, 'validations triggered but no validation message exists'