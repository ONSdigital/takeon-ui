from behave import given, when
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


@when(u'I validate the current period details')
def step_impl(context):
    if context.survey == '0023':
        RsiContributorDetailsPage().validate_the_current_period_details(context.internet_sales_value)
    else:
        TestSurveyContributorDetailsPage().validate_the_current_period_details(context.internet_sales_value)
