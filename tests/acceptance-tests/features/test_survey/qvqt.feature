Feature: QvQT validation rule

  Scenario Outline: LU-6401 RSI Survey - current period value vs derived value greater than threshold value
    Given I search for the survey "999A" with <reference> for the period <period>
    When I run the validation process for <totalTurnoverValue> against the <derivedQuestionValue>
    Then the validation should return <result> if the absolute difference between the values are <operator> than the <thresholdValue>

    Examples:
      | period | totalTurnoverValue | derivedQuestionValue | result | operator | thresholdValue |
      | 201803 | 1000               | 1006                 | true   | greater  | 5              |
      | 201806 | 1000               | 994                  | true   | greater  | 5              |
      | 201803 | 1000               | 1005                 | false  | equal    | 5              |
      | 201806 | 1000               | 995                  | false  | equal    | 5              |
      | 201803 | 1000               | 1004                 | false  | less     | 5              |
      | 201803 | 1000               | 996                  | false  | less     | 5              |
