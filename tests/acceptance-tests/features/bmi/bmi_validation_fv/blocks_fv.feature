Feature: Blocks Survey - Fixed Value(FV) Validation rule


  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a BMI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline:  LU-7208 - Check Fixed Value Validation - Blocks Survey
    Given I search for the survey "073" with <reference> for the current period <period>
    And I submit the "bricks stock material" <values> for questions
      | question_codes |
      | Q101           |
      | Q102           |
      | Q103           |
      | Q104           |
      | Q111           |
      | Q112           |
      | Q113           |
      | Q114           |
      | Q121           |
      | Q122           |
      | Q123           |
      | Q124           |
    When I trigger the validation process
    Then the "fv validation" message should <isValidationExists> displayed for question codes
    Examples:
      | reference   | period | values       | isValidationExists |
      | 12000138556 | 201905 | 99999999999  | be                 |
      | 12000138556 | 201905 | 9999999999   | not be             |
      | 12000138556 | 201905 | 999999999999 | not be             |
      | 12000138556 | 201905 | 0            | not be             |
      | 12000138556 | 201905 | blank        | not be             |


  Scenario Outline:  LU-7208 - Check Fixed Value Validation - Blocks Survey comment field questions
    Given I search for the survey "073" with <reference> for the current period <period>
    And I submit the "bricks stock material" <values> for questions
      | question_codes |
      | Q145           |
      | Q146           |
    When I trigger the validation process
    Then the "fv validation" message should <isValidationExists> displayed for question codes
    Examples:
      | reference   | period | values      | isValidationExists |
      | 12000138556 | 201905 | 99999999999 | not be             |
      | 12000138556 | 201905 | 0           | not be             |
      | 12000138556 | 201905 | blank       | not be             |
