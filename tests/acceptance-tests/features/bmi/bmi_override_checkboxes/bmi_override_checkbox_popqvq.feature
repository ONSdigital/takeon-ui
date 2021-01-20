Feature: BMI Surveys(Blocks,Bricks) - Override checkbox - Period On Period Question Vs Question(PoPQvQ) Validation rule


  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a BMI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline:  LU-7170 - Check Override functionality for PoPQvQ Validation
    Given I search for the <survey> with <reference> for the previous period <previousPeriod>
    And I run the validation process on <previousQuestion> with <previousPValue>
    And I search for the <survey> with <reference> for the current period <currentPeriod>
    When I run the validation process on <currentQuestion> with <currentPValue>
    And I override the validation for the question <currentQuestion>
    Then the validation message should change to "popqvq override message"

    Examples:
      | survey | reference   | currentPValue | previousPValue | previousQuestion | currentQuestion | previousPeriod | currentPeriod |
      | 073    | 12000228645 | 3             | 4              | Q104             | Q101            | 201905         | 201906        |
      | 074    | 12000229065 | 3             | 4              | Q004             | Q001            | 201905         | 201906        |
