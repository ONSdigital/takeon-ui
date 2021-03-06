Feature: RSI Survey - Comment Present(Question vs Value) Validation rule

  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: LU-6531 - Comment Present Validation RSI survey on form 5
    Given I search for the survey "023" with <reference> for the current period <period>
    When I submit the "comment" <comment> for question <question>
    And I trigger the validation process
    Then the "qvv validation" message should <isValidationExists> displayed
    Examples:
      | period | reference   | comment | question | isValidationExists |
      | 201903 | 12000551526 | 12345   | Q146     | be                 |
      | 201903 | 12000551526 | blank   | Q146     | not be             |
      | 201903 | 12000551526 | Test    | Q146     | be                 |

  Scenario Outline: LU-6531 - Comment Present Validation RSI survey on form 6
    Given I search for the survey "023" with <reference> for the current period <period>
    When I submit the "comment" <comment> for question <question>
    And I trigger the validation process
    Then the "qvv validation" message should <isValidationExists> displayed
    Examples:
      | period | reference   | comment | question | isValidationExists |
      | 201903 | 12000613746 | blank   | Q146     | not be             |
      | 201903 | 12000613746 | Test    | Q146     | be                 |
      | 201903 | 12000613746 | 12345   | Q146     | be                 |

  Scenario Outline: LU-6531 - Comment Present Validation RSI survey on form 7
    Given I search for the survey "023" with <reference> for the current period <period>
    When I submit the "comment" <comment> for question <question>
    And I trigger the validation process
    Then the "qvv validation" message should <isValidationExists> displayed
    Examples:
      | period | reference   | comment | question | isValidationExists |
      | 201903 | 12000791240 | 12345   | Q146     | be                 |
      | 201903 | 12000791240 | blank   | Q146     | not be             |
      | 201903 | 12000791240 | Test    | Q146     | be                 |
