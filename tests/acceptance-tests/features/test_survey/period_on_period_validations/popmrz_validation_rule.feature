Feature: Test Survey - Period on Period Movement Ratio to Zero(PoPMRZ) Validation rule

  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a Business Survey user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: SP-100 - PoPMRZ Validation on test survey
    Given I search for the survey "999A" with <reference> for the previous period <previousPeriodValue>
    And  the current period sales value is "0"
    And has popmrz value <primaryValue> compared to value <comparisonValue>
    When I search for the survey "999A" with <reference> for the current period <currentPeriodValue>
    And I validate popmrz current period details
    Then the validation should return <result> if the "turnover ratio is" <operator> threshold value <thresholdValue>
    And the "popmrz validation" message should <isValidationExists> displayed for question code "Q23"

    Examples:
      | previousPeriodValue | currentPeriodValue | reference   | thresholdValue | primaryValue | comparisonValue | result | operator     | isValidationExists |
      | 201712              | 201801             | 12345678036 | 10%            | 99           | 1000            | false  | less than    | not be             |
      | 201712              | 201801             | 12345678036 | 10%            | 100          | 1000            | false  | equal to     | not be             |
      | 201712              | 201801             | 12345678036 | 10%            | 101          | 1000            | true   | greater than | be                 |
      | 201712              | 201801             | 12345678036 | 10%            | 0            | 1000            | false  | less than    | not be             |
      | 201712              | 201801             | 12345678036 | 10%            | 0            | 0               | false  | equal to     | not be             |
