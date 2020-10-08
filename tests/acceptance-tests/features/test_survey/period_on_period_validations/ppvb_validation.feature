Feature:Test Survey - Previous Period Value Blank (PPVB) Validation rule

  Background:
    Given As a Business Survey user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: SP-100 - Previous Period Value Blank Validation on test survey
    Given I search for the survey "999A" with <reference> for the previous period <PPeriod>
    And I run the validation process on <question> with <ppValue>
    When I search for the survey "999A" with <reference> for the current period <CPeriod>
    And I run the validation process on <question> with <cpValue>
    Then the "ppvb validation" message should <isValidationExists> displayed for question code "Q21"

    Examples:
      | PPeriod | CPeriod | reference   | question | ppValue | cpValue | isValidationExists |
      | 201712  | 201801  | 12345678036 | Q21      | blank   | blank   | be                 |
      | 201712  | 201801  | 12345678036 | Q21      | blank   | 1       | be                 |
      | 201712  | 201801  | 12345678036 | Q21      | 1       | blank   | not be             |
      | 201712  | 201801  | 12345678036 | Q21      | 1       | 1       | not be             |
