Feature: Bricks Survey - Comment Present(Question vs Value) Validation rule

  Background:
    Given As a BMI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: LU-6531 - Comment Present Validation Bricks survey on form 4
    Given I search for the survey "0074" with <reference> for the period <period>
    When I submit the "comment" <comment> for question <question>
    And I trigger the validation process
    Then the <validation> message should <isValidationExists> displayed
    Examples:
      | period | reference   | comment | question | validation                               | isValidationExists |
      | 201905 | 49900229065 | 12345   | Q145     | There is a comment from this contributor | not be             |
      | 201905 | 49900229065 | blank   | Q145     | There is a comment from this contributor | not be             |
      | 201905 | 49900229065 | 2       | Q145     | There is a comment from this contributor | be                 |
      | 201905 | 49900229065 | blank   | Q146     | There is a comment from this contributor | not be             |
      | 201905 | 49900229065 | 1       | Q146     | There is a comment from this contributor | not be             |
      | 201905 | 49900229065 | 2       | Q146     | There is a comment from this contributor | be                 |
