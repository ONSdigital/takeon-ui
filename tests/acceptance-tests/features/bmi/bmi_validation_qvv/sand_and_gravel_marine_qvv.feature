Feature: Sand and Gravel Marine Survey - Comment Present(Question vs Value) Validation rule

  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a BMI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: LU-6531 - Comment Present Validation Sand Gravel marine survey on form 2
    Given I search for the survey "076" with <reference> for the current period <period>
    When I submit the "comment" <comment> for question <question>
    And I trigger the validation process
    Then the "qvv validation" message should <isValidationExists> displayed
    Examples:
      | period | reference   | comment | question | isValidationExists |
      | 201903 | 12000004791 | 12345   | Q146     | not be             |
      | 201903 | 12000004791 | blank   | Q146     | not be             |
      | 201903 | 12000004791 | 2       | Q146     | be                 |
      | 201903 | 12000004791 | blank   | Q148     | not be             |
      | 201903 | 12000004791 | 1       | Q148     | not be             |
      | 201903 | 12000004791 | 2       | Q148     | be                 |
