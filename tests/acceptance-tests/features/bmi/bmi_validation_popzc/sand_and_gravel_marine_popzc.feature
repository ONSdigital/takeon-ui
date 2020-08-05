Feature: Sand and Gravel Marine Survey - Period on Period Zero Continuity(PoPZC) Validation rule

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

  Scenario Outline: LU-7035 - Period on Period Zero Continuity Validation
    Given I search for the survey "076" with <reference> for the previous period <previousPeriod>
    And I run the validation process with <previousPeriodValue>
    When I search for the survey "076" with <reference> for the current period <currentPeriod>
    And I run the validation process with <currentPeriodValue>
    Then the validation should return <result> if the "period vs previous frequency period movement to or from zero"
    And the "This is different to the previous submission. If this is 0 or blank, the previous was greater. If this has a value, the previous was 0 or blank" message should <isValidationExists> displayed for question codes
    Examples:
      | reference   | currentPeriodValue | previousPeriodValue | result | previousPeriod | currentPeriod | isValidationExists |
      | 49900004791 | 1                  | 0                   | true   | 201903         | 201906        | be                 |
      | 49900004791 | 0                  | 1                   | true   | 201903         | 201906        | be                 |
      | 49900004791 | 2                  | 3                   | false  | 201903         | 201906        | not be             |
      | 49900004791 | 0                  | 0                   | false  | 201903         | 201906        | not be             |
      | 49900004791 | blank              | blank               | false  | 201903         | 201906        | not be             |
