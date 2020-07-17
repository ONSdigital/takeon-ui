Feature: RSI Survey - Comment Present(Question vs Value) Validation rule for text type

  Background:
    Given As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: LU-6531 - Comment Present Validation RSI survey on form 5
    Given I search for the survey "0023" with <reference> for the current period <period>
    And I submit the "comment" <comment> for questions
      | question_codes |
      | Q146a          |
      | Q146b          |
      | Q146c          |
      | Q146d          |
      | Q146e          |
      | Q146f          |
      | Q146g          |
      | Q146h          |
    When I trigger the validation process
    Then the <comment> message should <isValidationExists> displayed
    Examples:
      | period | reference   | comment   | isValidationExists |
      | 201903 | 49900551526 | TEST      | be                 |
      | 201903 | 49900551526 | TEST TEST | be                 |
      | 201903 | 49900551526 | blank     | be                 |

