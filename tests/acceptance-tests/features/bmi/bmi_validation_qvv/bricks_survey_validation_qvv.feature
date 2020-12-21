Feature: Bricks Survey - Comment Present(Question vs Value) Validation rule

  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a BMI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: LU-6531 - Comment Present Validation Bricks survey on form 4
    Given I search for the survey "074" with <reference> for the current period <period>
    When I submit the "comment" <comment> for question <question>
    And I trigger the validation process
    Then the "qvv validation" message should <isValidationExists> displayed
    Examples:
      | period | reference   | comment | question | isValidationExists |
      | 201905 | 49900229065 | 12345   | Q145     | not be             |
      | 201905 | 49900229065 | blank   | Q145     | not be             |
      | 201905 | 49900229065 | 2       | Q145     | be                 |
      | 201905 | 49900229065 | blank   | Q146     | not be             |
      | 201905 | 49900229065 | 1       | Q146     | not be             |
      | 201905 | 49900229065 | 2       | Q146     | be                 |
