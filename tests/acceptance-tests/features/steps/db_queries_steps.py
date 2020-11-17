from behave import given, when, then

from config_files.db_connect import DBConnect
from pages.common.contributor_search_page import ContributorSearchPage
from test_data.select_queries import SelectQueries


@given(u'I have the query to "{query_type}" for the test survey "{survey}"')
def query_the_db(context, query_type, survey):
    context.survey = survey
    context.query = SelectQueries().survey_query(query_type, survey)


@when(u'I query the database')
def connect_to_db(context):
    context.survey_details = DBConnect().db_select_query(context.query)


@then(u'I should able to get back the reference,period details for that survey')
def check_the_db_results(context):
    reference = context.survey_details[0]
    period = context.survey_details[1]
    ContributorSearchPage().select_the_reference_view_form(context.survey, reference, period, None)
