Feature: BMI Surveys(Blocks,Bricks,Sand Gravel Land and Sand Gravel Marine) - Override checkbox - Fixed Value(FV) Validation rule


  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a BMI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: LU-7170 - Check Override functionality for Comment Present Validation
    Given I search for the <survey> with <reference> for the current period <period>
    And I submit the "comment" <comment> for question <question>
    And I trigger the validation process
    When I override the validation for the question <question>
    Then the validation message should change to "qvv override message"
    Examples:
      | survey | period | reference   | comment | question |
      | 073    | 201905 | 12000228645 | 2       | Q145     |
      | 074    | 201905 | 12000229065 | 2       | Q145     |
      | 066    | 201903 | 12000000796 | 2       | Q146     |
      | 076    | 201903 | 12000004791 | 2       | Q146     |
