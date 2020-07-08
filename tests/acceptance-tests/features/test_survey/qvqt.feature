Feature: Test Survey - QvQT validation rule

  Background:
    Given As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: LU-6401 - current period value vs derived value greater than threshold value
    Given I search for the survey "999A" with <reference> for the current period <period>
    And I submit the commodity <values> for questions
      | question_codes |
      | Q1             |
      | Q2             |
    When I run the validation process against the <derivedValue>
    Then the validation should return <result> if the "absolute difference between the values are" <operator> threshold value <thresholdValue>
    And the <validation> message should <isValidationExists> displayed for question code "Q6"

    Examples:
      | reference   | period | values | derivedValue | result | operator     | thresholdValue | validation                                                | isValidationExists |
      | 12345678012 | 201712 | 7,1    | 6            | true   | greater than | 5              | Total different to calculated total (allowing for margin) | be                 |
      | 12345678012 | 201712 | 1,7    | -6           | true   | greater than | 5              | Total different to calculated total (allowing for margin) | be                 |
      | 12345678012 | 201712 | 6,1    | 5            | false  | equal to     | 5              | Total different to calculated total (allowing for margin) | not be             |
      | 12345678012 | 201712 | 1,6    | -5           | false  | equal to     | 5              | Total different to calculated total (allowing for margin) | not be             |
      | 12345678012 | 201712 | 5,1    | 4            | false  | less than    | 5              | Total different to calculated total (allowing for margin) | not be             |
      | 12345678012 | 201712 | 1,5    | -4           | false  | less than    | 5              | Total different to calculated total (allowing for margin) | not be             |
