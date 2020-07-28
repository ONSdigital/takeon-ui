Feature: RSI Survey - Validation Value is Blank and Value is Zero

  Background:
    Given As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: RSI LU-6579 - Value is Blank and Value is Zero Validation RSI survey on forms 5
    Given I search for the survey "023" with <reference> for the current period <period>
    When I submit the "total turnover" <value> for question <question>
    And I trigger the validation process
    Then the <validation> message should <isValidationExists> displayed

    Examples:
      | period | reference   | value | question | validation                             | isValidationExists |
      | 201903 | 49900534932 | 0     | Q20      | This value is zero                     | be                 |
      | 201903 | 49900534932 | blank | Q20      | This value is blank                    | be                 |
      | 201903 | 49900534932 | 2     | Q20      | This value is zero,This value is blank | not be             |
      | 201903 | 49900534932 | -2    | Q20      | This value is zero,This value is blank | not be             |


  Scenario Outline: RSI LU-6579 - Value is Blank and Value is Zero Validation RSI survey on forms 6
    Given I search for the survey "023" with <reference> for the current period <period>
    When I submit the "total turnover" <value> for question <question>
    And I trigger the validation process
    Then the <validation> message should <isValidationExists> displayed

    Examples:
      | period | reference   | value | question | validation                             | isValidationExists |
      | 201903 | 49900694171 | 0     | Q20      | This value is zero                     | be                 |
      | 201903 | 49900694171 | blank | Q20      | This value is blank                    | be                 |
      | 201903 | 49900694171 | 2     | Q20      | This value is zero,This value is blank | not be             |
      | 201903 | 49900534932 | -2    | Q20      | This value is zero,This value is blank | not be             |


  Scenario Outline: RSI LU-6579 - Value is Blank and Value is Zero Validation RSI survey on forms 7
    Given I search for the survey "023" with <reference> for the current period <period>
    When I submit the "total turnover" <value> for question <question>
    And I trigger the validation process
    Then the <validation> message should <isValidationExists> displayed

    Examples:
      | period | reference   | value | question | validation                             | isValidationExists |
      | 201904 | 49900756292 | 0     | Q20      | This value is zero                     | be                 |
      | 201904 | 49900756292 | blank | Q20      | This value is blank                    | be                 |
      | 201904 | 49900756292 | 2     | Q20      | This value is zero,This value is blank | not be             |
      | 201903 | 49900534932 | -2    | Q20      | This value is zero,This value is blank | not be             |
