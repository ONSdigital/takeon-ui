Feature: Test Survey - Get Data from database

  Background:
    Given As a Business Survey user I set the search criteria options for the forms returned by the contributor

  Scenario: SPP-765 - get test survey from ids from database
    Given I have the query to "get the survey details with status form sent out" for the test survey "999A"
    When I query the database
    Then I should able to get back the reference,period details for that survey
