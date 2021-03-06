Feature: Test Survey - Value Present SIC (VPSIC) Validation rule

  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a Business Survey user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: SP-100 - Value Present SIC (VPSIC) Validation on test survey
    Given I search for the survey "999A" with <reference> for the current period <period> with SIC code <SIC>
    When I submit the "value" <value> for question <question>
    And I trigger the validation process
    Then the "vpsic validation" message should <isValidationExists> displayed
    Examples:
      | period | reference   | SIC   | value | question | isValidationExists |
      | 201712 | 12345678036 | 47300 | 1        | Q4       | be                 |
      | 201712 | 12345678036 | 47300 | blank    | Q4       | not be             |
      | 201712 | 12345678036 | 47300 | 0        | Q4       | not be             |
      | 201712 | 12345678036 | 47300 | -2       | Q4       | not be             |
      | 201712 | 12345678037 | 37266 | 1        | Q4       | not be             |
