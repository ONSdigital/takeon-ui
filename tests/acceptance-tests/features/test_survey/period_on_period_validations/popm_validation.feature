Feature:Test Survey - Period on Period Movement(PoPM) Validation rule

  Background:
    Given As a Business Survey user I set the search criteria options for the forms returned by the contributor


  Scenario Outline: SP-100 - Period on Period Movement(PoPM) Validation on test survey
    Given I search for the survey "999A" with <reference> for the previous period <previousPeriod>
    And I run the validation process on <question> with <previousPeriodValue>
    When I search for the survey "999A" with <reference> for the current period <currentPeriod>
    And I run the validation process on <question> with <currentPeriodValue>
    Then the validation should return <result> if the "absolute difference between the values are" <operator> threshold value <thresholdValue>
    And the "popm validation" message should <isValidationExists> displayed for question code "Q22"

    Examples:
      | previousPeriod | currentPeriod | reference   | question | previousPeriodValue | currentPeriodValue | result | thresholdValue | operator     | isValidationExists |
      | 201712         | 201801        | 12345678036 | Q22      | 9999                | 30000              | true   | 20000          | greater than | be                 |
      | 201712         | 201801        | 12345678036 | Q22      | 30000               | 9999               | true   | 20000          | greater than | be                 |
      | 201712         | 201801        | 12345678036 | Q22      | 10000               | 30000              | false  | 20000          | equal to     | not be             |
      | 201712         | 201801        | 12345678036 | Q22      | 30000               | 10000              | false  | 20000          | equal to     | not be             |
      | 201712         | 201801        | 12345678036 | Q22      | 10001               | 30000              | false  | 20000          | less than    | not be             |
      | 201712         | 201801        | 12345678036 | Q22      | 30000               | 10001              | false  | 20000          | less than    | not be             |
      | 201712         | 201801        | 12345678036 | Q22      | 0                   | 0                  | false  | 20000          | equal to     | not be             |
      | 201712         | 201801        | 12345678036 | Q22      | blank               | blank              | false  | 20000          | equal to     | not be             |
