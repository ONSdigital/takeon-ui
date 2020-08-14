Feature: Sand and Gravel Marine Survey - Fixed Value(FV) Validation rule


  Background:
    Given As a BMI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline:  LU-7208 - Check Fixed Value Validation - Sand and Gravel Marine Survey
    Given I search for the survey "076" with <reference> for the current period <period>
    And I submit the "bricks stock material" <values> for questions
      | question_codes |
      | Q601           |
      | Q602           |
      | Q603           |
      | Q604           |
      | Q605           |
      | Q606           |
      | Q607           |
      | Q608           |
    When I trigger the validation process
    Then the "fv validation" message should <isValidationExists> displayed for question codes
    Examples:
      | reference   | period | values       | isValidationExists |
      | 49900004791 | 201903 | 99999999999  | be                 |
      | 49900004791 | 201903 | 9999999999   | not be             |
      | 49900004791 | 201903 | 999999999999 | not be             |
      | 49900004791 | 201903 | 0            | not be             |
      | 49900004791 | 201903 | blank        | not be             |


  Scenario Outline:  LU-7208 - Check Fixed Value Validation - Sand and Gravel Marine Survey comment field questions
    Given I search for the survey "076" with <reference> for the current period <period>
    And I submit the "bricks stock material" <values> for questions
      | question_codes |
      | Q148           |
      | Q146           |
    When I trigger the validation process
    Then the "fv validation" message should <isValidationExists> displayed for question codes
    Examples:
      | reference   | period | values      | isValidationExists |
      | 49900004791 | 201903 | 99999999999 | not be             |
      | 49900004791 | 201903 | 0           | not be             |
      | 49900004791 | 201903 | blank       | not be             |
