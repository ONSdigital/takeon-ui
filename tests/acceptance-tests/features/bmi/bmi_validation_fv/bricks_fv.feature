Feature: Bricks Survey - Fixed Value(FV) Validation rule


  Background:
    Given As a BMI user I set the search criteria options for the forms returned by the contributor

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
    Then the <validation> message should <isValidationExists> displayed
    Examples:
      | reference   | period | values       | validation                         | isValidationExists |
      | 49900229065 | 201905 | 99999999999  | Value set to default, please check | be                 |
      | 49900229065 | 201905 | 9999999999   | Value set to default, please check | not be             |
      | 49900229065 | 201905 | 999999999999 | Value set to default, please check | not be             |
      | 49900229065 | 201905 | 0            | Value set to default, please check | not be             |
      | 49900229065 | 201905 | blank        | Value set to default, please check | not be             |


  Scenario Outline:  LU-7208 - Fixed Value Validation - Bricks Survey comment field questions
    Given I search for the survey "074" with <reference> for the current period <period>
    And I submit the "bricks stock material" <values> for questions
      | question_codes |
      | Q8000          |
      | Q145           |
      | Q146           |
    When I trigger the validation process
    Then the <validation> message should <isValidationExists> displayed
    Examples:
      | reference   | period | values      | validation                         | isValidationExists |
      | 49900229065 | 201905 | 99999999999 | Value set to default, please check | not be             |
      | 49900229065 | 201905 | 0           | Value set to default, please check | not be             |
      | 49900229065 | 201905 | blank       | Value set to default, please check | not be             |
