Feature: Bricks Survey - Period on Period Movement(PoPM) Validation rule

  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a BMI user I set the search criteria options for the forms returned by the contributor
    And I have the "bricks material stock" questions to check
      | question_codes |
      | Q002           |
      | Q012           |
      | Q022           |
      | Q003           |
      | Q013           |
      | Q023           |

  Scenario Outline: LU-7033 - Period on Period Movement Validation
    Given I search for the survey "074" with <reference> for the previous period <previousPeriod>
    And I run the validation process with <previousPeriodValue>
    When I search for the survey "074" with <reference> for the current period <currentPeriod>
    And I run the validation process with <currentPeriodValue>
    Then the validation should return <result> if the "absolute difference between the values are" <operator> threshold value <thresholdValue>
    And the "popm validation" message should <isValidationExists> displayed for question codes

    Examples:
      | reference   | currentPeriodValue | previousPeriodValue | result | thresholdValue | operator     | previousPeriod | currentPeriod | isValidationExists |
      | 12000423293 | 2000000            | 999999              | true   | 1000000        | greater than | 201905         | 201906        | be                 |
      | 12000423293 | 999999             | 2000000             | true   | 1000000        | greater than | 201905         | 201906        | be                 |
      | 12000423293 | 2000000            | 1000000             | false  | 1000000        | equal to     | 201905         | 201906        | not be             |
      | 12000423293 | 1000000            | 2000000             | false  | 1000000        | equal to     | 201905         | 201906        | not be             |
      | 12000423293 | 2000000            | 1000001             | false  | 1000000        | less than    | 201905         | 201906        | not be             |
      | 12000423293 | 1000001            | 2000000             | false  | 1000000        | less than    | 201905         | 201906        | not be             |
      | 12000423293 | 0                  | 0                   | false  | 1000000        | equal to     | 201905         | 201906        | not be             |
      | 12000423293 | blank              | blank               | false  | 1000000        | equal to     | 201905         | 201906        | not be             |
