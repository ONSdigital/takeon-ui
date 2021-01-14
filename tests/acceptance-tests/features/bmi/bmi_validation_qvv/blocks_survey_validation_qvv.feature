Feature: Blocks Survey - Comment Present(Question vs Value) Validation rule

  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a BMI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: LU-6531 - Comment Present Validation Blocks survey on form 3
    Given I search for the survey "073" with <reference> for the current period <period>
    When I submit the "comment" <comment> for question <question>
    And I trigger the validation process
    Then the "qvv validation" message should <isValidationExists> displayed
    Examples:
      | period | reference   | comment | question | isValidationExists |
      | 201905 | 12000228645 | 12345   | Q145     | not be             |
      | 201905 | 12000228645 | blank   | Q145     | not be             |
      | 201905 | 12000228645 | 2       | Q145     | be                 |
      | 201905 | 12000228645 | blank   | Q146     | not be             |
      | 201905 | 12000228645 | 1       | Q146     | not be             |
      | 201905 | 12000228645 | 2       | Q146     | be                 |
