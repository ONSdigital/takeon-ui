from behave import given, when
from pages.test_survey.test_survey_contributor_details_page import TestSurveyContributorDetailsPage
from pages.rsi.rsi_contributor_details_page import RsiContributorDetailsPage


@given(u'the current period sales value is "{current_internet_sales_val}"')
def current_period_sales(context, current_internet_sales_val):
    context.current_internet_sales = current_internet_sales_val


@given(u'has the internet sales value {internet_sales} out of total turnover value {total_sales}')
@when(u'has the internet sales value {internet_sales} out of total turnover value {total_sales}')
def submit_sales_values(context, internet_sales, total_sales):
    context.internet_sales = internet_sales
    context.total_sales = total_sales
    context.values = None
    if context.survey == '023':
        RsiContributorDetailsPage().submit_sales_values(context.period_type, context.internet_sales,
                                                        context.total_sales)
    else:
        TestSurveyContributorDetailsPage().submit_sales_values(context.period_type, context.internet_sales,
                                                               context.total_sales)


@when(u'I validate {validation_type} current period details')
def validate_the_current_period_details(context, validation_type=None):
    if context.survey == '023':
        RsiContributorDetailsPage().validate_the_current_period_details(context.current_internet_sales,
                                                                        context.total_sales)
    else:
        TestSurveyContributorDetailsPage().validate_the_current_period_details(validation_type,
                                                                               context.current_internet_sales)


@when(u'I validate the current period details for {factor} factor type')
def current_period_factor_type(context, factor):
    if context.survey == '023' or context.survey == '999A':
        context.factor_type = factor
