Feature: Test Survey - Question vs Question(QvQ) Validation rule

  Background:
    Given As a Business Survey user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: SP-100 - Question vs Question(QvQ) Validation on test survey
    Given I search for the survey "999A" with <reference> for the current period <period>
    And I submit the "sales" <values> for questions
      | question_codes |
      | Q9             |
      | Q10            |
    When I trigger the validation process
    Then the "qvq validation" message should <isValidationExists> displayed for question code "Q9"
    Examples:
      | period | reference   | values | isValidationExists |
      | 201712 | 12345678036 | 2,1    | be                 |
      | 201712 | 12345678036 | 1,1    | not be             |
      | 201712 | 12345678036 | 1,2    | not be             |
