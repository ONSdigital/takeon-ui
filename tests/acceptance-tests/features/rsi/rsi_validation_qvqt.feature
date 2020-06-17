Feature: Test Survey - QvQT validation rule

  Background:
    Given As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: LU-6402 - current period value vs derived value greater than threshold value on forms 6 and 7
    Given I search for the survey "0023" with <reference> for the period <period>
    When I run the validation process for <totalTurnoverValue> against the <derivedQValue>
    Then the validation should return <result> if the "absolute difference between the values are" <operator> threshold value <thresholdValue>
    And the <validation> message should <isValidationExists> displayed for question code "Q6"

    Examples:
      | reference   | period | totalTurnoverValue | derivedQValue | result | operator     | thresholdValue | validation                                                | isValidationExists |
      | 49900694171 | 201903 | 1000               | 1006          | true   | greater than | 5              | Total different to calculated total (allowing for margin) | be                 |
      | 49900694171 | 201903 | 1000               | 994           | true   | greater than | 5              | Total different to calculated total (allowing for margin) | be                 |
      | 49900694171 | 201903 | 1000               | 1005          | false  | equal than   | 5              | Total different to calculated total (allowing for margin) | not be             |
      | 49900767172 | 201903 | 1000               | 995           | false  | equal than   | 5              | Total different to calculated total (allowing for margin) | not be             |
      | 49900767172 | 201903 | 1000               | 1004          | false  | less than    | 5              | Total different to calculated total (allowing for margin) | not be             |
      | 49900767172 | 201903 | 1000               | 996           | false  | less than    | 5              | Total different to calculated total (allowing for margin) | not be             |