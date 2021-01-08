Feature: RSI Survey - Question vs Question Validation rule

  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: LU-6831 - Question vs Question Validation RSI survey on form 5
    Given I search for the survey "023" with <reference> for the current period <period>
    And I submit the "sales" <values> for questions
      | question_codes |
      | Q20            |
      | Q21            |
    When I trigger the validation process
    Then the "qvq validation" message should <isValidationExists> displayed for question code "Q21"
    Examples:
      | period | reference   | values     | isValidationExists |
      | 201903 | 49900551526 | 99,100     | be                 |
      | 201903 | 49900551526 | 100,99     | not be             |
      | 201903 | 49900551526 | 100,999999 | be                 |


  Scenario Outline: LU-6831 - Question vs Question Validation RSI survey on form 6
    Given I search for the survey "023" with <reference> for the current period <period>
    And I submit the "sales" <values> for questions
      | question_codes |
      | Q20            |
      | Q21            |
    When I trigger the validation process
    Then the "qvq validation" message should <isValidationExists> displayed for question code "Q21"
    Examples:
      | period | reference   | values     | isValidationExists |
      | 201903 | 49900617217 | 99,100     | be                 |
      | 201903 | 49900617217 | 100,99     | not be             |
      | 201903 | 49900617217 | 100,999999 | be                 |


  Scenario Outline: LU-6831 - Question vs Question Validation RSI survey on form 7
    Given I search for the survey "023" with <reference> for the current period <period>
    And I submit the "sales" <values> for questions
      | question_codes |
      | Q20            |
      | Q21            |
    When I trigger the validation process
    Then the "qvq validation" message should <isValidationExists> displayed for question code "Q21"
    Examples:
      | period | reference   | values     | isValidationExists |
      | 201904 | 49900756292 | 99,100     | be                 |
      | 201904 | 49900756292 | 100,99     | not be             |
      | 201904 | 49900756292 | 100,999999 | be                 |
