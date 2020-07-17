Feature: Blocks Survey - Period on Period Movement(PoPM) Validation rule

  Scenario Outline:  LU-7033 - Period on Period Movement Validation
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the survey "0073" with <reference> for the previous period <previousPeriod>
    And I run the validation process on <questionCode> with <previousPeriodValue>
    When I search for the survey "0073" with <reference> for the current period <currentPeriod>
    And I run the validation process on <questionCode> with <currentPeriodValue>
    Then the validation should return <result> if the "absolute difference between the values are" <operator> threshold value <thresholdValue>
    And the "This has changed significantly since the last submission" message should <isValidationExists> displayed for question code "Q102"

    Examples:
      | reference   | currentPeriodValue | previousPeriodValue | result | thresholdValue | operator     | questionCode | previousPeriod | currentPeriod | isValidationExists |
      | 49900189484 | 20000              | 9999                | true   | 10000          | greater than | Q102         | 201905         | 201906        | be                 |
      | 49900189484 | 9999               | 20000               | true   | 10000          | greater than | Q102         | 201905         | 201906        | be                 |
      | 49900189484 | 20000              | 10000               | false  | 10000          | equal to     | Q102         | 201905         | 201906        | be                 |
      | 49900189484 | 10000              | 20000               | false  | 10000          | equal to     | Q102         | 201905         | 201906        | be                 |
      | 49900189484 | 20000              | 10001               | false  | 10000          | less than    | Q102         | 201905         | 201906        | be                 |
      | 49900189484 | 10001              | 20000               | false  | 10000          | less than    | Q102         | 201905         | 201906        | be                 |
      | 49900189484 | 0                  | 0                   | false  | 10000          | equal to     | Q102         | 201905         | 201906        | be                 |
      | 49900189484 | blank              | blank               | false  | 10000          | equal to     | Q102         | 201905         | 201906        | be                 |