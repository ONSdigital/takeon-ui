Feature: Blocks Survey - Fixed Value(FV) Validation rule


  Background:
    Given As a BMI user I set the search criteria options for the forms returned by the contributor

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
    Then the <validation> message should <isValidationExists> displayed for question codes
    Examples:
      | reference   | period | values       | validation                         | isValidationExists |
      | 49900138556 | 201905 | 99999999999  | Value set to default, please check | be                 |
      | 49900138556 | 201905 | 9999999999   | Value set to default, please check | not be             |
      | 49900138556 | 201905 | 999999999999 | Value set to default, please check | not be             |
      | 49900138556 | 201905 | 0            | Value set to default, please check | not be             |
      | 49900138556 | 201905 | blank        | Value set to default, please check | not be             |


  Scenario Outline:  LU-7208 - Check Fixed Value Validation - Blocks Survey comment field questions
    Given I search for the survey "073" with <reference> for the current period <period>
    And I submit the "bricks stock material" <values> for questions
      | question_codes |
      | Q145           |
      | Q146           |
    When I trigger the validation process
    Then the <validation> message should <isValidationExists> displayed for question codes
    Examples:
      | reference   | period | values      | validation                         | isValidationExists |
      | 49900138556 | 201905 | 99999999999 | Value set to default, please check | not be             |
      | 49900138556 | 201905 | 0           | Value set to default, please check | not be             |
      | 49900138556 | 201905 | blank       | Value set to default, please check | not be             |
