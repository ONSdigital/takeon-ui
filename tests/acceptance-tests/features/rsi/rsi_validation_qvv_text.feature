Feature: RSI Survey - Comment Present(Question vs Value) Validation rule for text type

  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: LU-6640 - Comment Present Validation RSI survey on form 5
    Given I search for the survey "023" with <reference> for the current period <period>
    And I submit the "comment" <comment> for questions
      | question_codes |
      | Q146           |
      | Q146a          |
      | Q146b          |
      | Q146c          |
      | Q146d          |
      | Q146e          |
      | Q146f          |
      | Q146g          |
      | Q146h          |
    When I trigger the validation process
    Then the "comment" <comment> message should <isValidationExists> displayed
    Examples:
      | period | reference   | comment            | isValidationExists |
      | 201903 | 12000551526 | TEST               | be                 |
      | 201903 | 12000551526 | TEST<Blank>TEST    | be                 |
      | 201903 | 12000551526 | <Blank>TEST<Blank> | be                 |
      | 201903 | 12000551526 | <Blank>TEST        | be                 |
      | 201903 | 12000551526 | TEST<Blank>        | be                 |
      | 201903 | 12000551526 | <Blank>            | be                 |

  Scenario Outline: LU-6640 - Comment Present Validation RSI survey on form 6
    Given I search for the survey "023" with <reference> for the current period <period>
    And I submit the "comment" <comment> for questions
      | question_codes |
      | Q146           |
      | Q146a          |
      | Q146b          |
      | Q146c          |
      | Q146d          |
      | Q146e          |
      | Q146f          |
      | Q146g          |
      | Q146h          |
    When I trigger the validation process
    Then the "comment" <comment> message should <isValidationExists> displayed
    Examples:
      | period | reference   | comment            | isValidationExists |
      | 201903 | 12000613746 | TEST               | be                 |
      | 201903 | 12000613746 | TEST<Blank>TEST    | be                 |
      | 201903 | 12000613746 | <Blank>TEST<Blank> | be                 |
      | 201903 | 12000613746 | <Blank>TEST        | be                 |
      | 201903 | 12000613746 | TEST<Blank>        | be                 |
      | 201903 | 12000613746 | <Blank>            | be                 |


  Scenario Outline: LU-6640 - Comment Present Validation RSI survey on form 7
    Given I search for the survey "023" with <reference> for the current period <period>
    And I submit the "comment" <comment> for questions
      | question_codes |
      | Q146           |
      | Q146a          |
      | Q146b          |
      | Q146c          |
      | Q146d          |
      | Q146e          |
      | Q146f          |
      | Q146g          |
      | Q146h          |
    When I trigger the validation process
    Then the "comment" <comment> message should <isValidationExists> displayed
    Examples:
      | period | reference   | comment            | isValidationExists |
      | 201903 | 12000791240 | TEST               | be                 |
      | 201903 | 12000791240 | TEST<Blank>TEST    | be                 |
      | 201903 | 12000791240 | <Blank>TEST<Blank> | be                 |
      | 201903 | 12000791240 | <Blank>TEST        | be                 |
      | 201903 | 12000791240 | TEST<Blank>        | be                 |
      | 201903 | 12000791240 | <Blank>            | be                 |

