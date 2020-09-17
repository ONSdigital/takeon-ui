Feature: Test Survey - Historic Data
  As a Business Survey Operator I need a view showing me historical data
  So that I can decide if a validation can be overridden


  Background:
    Given As a Business Survey user I set the search criteria options for the forms returned by the contributor

  Scenario: SPP-92 - View Historic Data
    Given I search for the survey "999A" with <reference> for the current period <period>
    When I switch to the "historic data" tab on the contributor details page
    Then I can able to view the questions and current period values
