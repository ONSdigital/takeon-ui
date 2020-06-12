Feature:  Comment Present Validation rule

  Background:
    Given As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: RSI LU-6403 - Comment Present Validation test survey
    Given I search for the survey "999A" with <reference> for the period <period>
    When I submit the comment <comment> about reason for turnover changes for <field type>
    And I trigger the validation process
    Then the <validation> message should <isValidationExists> displayed
    Examples:
      | field type | period | reference   | comment    | validation                               | isValidationExists |
      | integer    | 201903 | 49900534932 | 2          | There is a comment from this contributor | be                 |
      | integer    | 201903 | 49900534932 | blank      | There is a comment from this contributor | not be             |
      | integer    | 201903 | 49900534932 | -2         | There is a comment from this contributor | not be             |
      | string     | 201903 | 49900534932 | some value | There is a comment from this contributor | be                 |
      | string     | 201903 | 49900534932 | blank      | There is a comment from this contributor | not be             |
