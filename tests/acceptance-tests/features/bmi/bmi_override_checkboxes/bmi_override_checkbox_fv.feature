Feature: BMI Surveys(Blocks,Bricks,Sand Gravel Land and Sand Gravel Marine) - Override checkbox - Fixed Value(FV) Validation rule


  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a BMI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline:  LU-7170 - Check Override functionality for Fixed Value Validation
    Given I search for the <survey> with <reference> for the current period <period>
    And I submit the "bmi survey stock material" <value> for question <question>
    And I trigger the validation process
    When I override the validation for the question <question>
    Then the validation message should change to "fv override message"
    Examples:
      | survey | reference   | period | value       | question |
      | 073    | 49900138556 | 201906 | 99999999999 | Q101     |
      | 074    | 49900229065 | 201905 | 99999999999 | Q001     |
      | 066    | 49900012765 | 201903 | 99999999999 | Q601     |
      | 076    | 49900004791 | 201903 | 99999999999 | Q601     |
