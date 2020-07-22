Feature: Sand And Gravel Marine Survey - Period on Period Movement(PoPM) Validation rule

  Background:
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I have the "sand and gravel marine material stock" questions to check
      | question_codes |
      | Q601           |
      | Q602           |
      | Q603           |
      | Q604           |
      | Q605           |
      | Q606           |
      | Q607           |


  Scenario Outline: LU-7033 - Period on Period Movement Validation
    Given I search for the survey "0076" with <reference> for the previous period <previousPeriod>
    And I run the validation process with <previousPeriodValue>
    When I search for the survey "0076" with <reference> for the current period <currentPeriod>
    And I run the validation process with <currentPeriodValue>
    Then the validation should return <result> if the "absolute difference between the values are" <operator> threshold value <thresholdValue>
    And the "This has changed significantly since the last submission" message should <isValidationExists> displayed for question codes

    Examples:
      | reference   | currentPeriodValue | previousPeriodValue | result | thresholdValue | operator     | previousPeriod | currentPeriod | isValidationExists |
      | 49900064408 | 30000              | 9999                | true   | 20000          | greater than | 201903         | 201906        | be                 |
      | 49900064408 | 9999               | 30000               | true   | 20000          | greater than | 201903         | 201906        | be                 |
      | 49900064408 | 30000              | 10000               | false  | 20000          | equal to     | 201903         | 201906        | not be             |
      | 49900064408 | 10000              | 30000               | false  | 20000          | equal to     | 201903         | 201906        | not be             |
      | 49900064408 | 30000              | 10001               | false  | 20000          | less than    | 201903         | 201906        | not be             |
      | 49900064408 | 10001              | 30000               | false  | 20000          | less than    | 201903         | 201906        | not be             |
      | 49900064408 | 0                  | 0                   | false  | 20000          | equal to     | 201903         | 201906        | not be             |
      | 49900064408 | blank              | blank               | false  | 20000          | equal to     | 201903         | 201906        | not be             |
