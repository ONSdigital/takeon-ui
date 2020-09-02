Feature: Sand and Gravel Land Survey - Comment Present(Question vs Value) Validation rule

  Background:
    Given As a BMI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: LU-6531 - Comment Present Validation Sand Gravel land survey on form 1
    Given I search for the survey "066" with <reference> for the current period <period>
    When I submit the "comment" <comment> for question <question>
    And I trigger the validation process
    Then the "qvv validation" message should <isValidationExists> displayed
    Examples:
      | period | reference   | comment | question | validation                               | isValidationExists |
      | 201903 | 49900000796 | 12345   | Q146     | There is a comment from this contributor | not be             |
      | 201903 | 49900000796 | blank   | Q146     | There is a comment from this contributor | not be             |
      | 201903 | 49900000796 | 2       | Q146     | There is a comment from this contributor | be                 |
      | 201903 | 49900000796 | blank   | Q147     | There is a comment from this contributor | not be             |
      | 201903 | 49900000796 | 1       | Q147     | There is a comment from this contributor | not be             |
      | 201903 | 49900000796 | 2       | Q147     | There is a comment from this contributor | be                 |
