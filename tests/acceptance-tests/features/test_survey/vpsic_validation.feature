Feature: Test Survey - Value Present SIC (VPSIC) Validation rule

  Background:
    Given As a Business Survey user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: SP-100 - Value Present SIC (VPSIC) Validation on test survey
    Given I search for the survey "999A" with <reference> for the current period <period> with SIC code <SIC>
    When I submit the "SICValue" <SICValue> for question <question>
    And I trigger the validation process
    Then the "vpsic validation" message should <isValidationExists> displayed
    Examples:
      | period | reference   | SIC   | SICValue | question | isValidationExists |
      | 201712 | 12345678036 | 47300 | 1        | Q4       | be                 |
      | 201712 | 12345678036 | 47300 | blank    | Q4       | not be             |
      | 201712 | 12345678036 | 47300 | 0        | Q4       | not be             |
      | 201712 | 12345678036 | 47300 | -2       | Q4       | not be             |
      | 201712 | 12345678037 | 37266 | 1        | Q4       | not be             |
