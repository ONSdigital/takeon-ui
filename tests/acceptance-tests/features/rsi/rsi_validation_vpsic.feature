Feature: RSI Survey - Validation Value Present SIC (VPSIC)

  Background:
    Given As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: LU-6670 - Value Present SIC (VPSIC) Validation for RSI Survey form 7
    Given I search for the survey "0023" with <reference> for the current period <period> with SIC code <SIC>
    When I submit the "SICValue" <SICValue> for question <question>
    And I trigger the validation process
    Then the <validation> message should <isValidationExists> displayed

    Examples:
      | period | reference   | SIC   | SICValue | question | validation                          | isValidationExists |
      | 201903 | 49900818161 | 47300 | 1        | Q21      | Check the response to this question | be                 |
      | 201903 | 49900818161 | 47300 | blank    | Q21      | Check the response to this question | not be             |
      | 201904 | 49900818161 | 47300 | 0        | Q21      | Check the response to this question | not be             |
      | 201903 | 49900818161 | 47300 | -2       | Q21      | Check the response to this question | not be             |
      | 201903 | 49900748571 | 41100 | 1        | Q21      | Check the response to this question | not be             |
