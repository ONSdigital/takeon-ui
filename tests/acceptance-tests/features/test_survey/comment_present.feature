Feature: Test Survey - Comment Present(Question vs Value) Validation rule

  Background:
    Given As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: LU-6403 - Comment Present Validation test survey
    Given I search for the survey "999A" with <reference> for the period <period>
    When I submit the comment <comment> for question <question>
    And I trigger the validation process
    Then the <validation> message should <isValidationExists> displayed
    Examples:
      | period | reference   | comment | question | validation                               | isValidationExists |
      | 201801 | 12345678003 | 12345   | Q7       | There is a comment from this contributor | be                 |
      | 201801 | 12345678003 | blank   | Q7       | There is a comment from this contributor | not be             |
      | 201801 | 12345678003 | 2       | Q8       | There is a comment from this contributor | be                 |
      | 201801 | 12345678003 | blank   | Q8       | There is a comment from this contributor | not be             |
      | 201801 | 12345678003 | -2      | Q8       | There is a comment from this contributor | not be             |
