Feature: Test Survey - Fixed Value(FV) Validation rule


  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a Business Survey user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: SPP-100 - Check Fixed Value Validation
    Given I search for the survey "999A" with <reference> for the current period <period>
    And I submit the "fixed value" <value> for question <question>
    When I trigger the validation process
    Then the "fv validation" message should <isValidationExists> displayed
    Examples:
      | reference   | period | value        | isValidationExists | question |
      | 12345678036 | 201712 | 99999999999  | be                 | Q7       |
      | 12345678036 | 201712 | 9999999999   | not be             | Q7       |
      | 12345678036 | 201712 | 999999999999 | not be             | Q7       |
      | 12345678036 | 201712 | blank        | not be             | Q7       |
