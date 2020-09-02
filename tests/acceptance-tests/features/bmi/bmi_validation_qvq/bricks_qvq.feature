Feature: Bricks Survey - Question vs Derived Question (QvQ) Validation rule

  Background:
    Given As a BMI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: LU-7034 - Question vs Question Validation BMI survey on form 4
    Given I search for the survey "074" with <reference> for the current period <period>
    And I submit the "bricks opening stock dense aggregate" <values> for questions
      | question_codes |
      | Q001           |
      | Q002           |
      | Q003           |
    When I run the validation process for <bricksClosingStock> against the <derivedTotal>
      | closing_stock_question | derived_question |
      | Q004                   | Q9204            |
    Then the validation should return <result> if the "values are not equal"
    And the "qvq validation" message should <isValidationExists> displayed for question code "Q004"
    Examples:
      | period | reference   | values            | isValidationExists | result | derivedTotal | bricksClosingStock |
      | 201905 | 49900356828 | 1,1,1             | be                 | true   | 1            | 2                  |
      | 201905 | 49900356828 | 1,1,3             | be                 | true   | -1           | 2                  |
      | 201905 | 49900356828 | 2,1,1             | not be             | false  | 2            | 2                  |
      | 201905 | 49900356828 | 0,0,0             | not be             | false  | 0            | 0                  |
      | 201905 | 49900356828 | blank,blank,blank | not be             | false  | blank        | blank              |


  Scenario Outline: LU-7034 - Question vs Question Validation BMI survey on form 4
    Given I search for the survey "074" with <reference> for the current period <period>
    And I submit the "bricks opening stock dense aggregate" <values> for questions
      | question_codes |
      | Q011           |
      | Q012           |
      | Q013           |
    When I run the validation process for <bricksClosingStock> against the <derivedTotal>
      | closing_stock_question | derived_question |
      | Q014                   | Q9214            |
    Then the validation should return <result> if the "values are not equal"
    And the "qvq validation" message should <isValidationExists> displayed for question code "Q014"
    Examples:
      | period | reference   | values            | isValidationExists | result | derivedTotal | bricksClosingStock |
      | 201906 | 49900356828 | 1,1,1             | be                 | true   | 1            | 2                  |
      | 201906 | 49900356828 | 1,1,3             | be                 | true   | -1           | 2                  |
      | 201906 | 49900356828 | 2,1,1             | not be             | false  | 2            | 2                  |
      | 201906 | 49900356828 | 0,0,0             | not be             | false  | 0            | 0                  |
      | 201906 | 49900356828 | blank,blank,blank | not be             | false  | blank        | blank              |

  Scenario Outline: LU-7034 - Question vs Question Validation BMI survey on form 4
    Given I search for the survey "074" with <reference> for the current period <period>
    And I submit the "bricks opening stock dense aggregate" <values> for questions
      | question_codes |
      | Q021           |
      | Q022           |
      | Q023           |
    When I run the validation process for <bricksClosingStock> against the <derivedTotal>
      | closing_stock_question | derived_question |
      | Q024                   | Q9224            |
    Then the validation should return <result> if the "values are not equal"
    And the "qvq validation" message should <isValidationExists> displayed for question code "Q024"
    Examples:
      | period | reference   | values            | isValidationExists | result | derivedTotal | bricksClosingStock |
      | 201905 | 49900356828 | 1,1,1             | be                 | true   | 1            | 2                  |
      | 201905 | 49900356828 | 1,1,3             | be                 | true   | -1           | 2                  |
      | 201905 | 49900356828 | 2,1,1             | not be             | false  | 2            | 2                  |
      | 201905 | 49900356828 | 0,0,0             | not be             | false  | 0            | 0                  |
      | 201905 | 49900356828 | blank,blank,blank | not be             | false  | blank        | blank              |
