Feature: Test Survey - Period on Period Question vs Question(PoPQvQ) Validation rule

  Background:

    Given As a Business Survey user I set the search criteria options for the forms returned by the contributor


  Scenario Outline: SP-100 - Period on Period Question vs Question(PoPQvQ) Validation on test survey
    Given I search for the survey "999A" with <reference> for the previous period <previousPeriod>
    And I run the validation process on <previousQuestionCode> with <previousPeriodValue>
    When I search for the survey "999A" with <reference> for the current period <currentPeriod>
    And I run the validation process on <currentQuestionCode> with <currentPeriodValue>
    Then the validation should return <result> if the "values are not equal"
    And the "popqvq validation" message should <isValidationExists> displayed for question code "Q26"

    Examples:
      | reference   | currentPeriodValue | previousPeriodValue | result | isValidationExists | previousQuestionCode | currentQuestionCode | previousPeriod | currentPeriod |
      | 12345678036 | 3                  | 4                   | true   | be                 | Q27                  | Q26                 | 201712         | 201801        |
      | 12345678036 | 4                  | 3                   | true   | be                 | Q27                  | Q26                 | 201712         | 201801        |
      | 12345678036 | 3                  | 3                   | false  | not be             | Q27                  | Q26                 | 201712         | 201801        |
      | 12345678036 | blank              | blank               | false  | not be             | Q27                  | Q26                 | 201712         | 201801        |
