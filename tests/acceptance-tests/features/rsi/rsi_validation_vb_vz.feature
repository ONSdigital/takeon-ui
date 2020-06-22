Feature: RSI Validation Value is Versus Value

  Background:
    Given As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: RSI LU-6579 - Value is Blank and Validation is Zero Check on forms 5
    Given I search for the survey "0023" with <reference> for the period <period>
    When I submit the total turnover value <value> for question <question>
    And I trigger the validation process
    Then the <validation> message should <isValidationExists> displayed

    Examples:
      | period | reference   | value | question | validation                             | isValidationExists |
      | 201903 | 49900534932 | 0     | Q20      | This value is zero                     | be                 |
      | 201903 | 49900534932 | blank | Q20      | This value is blank                    | be                 |
      | 201903 | 49900534932 | 2     | Q20      | This value is zero,This value is blank | not be             |


  Scenario Outline: RSI LU-6579 - Value is Blank and Validation is Zero Check on forms 6
    Given I search for the survey "0023" with <reference> for the period <period>
    When I submit the total turnover value <value> for question <question>
    And I trigger the validation process
    Then the <validation> message should <isValidationExists> displayed

    Examples:
      | period | reference   | value | question | validation                             | isValidationExists |
      | 201903 | 49900613746 | 0     | Q20      | This value is zero                     | be                 |
      | 201903 | 49900613746 | blank | Q20      | This value is blank                    | be                 |
      | 201903 | 49900613746 | 2     | Q20      | This value is zero,This value is blank | not be             |


  Scenario Outline: RSI LU-6579 - Value is Blank and Validation is Zero Check on forms 7
    Given I search for the survey "0023" with <reference> for the period <period>
    When I submit the total turnover value <value> for question <question>
    And I trigger the validation process
    Then the <validation> message should <isValidationExists> displayed

    Examples:
      | period | reference   | value | question | validation                             | isValidationExists |
      | 201903 | 49900748571 | 0     | Q20      | This value is zero                     | be                 |
      | 201903 | 49900748571 | blank | Q20      | This value is blank                    | be                 |
      | 201903 | 49900748571 | 2     | Q20      | This value is zero,This value is blank | not be             |

