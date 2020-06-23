Feature: RSI Survey - Comment Present(Question vs Value) Validation rule

  Background:
    Given As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: LU-6531 - Comment Present Validation RSI survey on form 5
    Given I search for the survey "0023" with <reference> for the period <period>
    When I submit the "comment" <comment> for question <question>
    And I trigger the validation process
    Then the <validation> message should <isValidationExists> displayed
    Examples:
      | period | reference   | comment | question | validation                               | isValidationExists |
      | 201903 | 49900551526 | 12345   | Q146     | There is a comment from this contributor | be                 |
      | 201903 | 49900551526 | blank   | Q146     | There is a comment from this contributor | not be             |
      | 201903 | 49900551526 | 2       | Q146     | There is a comment from this contributor | be                 |

    Scenario Outline: LU-6531 - Comment Present Validation RSI survey on form 6
    Given I search for the survey "0023" with <reference> for the period <period>
    When I submit the "comment" <comment> for question <question>
    And I trigger the validation process
    Then the <validation> message should <isValidationExists> displayed
    Examples:
      | period | reference   | comment | question | validation                               | isValidationExists |
      | 201903 | 49900613746 | blank   | Q146       | There is a comment from this contributor | not be             |
      | 201903 | 49900613746 | 1       | Q146       | There is a comment from this contributor | be                 |
      | 201903 | 49900613746 | 12345   | Q146       | There is a comment from this contributor | be                 |

    Scenario Outline: LU-6531 - Comment Present Validation RSI survey on form 7
    Given I search for the survey "0023" with <reference> for the period <period>
    When I submit the "comment" <comment> for question <question>
    And I trigger the validation process
    Then the <validation> message should <isValidationExists> displayed
    Examples:
      | period | reference   | comment | question | validation                               | isValidationExists |
      | 201903 | 49900791240 | 12345   | Q146       | There is a comment from this contributor | be                 |
      | 201903 | 49900791240 | blank   | Q146       | There is a comment from this contributor | not be             |
      | 201903 | 49900791240 | 2       | Q146       | There is a comment from this contributor | be                 |
