Feature: Blocks Survey - Period on Period Question vs Question (PoPQvQ) Validation rule

  Scenario Outline:  LU-7032 - Period on Period Question vs Question Validation Blocks survey on form 3
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the survey "0073" with <reference> for the previous period <previousPeriod>
    And I run the validation process on <previousQuestionCode> with <previousPeriodValue>
    When I search for the survey "0073" with <reference> for the current period <currentPeriod>
    And I run the validation process on <currentQuestionCode> with <currentPeriodValue>
    Then the validation should return <result> if the absolute difference between the periods doesnt meet the <thresholdValue>
    And the "This has changed since last submission" message should <isValidationExists> displayed

    Examples:
      | reference   | currentPeriodValue | previousPeriodValue | result | thresholdValue | isValidationExists | currentQuestionCode | currentQuestionCode | previousPeriod | currentPeriod |
      | 49900008900 | 30000              | 9999                | true   | 20000          | be                 | 104          | 101                 | 201903         | 201906        |
