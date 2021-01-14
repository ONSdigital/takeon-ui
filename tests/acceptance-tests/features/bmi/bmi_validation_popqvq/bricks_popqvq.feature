Feature: Bricks Survey - Period on Period Question vs Question (PoPQvQ) Validation rule

  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in

  Scenario Outline:  LU-7032 - Period on Period Question vs Question Validation - Closing Stock vs Opening Stock(Commons)
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the survey "074" with <reference> for the previous period <previousPeriod>
    And I run the validation process on <previousQuestionCode> with <previousPeriodValue>
    When I search for the survey "074" with <reference> for the current period <currentPeriod>
    And I run the validation process on <currentQuestionCode> with <currentPeriodValue>
    Then the validation should return <result> if the "values are not equal"
    And the "popqvq validation" message should <isValidationExists> displayed for question code "Q001"

    Examples:
      | reference   | currentPeriodValue | previousPeriodValue | result | isValidationExists | previousQuestionCode | currentQuestionCode | previousPeriod | currentPeriod |
      | 12000229065 | 3                  | 4                   | true   | be                 | Q004                 | Q001                | 201905         | 201906        |
      | 12000229065 | 4                  | 3                   | true   | be                 | Q004                 | Q001                | 201905         | 201906        |
      | 12000229065 | 3                  | 3                   | false  | not be             | Q004                 | Q001                | 201905         | 201906        |
      | 12000229065 | blank              | blank               | false  | not be             | Q004                 | Q001                | 201905         | 201906        |


  Scenario Outline:  LU-7032 - Period on Period Question vs Question Validation - Closing Stock vs Opening Stock(Facings)
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the survey "074" with <reference> for the previous period <previousPeriod>
    And I run the validation process on <previousQuestionCode> with <previousPeriodValue>
    When I search for the survey "074" with <reference> for the current period <currentPeriod>
    And I run the validation process on <currentQuestionCode> with <currentPeriodValue>
    Then the validation should return <result> if the "values are not equal"
    And the "popqvq validation" message should <isValidationExists> displayed for question code "Q011"

    Examples:
      | reference   | currentPeriodValue | previousPeriodValue | result | isValidationExists | previousQuestionCode | currentQuestionCode | previousPeriod | currentPeriod |
      | 12000229065 | 3                  | 4                   | true   | be                 | Q014                 | Q011                | 201905         | 201906        |
      | 12000229065 | 4                  | 3                   | true   | be                 | Q014                 | Q011                | 201905         | 201906        |
      | 12000229065 | 3                  | 3                   | false  | not be             | Q014                 | Q011                | 201905         | 201906        |
      | 12000229065 | blank              | blank               | false  | not be             | Q014                 | Q011                | 201905         | 201906        |


  Scenario Outline:  LU-7032 - Period on Period Question vs Question Validation - Closing Stock vs Opening Stock(Engineering)
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the survey "074" with <reference> for the previous period <previousPeriod>
    And I run the validation process on <previousQuestionCode> with <previousPeriodValue>
    When I search for the survey "074" with <reference> for the current period <currentPeriod>
    And I run the validation process on <currentQuestionCode> with <currentPeriodValue>
    Then the validation should return <result> if the "values are not equal"
    And the "popqvq validation" message should <isValidationExists> displayed for question code "Q021"

    Examples:
      | reference   | currentPeriodValue | previousPeriodValue | result | isValidationExists | previousQuestionCode | currentQuestionCode | previousPeriod | currentPeriod |
      | 12000229065 | 3                  | 4                   | true   | be                 | Q024                 | Q021                | 201905         | 201906        |
      | 12000229065 | 4                  | 3                   | true   | be                 | Q024                 | Q021                | 201905         | 201906        |
      | 12000229065 | 3                  | 3                   | false  | not be             | Q024                 | Q021                | 201905         | 201906        |
      | 12000229065 | blank              | blank               | false  | not be             | Q024                 | Q021                | 201905         | 201906        |


  Scenario Outline:  LU-7032 - Period on Period Question vs Question Validation - Brick type
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the survey "074" with <reference> for the previous period <previousPeriod>
    And I run the validation process on <previousQuestionCode> with <previousPeriodValue>
    When I search for the survey "074" with <reference> for the current period <currentPeriod>
    And I run the validation process on <currentQuestionCode> with <currentPeriodValue>
    Then the validation should return <result> if the "values are not equal"
    And the "popqvq validation" message should <isValidationExists> displayed for question code "Q8000"

    Examples:
      | reference   | currentPeriodValue | previousPeriodValue | result | isValidationExists | previousQuestionCode | currentQuestionCode | previousPeriod | currentPeriod |
      | 12000229065 | 3                  | 4                   | true   | be                 | Q8000                | Q8000               | 201905         | 201906        |
      | 12000229065 | 4                  | 3                   | true   | be                 | Q8000                | Q8000               | 201905         | 201906        |
      | 12000229065 | 3                  | 3                   | false  | not be             | Q8000                | Q8000               | 201905         | 201906        |
      | 12000229065 | blank              | blank               | false  | not be             | Q8000                | Q8000               | 201905         | 201906        |
