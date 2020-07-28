Feature: Blocks Survey - Question vs Derived Question (QvQ) Validation rule

  Background:
    Given As a BMI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: LU-7034 - Question vs Question Validation BMI survey on form 3
    Given I search for the survey "073" with <reference> for the current period <period>
    And I submit the "blocks opening stock dense aggregate" <values> for questions
      | question_codes |
      | Q101           |
      | Q102           |
      | Q103           |
    When I run the validation process for <blocksClosingStock> against the <derivedTotal>
      | closing_stock_question | derived_question |
      | Q104                   | Q9001            |
    Then the validation should return <result> if the "values are not equal"
    And the <validation> message should <isValidationExists> displayed for question code "Q104"
    Examples:
      | period | reference   | validation                                   | values            | isValidationExists | result | derivedTotal | blocksClosingStock |
      | 201905 | 49900138556 | This total is not equal to the derived total | 1,1,1             | be                 | true   | 1            | 2                  |
      | 201905 | 49900138556 | This total is not equal to the derived total | 1,1,3             | be                 | true   | -1           | 2                  |
      | 201905 | 49900138556 | This total is not equal to the derived total | 2,1,1             | not be             | false  | 2            | 2                  |
      | 201905 | 49900138556 | This total is not equal to the derived total | 0,0,0             | not be             | false  | 0            | 0                  |
      | 201905 | 49900138556 | This total is not equal to the derived total | blank,blank,blank | not be             | false  | blank        | blank              |


  Scenario Outline: LU-7034 - Question vs Question Validation BMI survey on form 3
    Given I search for the survey "073" with <reference> for the current period <period>
    And I submit the "blocks opening stock dense aggregate" <values> for questions
      | question_codes |
      | Q111           |
      | Q112           |
      | Q113           |
    When I run the validation process for <blocksClosingStock> against the <derivedTotal>
      | closing_stock_question | derived_question |
      | Q114                   | Q9002            |
    Then the validation should return <result> if the "values are not equal"
    And the <validation> message should <isValidationExists> displayed for question code "Q114"
    Examples:
      | period | reference   | validation                                   | values            | isValidationExists | result | derivedTotal | blocksClosingStock |
      | 201905 | 49900138556 | This total is not equal to the derived total | 1,1,1             | be                 | true   | 1            | 2                  |
      | 201905 | 49900138556 | This total is not equal to the derived total | 1,1,3             | be                 | true   | -1           | 2                  |
      | 201905 | 49900138556 | This total is not equal to the derived total | 2,1,1             | not be             | false  | 2            | 2                  |
      | 201905 | 49900138556 | This total is not equal to the derived total | 0,0,0             | not be             | false  | 0            | 0                  |
      | 201905 | 49900138556 | This total is not equal to the derived total | blank,blank,blank | not be             | false  | blank        | blank              |

  Scenario Outline: LU-7034 - Question vs Question Validation BMI survey on form 3
    Given I search for the survey "073" with <reference> for the current period <period>
    And I submit the "blocks opening stock dense aggregate" <values> for questions
      | question_codes |
      | Q121           |
      | Q122           |
      | Q123           |
    When I run the validation process for <blocksClosingStock> against the <derivedTotal>
      | closing_stock_question | derived_question |
      | Q124                   | Q9003            |
    Then the validation should return <result> if the "values are not equal"
    And the <validation> message should <isValidationExists> displayed for question code "Q124"
    Examples:
      | period | reference   | validation                                   | values            | isValidationExists | result | derivedTotal | blocksClosingStock |
      | 201905 | 49900138556 | This total is not equal to the derived total | 1,1,1             | be                 | true   | 1            | 2                  |
      | 201905 | 49900138556 | This total is not equal to the derived total | 1,1,3             | be                 | true   | -1           | 2                  |
      | 201905 | 49900138556 | This total is not equal to the derived total | 2,1,1             | not be             | false  | 2            | 2                  |
      | 201905 | 49900138556 | This total is not equal to the derived total | 0,0,0             | not be             | false  | 0            | 0                  |
      | 201905 | 49900138556 | This total is not equal to the derived total | blank,blank,blank | not be             | false  | blank        | blank              |
