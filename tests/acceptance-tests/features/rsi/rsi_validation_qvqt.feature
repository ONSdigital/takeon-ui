Feature: RSI Survey - QvQT validation rule

  Background:
    Given As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: LU-6402 - current period total turnover value vs derived value greater than threshold value on form 6
    Given I search for the survey "023" with <reference> for the current period <period>
    And I submit the "commodity" <values> for questions
      | question_codes |
      | Q22            |
      | Q23            |
      | Q24            |
      | Q25            |
      | Q26            |
    When I run the validation process for <totalTurnoverValue> against the <derivedValue>
    Then the validation should return <result> if the "absolute difference between the values are" <operator> threshold value <thresholdValue>
    And the <validation> message should <isValidationExists> displayed for question code "Q20"

    Examples:
      | reference   | period | values    | totalTurnoverValue | derivedValue | result | operator     | thresholdValue | validation                                                | isValidationExists |
      | 49900694171 | 201903 | 1,1,1,0,1 | 10                 | 4            | true   | greater than | 5              | Total different to calculated total (allowing for margin) | be                 |
      | 49900694171 | 201903 | 1,2,3,2,2 | 4                  | 10           | true   | greater than | 5              | Total different to calculated total (allowing for margin) | be                 |
      | 49900694171 | 201903 | 1,1,1,1,1 | 10                 | 5            | false  | equal to     | 5              | Total different to calculated total (allowing for margin) | not be             |
      | 49900694171 | 201903 | 1,2,3,2,2 | 5                  | 10           | false  | equal to     | 5              | Total different to calculated total (allowing for margin) | not be             |
      | 49900694171 | 201903 | 1,1,1,1,2 | 10                 | 6            | false  | less than    | 5              | Total different to calculated total (allowing for margin) | not be             |
      | 49900694171 | 201903 | 1,2,3,2,2 | 6                  | 10           | false  | less than    | 5              | Total different to calculated total (allowing for margin) | not be             |


  Scenario Outline: LU-6402 - current period total turnover value vs derived value greater than threshold value on form 7
    Given I search for the survey "023" with <reference> for the current period <period>
    And I submit the "commodity" <values> for questions
      | question_codes |
      | Q22            |
      | Q23            |
      | Q24            |
      | Q25            |
      | Q26            |
    When I run the validation process for <totalTurnoverValue> against the <deriveValue>
    Then the validation should return <result> if the "absolute difference between the values are" <operator> threshold value <thresholdValue>
    And the <validation> message should <isValidationExists> displayed for question code "Q20"

    Examples:
      | reference   | period | values    | totalTurnoverValue | deriveValue | result | operator     | thresholdValue | validation                                                | isValidationExists |
      | 49900791240 | 201903 | 1,1,1,1,0 | 10                 | 4           | true   | greater than | 5              | Total different to calculated total (allowing for margin) | be                 |
      | 49900791240 | 201903 | 1,2,3,2,1 | 3                  | 9           | true   | greater than | 5              | Total different to calculated total (allowing for margin) | be                 |
      | 49900791240 | 201903 | 1,1,1,1,1 | 10                 | 5           | false  | equal to     | 5              | Total different to calculated total (allowing for margin) | not be             |
      | 49900791240 | 201903 | 1,2,3,2,1 | 4                  | 9           | false  | equal to     | 5              | Total different to calculated total (allowing for margin) | not be             |
      | 49900791240 | 201903 | 1,1,1,1,1 | 9                  | 5           | false  | less than    | 5              | Total different to calculated total (allowing for margin) | not be             |
      | 49900791240 | 201903 | 1,2,3,2,1 | 6                  | 9           | false  | less than    | 5              | Total different to calculated total (allowing for margin) | not be             |
