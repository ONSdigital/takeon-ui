Feature: RSI Survey - Validation Value is Blank and Value is Zero

  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: RSI LU-6579 - Value is Blank(VB) Validation on forms 5,6 and 7
    Given I search for the survey "023" with <reference> for the current period <period>
    When I submit the "total turnover" <value> for question <question>
    And I trigger the validation process
    Then the "vb validation" message should <isValidationExists> displayed

    Examples:
      | period | reference   | value | question | isValidationExists |
      | 201903 | 49900534932 | blank | Q20      | be                 |
      | 201903 | 49900694171 | blank | Q20      | be                 |
      | 201904 | 49900756292 | blank | Q20      | be                 |


  Scenario Outline: RSI LU-6579 - Value is Zero(VZ) Validation on forms 5,6 and 7
    Given I search for the survey "023" with <reference> for the current period <period>
    When I submit the "total turnover" <value> for question <question>
    And I trigger the validation process
    Then the "vz validation" message should <isValidationExists> displayed

    Examples:
      | period | reference   | value | question | isValidationExists |
      | 201903 | 49900534932 | 0     | Q20      | be                 |
      | 201903 | 49900694171 | 0     | Q20      | be                 |
      | 201904 | 49900756292 | 0     | Q20      | be                 |


  Scenario Outline: RSI LU-6579 - Value is Blank(VB) and Value is Zero(VZ) Validation on forms 5,6 and 7
    Given I search for the survey "023" with <reference> for the current period <period>
    When I submit the "total turnover" <value> for question <question>
    And I trigger the validation process
    Then the "vb and vz validation" message should <isValidationExists> displayed

    Examples:
      | period | reference   | value | question | isValidationExists |
      | 201903 | 49900534932 | 2     | Q20      | not be             |
      | 201903 | 49900694171 | 2     | Q20      | not be             |
      | 201904 | 49900534932 | 2     | Q20      | not be             |

  Scenario Outline: RSI LU-6579 - Value is Blank(VB) and Value is Zero(VZ) Validation for negative values on forms 5,6 and 7
    Given I search for the survey "023" with <reference> for the current period <period>
    When I submit the "total turnover" <value> for question <question>
    And I trigger the validation process
    Then the "vb and vz validation" message should <isValidationExists> displayed

    Examples:
      | period | reference   | value | question | isValidationExists |
      | 201903 | 49900534932 | -2    | Q20      | not be             |
      | 201903 | 49900694171 | -2    | Q20      | not be             |
      | 201904 | 49900534932 | -2    | Q20      | not be             |
