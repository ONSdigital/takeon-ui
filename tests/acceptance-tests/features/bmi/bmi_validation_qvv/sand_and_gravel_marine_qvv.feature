Feature: Sand and Gravel Marine Survey - Comment Present(Question vs Value) Validation rule

  Background:
    Given As a BMI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: LU-6531 - Comment Present Validation Sand Gravel marine survey on form 2
    Given I search for the survey "076" with <reference> for the current period <period>
    When I submit the "comment" <comment> for question <question>
    And I trigger the validation process
    Then the <validation> message should <isValidationExists> displayed
    Examples:
      | period | reference   | comment | question | validation                               | isValidationExists |
      | 201903 | 49900004791 | 12345   | Q146     | There is a comment from this contributor | not be             |
      | 201903 | 49900004791 | blank   | Q146     | There is a comment from this contributor | not be             |
      | 201903 | 49900004791 | 2       | Q146     | There is a comment from this contributor | be                 |
      | 201903 | 49900004791 | blank   | Q148     | There is a comment from this contributor | not be             |
      | 201903 | 49900004791 | 1       | Q148     | There is a comment from this contributor | not be             |
      | 201903 | 49900004791 | 2       | Q148     | There is a comment from this contributor | be                 |
