Feature: Test Survey - Historic Data

  Background:
    Given As a Business Survey user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: SPP-92 - View Historic Data
    Given I search for the survey "999A" with <reference> for the current period <period>
    When I switch to the "historic data" tab on the contributor details page
    Then I can able to view the historic data
    Examples:
      | reference   | period |
      | 12345678002 | 201801 |
