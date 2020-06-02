from behave import given, when

from pages.contributor_search_page import ContributorSearchPage
from pages.search_by_page import SearchByPage


@given(u'As a {survey} user I set the search criteria options for the forms returned by the contributor')
def step_impl(context, survey):
    context.survey = survey
    SearchByPage().set_search_criteria_options()


@given(u'I search for the {survey} with {reference} for the period {period}')
@given(u'I search for the survey "{survey}" with {reference} for the period {period}')
@when(u'I search for the {survey} with {reference} for the period {period}')
@when(u'I search for the survey "{survey}" with {reference} for the period {period}')
def step_impl(context, survey, reference, period):
    context.survey = survey
    context.contributor_page = ContributorSearchPage()
    context.contributor_page.select_the_reference_view_form(context.survey, reference, period)
