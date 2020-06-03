Feature: RSI Validation Comment Present

  Background:
    Given As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: RSI LU-5033 - Comment Present Validation Check on form 5
    Given I search for the survey "0023" with <reference> for the period <period>
    When I submit the comment <comment> about reason for turnover changes
    And I trigger the validation process
    Then the <validation> message should <isValidationExists> displayed

    Examples:
      | period | reference   | comment | validation                   | isValidationExists |
      | 201904 | 49900534932 | 2       | Respondent entered a comment | be                 |
      | 201904 | 49900589234 | empty   | Respondent entered a comment | not be             |
    