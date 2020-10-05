Feature: Test Survey - Question vs Derived Question (QvDQ) Validation rule

  Background:
    Given As a Business Survey user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: SP-100 - Question vs Derived Question(QvDQ) Validation on test survey
    Given I search for the survey "999A" with <reference> for the current period <period>
    And I submit the "stock material values" <values> for questions
      | question_codes |
      | Q18            |
      | Q19            |
      | Q20            |
    When I run the validation process for <primaryQuestionValue> against the <derivedTotal>
      | primary_question | derived_question |
      | Q16              | Q17              |
    Then the validation should return <result> if the "values are not equal"
    And the "qvdq validation" message should <isValidationExists> displayed for question code "Q16"
    Examples:
      | period | reference   | values            | isValidationExists | result | derivedTotal | primaryQuestionValue |
      | 201712 | 12345678036 | 1,1,1             | be                 | true   | 3            | 2                    |
      | 201712 | 12345678036 | 1,1,-4            | be                 | true   | -2           | 2                    |
      | 201712 | 12345678036 | 2,1,1             | not be             | false  | 4            | 4                    |
      | 201712 | 12345678036 | 0,0,0             | not be             | false  | 0            | 0                    |
      | 201712 | 12345678036 | blank,blank,blank | not be             | false  | blank        | blank                |


