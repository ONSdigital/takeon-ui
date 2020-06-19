Feature: Scanning Errors Validation
  As a Business Survey User
  I want scanning errors to be flagged for investigation
  So that I can correct the survey response data and improve data quality for results processing


  Scenario Outline:  Sand and Gravel Land Survey 0066 - Check there is a fixed value validation to numerical fields for illegible values
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the survey "0066" with <reference> for the period <period>
    When I change the <existingValue> to <newValue> for all the question codes
    And I trigger the validation process
    Then the fixed validation <fixedValidation> message should <isValidationExists> displayed
    Examples:
      | reference   | period | existingValue | newValue    | fixedValidation                    | isValidationExists |
      | 49900012765 | 201903 | blank         | 99999999999 | Value set to default, please check | be                 |
      | 49900012765 | 201903 | 1234          | 99999999999 | Value set to default, please check | be                 |
      | 49900012765 | 201903 | 99999999999   | 1234        | Value set to default, please check | not be             |

  Scenario Outline: Sand and Gravel Marine Survey 0076 - Check there is a fixed value validation to numerical fields for illegible values
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the survey "0066" with <reference> for the period <period>
    When I change the <existingValue> to <newValue> for all the question codes
    And I trigger the validation process
    Then the <fixedValidation> message should <isValidationExists> displayed

    Examples:
      | reference   | period | existingValue | newValue    | fixedValidation                    | isValidationExists |
      | 49900000796 | 201903 | blank         | 99999999999 | Value set to default, please check | be                 |
      | 49900002387 | 201903 | 1234          | 99999999999 | Value set to default, please check | be                 |
      | 49900008900 | 201903 | 99999999999   | 1234        | Value set to default, please check | not be             |


  Scenario Outline:  Blocks Survey 0073 - Check there is a fixed value validation to numerical fields for illegible values
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the survey "0073" with <reference> for the period <period>
    When I change the <existingValue> to <newValue> for all the question codes
    And I trigger the validation process
    Then the <fixedValidation> message should <isValidationExists> displayed
    Examples:
      | reference   | period | existingValue | newValue    | fixedValidation                    | isValidationExists |
      | 49900190211 | 201905 | blank         | 99999999999 | Value set to default, please check | be                 |
      | 49900190211 | 201905 | 1234          | 99999999999 | Value set to default, please check | be                 |
      | 49900190211 | 201905 | 99999999999   | 1234        | Value set to default, please check | not be             |


  Scenario Outline:  Bricks Survey 0074 - Check there is a fixed value validation to numerical fields for illegible values
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the survey "0074" with <reference> for the period <period>
    When I change the <existingValue> to <newValue> for all the question codes
    And I trigger the validation process
    Then the <fixedValidation> message should <isValidationExists> displayed
    Examples:
      | reference   | period | existingValue | newValue    | fixedValidation                    | isValidationExists |
      | 49900229065 | 201905 | blank         | 99999999999 | Value set to default, please check | be                 |
      | 49900229065 | 201905 | 1234          | 99999999999 | Value set to default, please check | be                 |
      | 49900229065 | 201905 | 99999999999   | 1234        | Value set to default, please check | not be             |

  Scenario Outline:  Sand and Gravel Land Survey 0066  - Check there isn't any fixed value validation to numerical fields for comments field questions
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the survey "0066" with <reference> for the period <period>
    When I change the <existingValue> to <newValue> for the question codes
      | question_codes |
      | Q146           |
      | Q147           |
    And I trigger the validation process
    Then the fixed validation should <isValidationExists> exists
    Examples:
      | reference   | period | existingValue | newValue    | isValidationExists |
      | 49900012765 | 201903 | blank         | 99999999999 | not                |
      | 49900012765 | 201903 | 1234          | 99999999999 | not                |
      | 49900012765 | 201903 | 99999999999   | 1234        | not                |

  Scenario Outline: Sand and Gravel Marine Survey 0076 - Check there isn't any fixed value validation to numerical fields for comments field questions
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the survey "0076" with <reference> for the period <period>
    When I change the <existingValue> to <newValue> for the question codes
      | question_codes |
      | Q146           |
      | Q148           |
    And I trigger the validation process
    Then the fixed validation should <isValidationExists> exists
    Examples:
      | reference   | period | existingValue | newValue    | isValidationExists |
      | 49900004791 | 201903 | blank         | 99999999999 | not                |
      | 49900004791 | 201903 | 1234          | 99999999999 | not                |
      | 49900004791 | 201903 | 99999999999   | 1234        | not                |


  Scenario Outline: Blocks Survey 0073 - Check there isn't any fixed value validation to numerical fields for comments field questions
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the survey "0073" with <reference> for the period <period>
    When I change the <existingValue> to <newValue> for the question codes
      | question_codes |
      | Q145           |
      | Q146           |
    And I trigger the validation process
    Then the fixed validation should <isValidationExists> exists
    Examples:
      | reference   | period | existingValue | newValue    | isValidationExists |
      | 49900190211 | 201905 | blank         | 99999999999 | not                |
      | 49900190211 | 201905 | 1234          | 99999999999 | not                |
      | 49900190211 | 201905 | 99999999999   | 1234        | not                |

  Scenario Outline: Bricks Survey 0074 - Check there isn't any fixed value validation to numerical fields for numeric type field questions
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the survey "0074" with <reference> for the period <period>
    When I change the <existingValue> to <newValue> for the question codes
      | question_codes |
      | Q145           |
      | Q146           |
      | Q8000          |
    And I trigger the validation process
    Then the fixed validation should <isValidationExists> exists
    Examples:
      | reference   | period | existingValue | newValue    | isValidationExists |
      | 49900356828 | 201905 | blank         | 99999999999 | not                |
      | 49900356828 | 201905 | 1234          | 99999999999 | not                |
      | 49900356828 | 201905 | 99999999999   | 1234        | not                |
