Feature: Test Survey - Get Data from database

  Background:
    Given As a Business Survey user I set the search criteria options for the forms returned by the contributor

  Scenario: SPP-765 - Get test survey details from database
    Given I have the query to "get the survey details with status form sent out" for the test survey "999A"
    When I query the database to get the reference,period details for that survey
    Then I should be able to search for the form with those survey details
