Feature: Test Survey - Comment Present(Question vs Value) Validation rule

  Background:
    Given As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: LU-6403 - Comment Present Validation test survey
    Given I search for the survey "999A" with <reference> for the current period <period>
    When I submit the "comment" <comment> for question <question>
    And I trigger the validation process
    Then the "qvv validation" message should <isValidationExists> displayed
    Examples:
      | period | reference   | comment | question | isValidationExists |
      | 201801 | 12345678003 | 12345   | Q7       | be                 |
      | 201801 | 12345678003 | blank   | Q7       | not be             |
      | 201801 | 12345678003 | 2       | Q8       | be                 |
      | 201801 | 12345678003 | blank   | Q8       | not be             |
      | 201801 | 12345678003 | 1       | Q8       | not be             |
