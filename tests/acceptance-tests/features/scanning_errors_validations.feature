Feature: As a Business Survey User
  I want scanning errors to be flagged for investigation
  So that I can correct the survey response data and improve data quality for results processing


  Scenario Outline:  Sand and Gravel Land Survey 0066 - Check there is a fixed value validation to numerical fields for illegible values
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the <survey> with <reference> for the period <period>
    When I change the <existingValue> to <newValue> for all the question codes
    And I trigger the validation process
    Then the <fixedValidation> message should <isValidationExists> displayed

    Examples:
      | reference   | survey | period | existingValue | newValue    | fixedValidation                    | isValidationExists |
      | 10000000003 | 0066   | 201809 | blank         | 99999999999 | Value set to default, please check | be                 |
      | 10000000003 | 0066   | 201809 | 1234          | 99999999999 | Value set to default, please check | be                 |
      | 10000000003 | 0066   | 201809 | 99999999999   | 1234        | Value set to default, please check | not be             |

     Scenario Outline: Sand and Gravel Marine Survey 0076 - Check there is a fixed value validation to numerical fields for illegible values
    Given As a BMI user I search for the <survey> form returned by the contributor with <reference> number for <period>
    When I change the <existingValue> to <newValue> for all the question codes
    And I trigger the validation process
    Then the <fixedValidation> message should <isValidationExists> displayed

    Examples:
      | reference   | survey | period | existingValue | newValue    | fixedValidation                    | isValidationExists |
      | 10000000004 | 0076   | 201809 | blank         | 99999999999 | Value set to default, please check | be                 |
      | 10000000004 | 0076   | 201809 | 1234          | 99999999999 | Value set to default, please check | be                 |
      | 10000000004 | 0076   | 201809 | 99999999999   | 1234        | Value set to default, please check | not be             |


  Scenario Outline:  Blocks Survey 0073 - Check there is a fixed value validation to numerical fields for illegible values
    Given As a BMI user I search for the <survey> form returned by the contributor with <reference> number for <period>
    When I change the <existingValue> to <newValue> for all the question codes
    And I trigger the validation process
    Then the <fixedValidation> message should <isValidationExists> displayed

    Examples:
      | reference   | survey | period | existingValue | newValue    | fixedValidation                    | isValidationExists |
      | 10000000005 | 0073   | 201809 | blank         | 99999999999 | Value set to default, please check | be                 |
      | 10000000005 | 0073   | 201809 | 1234          | 99999999999 | Value set to default, please check | be                 |
      | 10000000005 | 0073   | 201809 | 99999999999   | 1234        | Value set to default, please check | not be             |


  Scenario Outline:  Bricks Survey 0074 - Check there is a fixed value validation to numerical fields for illegible values
    Given As a BMI user I search for the <survey> form returned by the contributor with <reference> number for <period>
    When I change the <existingValue> to <newValue> for all the question codes
    And I trigger the validation process
    Then the <fixedValidation> message should <isValidationExists> displayed

    Examples:
      | reference   | survey | period | existingValue | newValue    | fixedValidation                    | isValidationExists |
      | 10000000006 | 0074   | 201809 | blank         | 99999999999 | Value set to default, please check | be                 |
      | 10000000006 | 0074   | 201809 | 1234          | 99999999999 | Value set to default, please check | be                 |
      | 10000000006 | 0074   | 201809 | 99999999999   | 1234        | Value set to default, please check | not be             |


  Scenario Outline:  Sand and Gravel Land Survey 0066  - Check there isn't any fixed value validation to numerical fields for comments field questions
    Given As a BMI user I search for the <survey> form returned by the contributor with <reference> number for <period>
    When I change the <existingValue> to <newValue> for the questionCodes
      | question_codes |
      | Q146           |
      | Q147           |
    And I trigger the validation process
    Then the <fixedValidation> message should not be displayed

    Examples:
      | reference   | survey | period | existingValue | newValue    | fixedValidation                    |
      | 10000000006 | 0066   | 201809 | blank         | 99999999999 | Value set to default, please check |
      | 10000000006 | 0066   | 201809 | 1234          | 99999999999 | Value set to default, please check |
      | 10000000006 | 0066   | 201809 | 99999999999   | 1234        | Value set to default, please check |

  Scenario Outline: Sand and Gravel Marine Survey 0076 - Check there isn't any fixed value validation to numerical fields for comments field questions
    Given As a BMI user I search for the <survey> form returned by the contributor with <reference> number for <period>
    When I change the <existingValue> to <newValue> for the questionCodes
      | question_codes |
      | Q146           |
      | Q148           |
    And I trigger the validation process
    Then the <fixedValidation> message should not be displayed

    Examples:
      | reference   | survey | period | existingValue | newValue    | fixedValidation                    |
      | 10000000006 | 0076   | 201809 | blank         | 99999999999 | Value set to default, please check |
      | 10000000006 | 0076   | 201809 | 1234          | 99999999999 | Value set to default, please check |
      | 10000000006 | 0076   | 201809 | 99999999999   | 1234        | Value set to default, please check |


  Scenario Outline: Blocks Survey 0073 - Check there isn't any fixed value validation to numerical fields for comments field questions
    Given As a BMI user I search for the <survey> form returned by the contributor with <reference> number for <period>
    When I change the <existingValue> to <newValue> for the question codes
      | question_codes |
      | Q145           |
      | Q146           |
    And I trigger the validation process
    Then  <fixedValidation> message should not be displayed

    Examples:
      | reference   | survey | period | existingValue | newValue    | fixedValidation                    |
      | 10000000006 | 0073   | 201809 | blank         | 99999999999 | Value set to default, please check |
      | 10000000006 | 0073   | 201809 | 1234          | 99999999999 | Value set to default, please check |
      | 10000000006 | 0073   | 201809 | 99999999999   | 1234        | Value set to default, please check |

  Scenario Outline: Blocks Survey 0074 - Check there isn't any fixed value validation to numerical fields for rick type field questions
    Given As a BMI user I search for the <survey> form returned by the contributor with <reference> number for <period>
    When I change the <existingValue> to <newValue> for the question codes
      | question_codes |
      | Q145 |
      | Q146 |
      | Q8000 |
    And I trigger the validation process
    Then the <fixedValidation> message should not be displayed

    Examples:
      | reference   | survey | period | existingValue | newValue    | fixedValidation                    |
      | 10000000006 | 0073   | 201809 | blank         | 99999999999 | Value set to default, please check |
      | 10000000006 | 0073   | 201809 | 1234          | 99999999999 | Value set to default, please check |
      | 10000000006 | 0073   | 201809 | 99999999999   | 1234        | Value set to default, please check |
