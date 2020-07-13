Feature: Blocks Survey - Period on Period Question vs Question (PoPQvQ) Validation rule

  Scenario Outline:  LU-7032 - Period on Period Question vs Question Validation Blocks survey on form 3
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the survey "0073" with <reference> for the previous period <previousPeriod>
    And I run the validation process on <previousQuestionCode> with <previousPeriodValue>
    When I search for the survey "0073" with <reference> for the current period <currentPeriod>
    And I run the validation process on <currentQuestionCode> with <currentPeriodValue>
    Then the validation should return <result> if the "values are not equal"
    And the "This has changed since last submission" message should <isValidationExists> displayed

    Examples:
      | reference   | currentPeriodValue | previousPeriodValue | result | isValidationExists | previousQuestionCode | currentQuestionCode | previousPeriod | currentPeriod |
      | 49900228645 | 3                  | 4                   | true   | be                 | 104                  | 101                 | 201905         | 201906        |
      | 49900228645 | 4                  | 3                   | true   | be                 | 104                  | 101                 | 201905         | 201906        |
      | 49900228645 | 3                  | 3                   | false  | not be             | 104                  | 101                 | 201905         | 201906        |
      | 49900228645 | blank              | blank               | false  | not be             | 104                  | 101                 | 201905         | 201906        |


  Scenario Outline:  LU-7032 - Period on Period Question vs Question Validation Blocks survey on form 3
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the survey "0073" with <reference> for the previous period <previousPeriod>
    And I run the validation process on <previousQuestionCode> with <previousPeriodValue>
    When I search for the survey "0073" with <reference> for the current period <currentPeriod>
    And I run the validation process on <currentQuestionCode> with <currentPeriodValue>
    Then the validation should return <result> if the "values are not equal"
    And the "This has changed since last submission" message should <isValidationExists> displayed

    Examples:
      | reference   | currentPeriodValue | previousPeriodValue | result | isValidationExists | previousQuestionCode | currentQuestionCode | previousPeriod | currentPeriod |
      | 49900228645 | 3                  | 4                   | true   | be                 | 114                  | 111                 | 201905         | 201906        |
      | 49900228645 | 4                  | 3                   | true   | be                 | 114                  | 111                 | 201905         | 201906        |
      | 49900228645 | 3                  | 3                   | false  | not be             | 114                  | 111                 | 201905         | 201906        |
      | 49900228645 | blank              | blank               | false  | not be             | 114                  | 111                 | 201905         | 201906        |


  Scenario Outline:  LU-7032 - Period on Period Question vs Question Validation Blocks survey on form 3
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the survey "0073" with <reference> for the previous period <previousPeriod>
    And I run the validation process on <previousQuestionCode> with <previousPeriodValue>
    When I search for the survey "0073" with <reference> for the current period <currentPeriod>
    And I run the validation process on <currentQuestionCode> with <currentPeriodValue>
    Then the validation should return <result> if the "values are not equal"
    And the "This has changed since last submission" message should <isValidationExists> displayed

    Examples:
      | reference   | currentPeriodValue | previousPeriodValue | result | isValidationExists | previousQuestionCode | currentQuestionCode | previousPeriod | currentPeriod |
      | 49900228645 | 3                  | 4                   | true   | be                 | 124                  | 121                 | 201905         | 201906        |
      | 49900228645 | 4                  | 3                   | true   | be                 | 124                  | 121                 | 201905         | 201906        |
      | 49900228645 | 3                  | 3                   | false  | not be             | 124                  | 121                 | 201905         | 201906        |
      | 49900228645 | blank              | blank               | false  | not be             | 124                  | 121                 | 201905         | 201906        |


  Scenario Outline:  LU-7032 - Period on Period Question vs Question Validation Blocks survey on form 3
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the survey "0073" with <reference> for the previous period <previousPeriod>
    And I run the validation process on <previousQuestionCode> with <previousPeriodValue>
    When I search for the survey "0073" with <reference> for the current period <currentPeriod>
    And I run the validation process on <currentQuestionCode> with <currentPeriodValue>
    Then the validation should return <result> if the "values are not equal"
    And the "This has changed since last submission" message should <isValidationExists> displayed

    Examples:
      | reference   | currentPeriodValue | previousPeriodValue | result | isValidationExists | previousQuestionCode | currentQuestionCode | previousPeriod | currentPeriod |
      | 49900228645 | 3                  | 4                   | true   | be                 | 124                  | 121                 | 201905         | 201906        |
      | 49900228645 | 4                  | 3                   | true   | be                 | 124                  | 121                 | 201905         | 201906        |
      | 49900228645 | 3                  | 3                   | false  | not be             | 124                  | 121                 | 201905         | 201906        |
      | 49900228645 | blank              | blank               | false  | not be             | 124                  | 121                 | 201905         | 201906        |

  Scenario Outline:  LU-7032 - Period on Period Question vs Question Validation Bricks survey on form 3
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the survey "0074" with <reference> for the previous period <previousPeriod>
    And I run the validation process on <previousQuestionCode> with <previousPeriodValue>
    When I search for the survey "0074" with <reference> for the current period <currentPeriod>
    And I run the validation process on <currentQuestionCode> with <currentPeriodValue>
    Then the validation should return <result> if the "values are not equal"
    And the "This has changed since last submission" message should <isValidationExists> displayed for question code "Q101"

    Examples:
      | reference   | currentPeriodValue | previousPeriodValue | result | isValidationExists | previousQuestionCode | currentQuestionCode | previousPeriod | currentPeriod |
      | 49900228645 | 3                  | 4                   | true   | be                 | 104                  | 101                 | 201905         | 201906        |
      | 49900228645 | 4                  | 3                   | true   | be                 | 104                  | 101                 | 201905         | 201906        |
      | 49900228645 | 3                  | 3                   | false  | not be             | 104                  | 101                 | 201905         | 201906        |
      | 49900228645 | blank              | blank               | false  | not be             | 104                  | 101                 | 201905         | 201906        |
