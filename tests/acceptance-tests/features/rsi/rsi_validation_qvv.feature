Feature: RSI Validation Question Versus Value

  Background:
    Given As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: RSI LU-5033 - Comment Present Validation Check on forms 5, 6 and 7
    Given I search for the survey "0023" with <reference> for the period <period>
    When I submit the comment <comment> for question <question>
    And I trigger the validation process
    Then the <validation> message should <isValidationExists> displayed

    Examples:
      | period | reference   | comment | validation                   | isValidationExists |
      | 201903 | 49900534932 | 2       | Respondent entered a comment | be                 |
      | 201904 | 49900589234 | empty   | Respondent entered a comment | not be             |
      | 201903 | 49900613746 | 2       | Respondent entered a comment | be                 |
      | 201904 | 49900613746 | empty   | Respondent entered a comment | not be             |
      | 201903 | 49900756292 | 2       | Respondent entered a comment | be                 |
      | 201904 | 49900756292 | empty   | Respondent entered a comment | not be             |
