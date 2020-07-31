Feature: Blocks Survey - Period on Period Zero Continuity(PoPZC) Validation rule

  Background:
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I have the "blocks material stock" questions to check
      | question_codes |
      | Q104           |
      | Q114           |
      | Q124           |

  Scenario Outline: LU-7035 - Period on Period Zero Continuity Validation
    Given I search for the survey "073" with <reference> for the previous period <previousPeriod>
    And I run the validation process with <previousPeriodValue>
    When I search for the survey "073" with <reference> for the current period <currentPeriod>
    And I run the validation process with <currentPeriodValue>
    Then the validation should return <result> if the "absolute difference between the values are" <operator> threshold value <thresholdValue>
    And the "This is different to the previous submission. If this is 0 or blank, the previous was greater. If this has a value, the previous was 0 or blank" message should <isValidationExists> displayed for question codes

    Examples:
      | reference   | currentPeriodValue | previousPeriodValue | result | thresholdValue | operator     | previousPeriod | currentPeriod | isValidationExists |
      | 49900189484 | 100001             | 0                   | true   | 100000         | greater than | 201905         | 201906        | be                 |
      | 49900189484 | 0                  | 100001              | true   | 100000         | greater than | 201905         | 201906        | be                 |
      | 49900189484 | 100000             | 100000              | false  | 100000         | equal to     | 201905         | 201906        | not be             |
      | 49900189484 | 100000             | 100000              | false  | 100000         | equal to     | 201905         | 201906        | not be             |
      | 49900189484 | 100000             | 0                   | false  | 100000         | less than    | 201905         | 201906        | not be             |
      | 49900189484 | 0                  | 100000              | false  | 100000         | less than    | 201905         | 201906        | not be             |
      | 49900189484 | 0                  | 0                   | false  | 100000         | equal to     | 201905         | 201906        | not be             |
      | 49900189484 | blank              | blank               | false  | 100000         | equal to     | 201905         | 201906        | not be             |
