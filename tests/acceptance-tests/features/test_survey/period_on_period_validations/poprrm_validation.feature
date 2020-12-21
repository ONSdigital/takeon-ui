Feature:Test Survey - Period on Period Ratio of Ratios Movement(PoPRRM) Validation rule

  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a Business Survey user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: SP-100 - PoPRRM Validation on test survey
    Given I search for the survey "999A" with <reference> for the previous period <previousPeriodValue>
    And has poprrm value <ppPrimaryValue> compared to value <ppComparisonValue>
    When I search for the survey "999A" with <reference> for the current period <currentPeriodValue>
    And has poprrm value <cpPrimaryValue> compared to value <cpComparisonValue>
    And I validate the current period details for <factor> factor type
    Then the validation should return <result> if the "period on period ratio of ratios movement is" <operator> threshold value <thresholdValue>
    And the "poprrm validation" message should <isValidationExists> displayed for question code "Q28"

    Examples:
      | previousPeriodValue | currentPeriodValue | reference   | ppPrimaryValue | ppComparisonValue | cpPrimaryValue | cpComparisonValue | factor         | result | operator     | thresholdValue | isValidationExists |
      | 201712              | 201801             | 12345678036 | 10             | 400               | 10             | 100               | increase       | true   | equal to     | 4              | be                 |
      | 201712              | 201801             | 12345678036 | 10             | 100               | 10             | 400               | decrease       | true   | equal to     | 4              | be                 |
      | 201712              | 201801             | 12345678036 | 10             | 400               | 11             | 100               | increase       | true   | greater than | 4              | be                 |
      | 201712              | 201801             | 12345678036 | 10             | 100               | 11             | 400               | decrease       | false  | less than    | 4              | not be             |
      | 201712              | 201801             | 12345678036 | 10             | 400               | 9              | 100               | increase       | false  | less than    | 4              | not be             |
      | 201712              | 201801             | 12345678036 | 10             | 100               | 9              | 400               | decrease       | true   | greater than | 4              | be                 |
      | 201712              | 201801             | 12345678036 | 0              | 0                 | 0              | 0                 | not-applicable | false  | all zeros    | 4              | not be             |
      | 201712              | 201801             | 12345678036 | blank          | blank             | blank          | blank             | not-applicable | false  | all blanks   | 4              | not be             |
