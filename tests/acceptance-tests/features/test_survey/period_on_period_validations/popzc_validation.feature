Feature:Test Survey - Period on Period Zero Continuity(PoPZC) Validation rule

  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a Business Survey user I set the search criteria options for the forms returned by the contributor


  Scenario Outline: SP-100 - Period on Period Zero Continuity(PoPZC) Validation on test survey
    Given I search for the survey "999A" with <reference> for the previous period <previousPeriod>
    And I run the validation process on <question> with <previousPeriodValue>
    When I search for the survey "999A" with <reference> for the current period <currentPeriod>
    And I run the validation process on <question> with <currentPeriodValue>
    Then the validation should return <result> if the "period vs previous frequency period movement to or from zero"
    And the "popzc validation" message should <isValidationExists> displayed for question code "Q25"

    Examples:
      | previousPeriod | currentPeriod | reference   | question | previousPeriodValue | currentPeriodValue | isValidationExists | result |
      | 201712         | 201801        | 12345678036 | Q25      | 1                   | 0                  | be                 | true   |
      | 201712         | 201801        | 12345678036 | Q25      | 0                   | 1                  | be                 | true   |
      | 201712         | 201801        | 12345678036 | Q25      | 2                   | 3                  | not be             | false  |
      | 201712         | 201801        | 12345678036 | Q25      | 0                   | 0                  | not be             | false  |
      | 201712         | 201801        | 12345678036 | Q25      | blank               | blank              | not be             | false  |
