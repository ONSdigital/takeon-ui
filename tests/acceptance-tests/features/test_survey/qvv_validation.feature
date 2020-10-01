Feature: Test Survey - Question versus Value(QvV) Validation rule

  Background:
    Given As a Business Survey user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: SP-100 - Question versus Value Validation on test survey
    Given I search for the survey "999A" with <reference> for the current period <period>
    When I submit the "value" <value> for question <question>
    And I trigger the validation process
    Then the "qvv validation" message should <isValidationExists> displayed
    Examples:
      | period | reference   | value | question | isValidationExists |
      | 201712 | 12345678036 | 2     | Q8       | be                 |
      | 201712 | 12345678036 | blank | Q8       | not be             |
      | 201712 | 12345678036 | 1     | Q8       | not be             |


  Scenario Outline: SP-100 - Question versus Value Text Validation on test survey
    Given I search for the survey "999A" with <reference> for the current period <period>
    When I submit the "comment" <comment> for question <question>
    And I trigger the validation process
    Then the "qvv text validation" message should <isValidationExists> displayed
    Examples:
      | period | reference   | comment  | question | isValidationExists |
      | 201712 | 12345678036 | test-123 | Q30      | be                 |
      | 201712 | 12345678036 | test     | Q30      | be                 |
      | 201712 | 12345678036 | blank    | Q30      | not be             |
    