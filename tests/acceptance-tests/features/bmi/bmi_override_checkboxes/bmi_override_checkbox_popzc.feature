Feature: BMI Surveys(Blocks,Sand Gravel Land and Sand Gravel Marine) - Override checkboxes - Period on Period Zero Continuity(PoPZC) Validation rule

  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a BMI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: LU-7170 - Check Override functionality for Period on Period Zero Continuity Validation
    Given I search for the <survey> with <reference> for the previous period <previousPeriod>
    And I run the validation process on <questionCode> with <previousPeriodValue>
    And I search for the <survey> with <reference> for the current period <currentPeriod>
    When I run the validation process on <questionCode> with <currentPeriodValue>
    And I override the validation for the question <questionCode>
    Then the validation message should change to "popzc override message"

    Examples:
      | survey | reference   | currentPeriodValue | previousPeriodValue | previousPeriod | currentPeriod | questionCode |
      | 073    | 12000189484 | 1                  | 0                   | 201905         | 201906        | Q104         |
      | 066    | 12000000796 | 1                  | 0                   | 201903         | 201906        | Q601         |
      | 076    | 12000004791 | 1                  | 0                   | 201903         | 201906        | Q601         |
