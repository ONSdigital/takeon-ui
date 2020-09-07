Feature: BMI Surveys(Blocks,Bricks,Sand Gravel Land and Sand Gravel Marine) - Override checkbox - Period on Period Movement Value(PoPM) Validation rule


  Background:
    Given As a BMI user I set the search criteria options for the forms returned by the contributor


  Scenario Outline: LU-7033 - Period on Period Movement Validation
    Given I search for the <survey> with <reference> for the previous period <previousPeriod>
    And I run the validation process on <questionCode> with <previousPeriodValue>
    And I search for the survey "073" with <reference> for the current period <currentPeriod>
    When I run the validation process on <questionCode> with <currentPeriodValue>
    And I override the validation for the question <questionCode>
    Then the validation message should change to "popm override message"

    Examples:
      | survey | reference   | currentPeriodValue | previousPeriodValue | previousPeriod | currentPeriod | questionCode |
      | 073    | 49900189484 | 20000              | 9999                | 201905         | 201906        | Q102         |
      | 074    | 49900423293 | 2000000            | 999999              | 201905         | 201906        | Q002         |
      | 066    | 49900008900 | 30000              | 9999                | 201903         | 201906        | Q601         |
      | 076    | 49900064408 | 30000              | 9999                | 201903         | 201906        | Q601         |

