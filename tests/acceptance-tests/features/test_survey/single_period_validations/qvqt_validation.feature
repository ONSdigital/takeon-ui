Feature: Test Survey - Question vs Question Threshold(QvQT) validation rule

  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a Business Survey user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: SP-100 - Question vs Question Threshold(QvQT) Validation on test survey
    Given I search for the survey "999A" with <reference> for the current period <period>
    And I submit the "values" <values> for questions
      | question_codes |
      | Q13            |
      | Q14            |
      | Q15            |

    When I run the validation process for <primaryQuestion> against the <derivedValue>
    Then the validation should return <result> if the "absolute difference between the values are" <operator> threshold value <thresholdValue>
    And the "qvqt validation" message should <isValidationExists> displayed for question code "Q11"

    Examples:
      | reference   | period | values | primaryQuestion | derivedValue | result | operator     | thresholdValue | isValidationExists |
      | 12345678036 | 201712 | 7,2,1  | 4               | 10           | true   | greater than | 5              | be                 |
      | 12345678036 | 201712 | 7,2,1  | 16              | 10           | true   | greater than | 5              | be                 |
      | 12345678036 | 201712 | 7,2,1  | 5               | 10           | false  | equal to     | 5              | not be             |
      | 12345678036 | 201712 | 7,2,1  | 15              | 10           | false  | equal to     | 5              | not be             |
      | 12345678036 | 201712 | 7,2,1  | 6               | 10           | false  | less than    | 5              | not be             |
      | 12345678036 | 201712 | 7,2,1  | 14              | 10           | false  | less than    | 5              | not be             |
