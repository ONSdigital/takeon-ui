from behave import given, when, then

from pages.rsi.rsi_date_adjusted_response_validation import RsiDateAdjustedResponseValidation
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
        RsiContributorDetailsPage().submit_sales_values(context.period, context.period_type, context.internet_sales,
                                                        context.total_sales)
    else:
        TestSurveyContributorDetailsPage().submit_sales_values(context.period_type, context.internet_sales,
                                                               context.total_sales)


@when(u'I validate {validation_type} current period details')
def validate_the_current_period_details(context, validation_type=None):
    if context.survey == '023':
        RsiContributorDetailsPage().validate_the_current_period_details(context.period, context.current_internet_sales,
                                                                        context.total_sales)
    else:
        TestSurveyContributorDetailsPage().validate_the_current_period_details(validation_type,
                                                                               context.current_internet_sales)


@when(u'I validate the current period details for {factor} factor type')
def current_period_factor_type(context, factor):
    if context.survey == '023' or context.survey == '999A':
        context.factor_type = factor


@given(u'I have the contributor responses returned for {days_returned} as compared to {actual_days_returned}')
def contributor_response(context, days_returned, actual_days_returned):
    context.days_returned = days_returned
    context.actual_days_returned = actual_days_returned


@given(u'the period start date set as {period_start_date} with period end date as {period_end_date}')
def period_dates(context, period_start_date, period_end_date):
    RsiDateAdjustedResponseValidation().submit_period_dates(context.period, period_start_date, period_end_date)


@then(u'check the adjusted response values for {dates_range} should be {adjusted_response} as expected response')
def check_adjusted_responses(context, dates_range, adjusted_response):
    context.dates_range = dates_range
    context.adjusted_response = adjusted_response
    RsiDateAdjustedResponseValidation().check_adjusted_responses(dates_range, context.values, adjusted_response)
