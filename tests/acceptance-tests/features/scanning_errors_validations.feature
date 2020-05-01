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
