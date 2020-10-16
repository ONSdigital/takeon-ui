Feature: Test Survey - Historic Data

  Background:
    Given As a Business Survey user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: SPP-95 - Check Historic Data matches with Current Period Data
    Given I search for the survey "999A" with <reference> for the current period <period>
    And I submit the "current data" <values> for questions
      | question_codes |
      | Q1             |
      | Q2             |
    And I trigger the validation process
    Then the values <values> should be matching to the corresponding questions on historic data
    Examples:
      | reference   | period | values |
      | 12345678037 | 201801 | 1,2    |

  Scenario Outline: SPP-95 - Check Historic Data number of back periods
    Given I search for the <survey> with reference <reference>
    And I have all the back period details including the current period <period>
    When I switch to the "historic data" tab on the contributor details page
    Then I should be able to view all the periods in historic data
    Examples:
      | survey | reference   | period |
      | 999A   | 12345678037 | 201801 |
    