Feature: Blocks Survey - Period on Period Question vs Question (PoPQvQ) Validation rule

  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in

  Scenario Outline:  LU-7032 - Period on Period Question vs Question Validation - Aggregate blocks Closing Stock vs Opening Stock(Dense Aggregate)
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the survey "073" with <reference> for the previous period <previousPeriod>
    And I run the validation process on <previousQuestionCode> with <previousPeriodValue>
    When I search for the survey "073" with <reference> for the current period <currentPeriod>
    And I run the validation process on <currentQuestionCode> with <currentPeriodValue>
    Then the validation should return <result> if the "values are not equal"
    And the "popqvq validation" message should <isValidationExists> displayed for question code "Q101"

    Examples:
      | reference   | currentPeriodValue | previousPeriodValue | result | isValidationExists | previousQuestionCode | currentQuestionCode | previousPeriod | currentPeriod |
      | 49900228645 | 3                  | 4                   | true   | be                 | Q104                 | Q101                | 201905         | 201906        |
      | 49900228645 | 4                  | 3                   | true   | be                 | Q104                 | Q101                | 201905         | 201906        |
      | 49900228645 | 3                  | 3                   | false  | not be             | Q104                 | Q101                | 201905         | 201906        |
      | 49900228645 | blank              | blank               | false  | not be             | Q104                 | Q101                | 201905         | 201906        |


  Scenario Outline:  LU-7032 - Period on Period Question vs Question Validation - Aggregate blocks Closing Stock vs Opening Stock(Lightweight Aggregate)
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the survey "073" with <reference> for the previous period <previousPeriod>
    And I run the validation process on <previousQuestionCode> with <previousPeriodValue>
    When I search for the survey "073" with <reference> for the current period <currentPeriod>
    And I run the validation process on <currentQuestionCode> with <currentPeriodValue>
    Then the validation should return <result> if the "values are not equal"
    And the "popqvq validation" message should <isValidationExists> displayed for question code "Q111"

    Examples:
      | reference   | currentPeriodValue | previousPeriodValue | result | isValidationExists | previousQuestionCode | currentQuestionCode | previousPeriod | currentPeriod |
      | 49900228645 | 3                  | 4                   | true   | be                 | Q114                 | Q111                | 201905         | 201906        |
      | 49900228645 | 4                  | 3                   | true   | be                 | Q114                 | Q111                | 201905         | 201906        |
      | 49900228645 | 3                  | 3                   | false  | not be             | Q114                 | Q111                | 201905         | 201906        |
      | 49900228645 | blank              | blank               | false  | not be             | Q114                 | Q111                | 201905         | 201906        |


  Scenario Outline:  LU-7032 - Period on Period Question vs Question Validation - Aerated blocks Closing Stock vs Opening Stock
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the survey "073" with <reference> for the previous period <previousPeriod>
    And I run the validation process on <previousQuestionCode> with <previousPeriodValue>
    When I search for the survey "073" with <reference> for the current period <currentPeriod>
    And I run the validation process on <currentQuestionCode> with <currentPeriodValue>
    Then the validation should return <result> if the "values are not equal"
    And the "popqvq validation" message should <isValidationExists> displayed for question code "Q121"

    Examples:
      | reference   | currentPeriodValue | previousPeriodValue | result | isValidationExists | previousQuestionCode | currentQuestionCode | previousPeriod | currentPeriod |
      | 49900228645 | 3                  | 4                   | true   | be                 | Q124                 | Q121                | 201905         | 201906        |
      | 49900228645 | 4                  | 3                   | true   | be                 | Q124                 | Q121                | 201905         | 201906        |
      | 49900228645 | 3                  | 3                   | false  | not be             | Q124                 | Q121                | 201905         | 201906        |
      | 49900228645 | blank              | blank               | false  | not be             | Q124                 | Q121                | 201905         | 201906        |
