Feature: Blocks Survey - Period on Period Movement(PoPM) Validation rule

  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a BMI user I set the search criteria options for the forms returned by the contributor
    And I have the "blocks material stock" questions to check
      | question_codes |
      | Q102           |
      | Q112           |
      | Q103           |
      | Q113           |
      | Q122           |
      | Q123           |

  Scenario Outline: LU-7033 - Period on Period Movement Validation
    Given I search for the survey "073" with <reference> for the previous period <previousPeriod>
    And I run the validation process with <previousPeriodValue>
    When I search for the survey "073" with <reference> for the current period <currentPeriod>
    And I run the validation process with <currentPeriodValue>
    Then the validation should return <result> if the "absolute difference between the values are" <operator> threshold value <thresholdValue>
    And the "popm validation" message should <isValidationExists> displayed for question codes

    Examples:
      | reference   | currentPeriodValue | previousPeriodValue | result | thresholdValue | operator     | previousPeriod | currentPeriod | isValidationExists |
      | 12000189484 | 20000              | 9999                | true   | 10000          | greater than | 201905         | 201906        | be                 |
      | 12000189484 | 9999               | 20000               | true   | 10000          | greater than | 201905         | 201906        | be                 |
      | 12000189484 | 20000              | 10000               | false  | 10000          | equal to     | 201905         | 201906        | not be             |
      | 12000189484 | 10000              | 20000               | false  | 10000          | equal to     | 201905         | 201906        | not be             |
      | 12000189484 | 20000              | 10001               | false  | 10000          | less than    | 201905         | 201906        | not be             |
      | 12000189484 | 10001              | 20000               | false  | 10000          | less than    | 201905         | 201906        | not be             |
      | 12000189484 | 0                  | 0                   | false  | 10000          | equal to     | 201905         | 201906        | not be             |
      | 12000189484 | blank              | blank               | false  | 10000          | equal to     | 201905         | 201906        | not be             |
