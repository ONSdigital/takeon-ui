Feature: Bricks Survey - Fixed Value(FV) Validation rule


  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a BMI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline:  LU-7208 - Fixed Value Validation - Bricks Survey
    Given I search for the survey "074" with <reference> for the current period <period>
    And I submit the "bricks stock material" <values> for questions
      | question_codes |
      | Q001           |
      | Q002           |
      | Q003           |
      | Q004           |
      | Q011           |
      | Q012           |
      | Q013           |
      | Q014           |
      | Q021           |
      | Q022           |
      | Q023           |
      | Q024           |
      | Q501           |
      | Q502           |
      | Q503           |
      | Q504           |
    When I trigger the validation process
    Then the "fv validation" message should <isValidationExists> displayed for question codes
    Examples:
      | reference   | period | values       | isValidationExists |
      | 49900229065 | 201905 | 99999999999  | be                 |
      | 49900229065 | 201905 | 9999999999   | not be             |
      | 49900229065 | 201905 | 999999999999 | not be             |
      | 49900229065 | 201905 | 0            | not be             |
      | 49900229065 | 201905 | blank        | not be             |


  Scenario Outline:  LU-7208 - Fixed Value Validation - Bricks Survey comment field questions
    Given I search for the survey "074" with <reference> for the current period <period>
    And I submit the "bricks stock material" <values> for questions
      | question_codes |
      | Q8000          |
      | Q145           |
      | Q146           |
    When I trigger the validation process
    Then the "fv validation" message should <isValidationExists> displayed for question codes
    Examples:
      | reference   | period | values      | isValidationExists |
      | 49900229065 | 201905 | 99999999999 | not be             |
      | 49900229065 | 201905 | 0           | not be             |
      | 49900229065 | 201905 | blank       | not be             |
