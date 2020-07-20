Feature: Bricks Survey - Period on Period Movement(PoPM) Validation rule

  Scenario Outline:  LU-7033 - Period on Period Movement Validation - Drawn from kiln during month - Commons
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the survey "0074" with <reference> for the previous period <previousPeriod>
    And I run the validation process on <questionCode> with <previousPeriodValue>
    When I search for the survey "0074" with <reference> for the current period <currentPeriod>
    And I run the validation process on <questionCode> with <currentPeriodValue>
    Then the validation should return <result> if the "absolute difference between the values are" <operator> threshold value <thresholdValue>
    And the "This has changed significantly since the last submission" message should <isValidationExists> displayed for question code "Q002"

    Examples:
      | reference   | currentPeriodValue | previousPeriodValue | result | thresholdValue | operator     | questionCode | previousPeriod | currentPeriod | isValidationExists |
      | 49900423293 | 2000000            | 999999              | true   | 1000000        | greater than | Q002         | 201905         | 201906        | be                 |
      | 49900423293 | 999999             | 2000000             | true   | 1000000        | greater than | Q002         | 201905         | 201906        | be                 |
      | 49900423293 | 2000000            | 1000000             | false  | 1000000        | equal to     | Q002         | 201905         | 201906        | not be             |
      | 49900423293 | 1000000            | 2000000             | false  | 1000000        | equal to     | Q002         | 201905         | 201906        | not be             |
      | 49900423293 | 2000000            | 1000001             | false  | 1000000        | less than    | Q002         | 201905         | 201906        | not be             |
      | 49900423293 | 1000001            | 2000000             | false  | 1000000        | less than    | Q002         | 201905         | 201906        | not be             |
      | 49900423293 | 0                  | 0                   | false  | 1000000        | equal to     | Q002         | 201905         | 201906        | not be             |
      | 49900423293 | blank              | blank               | false  | 1000000        | equal to     | Q002         | 201905         | 201906        | not be             |


  Scenario Outline:  LU-7033 - Period on Period Movement Validation - Drawn from kiln during month - Facings
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the survey "0074" with <reference> for the previous period <previousPeriod>
    And I run the validation process on <questionCode> with <previousPeriodValue>
    When I search for the survey "0074" with <reference> for the current period <currentPeriod>
    And I run the validation process on <questionCode> with <currentPeriodValue>
    Then the validation should return <result> if the "absolute difference between the values are" <operator> threshold value <thresholdValue>
    And the "This has changed significantly since the last submission" message should <isValidationExists> displayed for question code "Q012"

    Examples:
      | reference   | currentPeriodValue | previousPeriodValue | result | thresholdValue | operator     | questionCode | previousPeriod | currentPeriod | isValidationExists |
      | 49900423920 | 2000000            | 999999              | true   | 1000000        | greater than | Q012         | 201905         | 201906        | be                 |
      | 49900423920 | 999999             | 2000000             | true   | 1000000        | greater than | Q012         | 201905         | 201906        | be                 |
      | 49900423920 | 2000000            | 1000000             | false  | 1000000        | equal to     | Q012         | 201905         | 201906        | not be             |
      | 49900423920 | 1000000            | 2000000             | false  | 1000000        | equal to     | Q012         | 201905         | 201906        | not be             |
      | 49900423920 | 2000000            | 1000001             | false  | 1000000        | less than    | Q012         | 201905         | 201906        | not be             |
      | 49900423920 | 1000001            | 2000000             | false  | 1000000        | less than    | Q012         | 201905         | 201906        | not be             |
      | 49900423920 | 0                  | 0                   | false  | 1000000        | equal to     | Q012         | 201905         | 201906        | not be             |
      | 49900423920 | blank              | blank               | false  | 1000000        | equal to     | Q012         | 201905         | 201906        | not be             |


  Scenario Outline:  LU-7033 - Period on Period Movement Validation - Drawn from kiln during month - Engineering
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the survey "0074" with <reference> for the previous period <previousPeriod>
    And I run the validation process on <questionCode> with <previousPeriodValue>
    When I search for the survey "0074" with <reference> for the current period <currentPeriod>
    And I run the validation process on <questionCode> with <currentPeriodValue>
    Then the validation should return <result> if the "absolute difference between the values are" <operator> threshold value <thresholdValue>
    And the "This has changed significantly since the last submission" message should <isValidationExists> displayed for question code "Q022"

    Examples:
      | reference   | currentPeriodValue | previousPeriodValue | result | thresholdValue | operator     | questionCode | previousPeriod | currentPeriod | isValidationExists |
      | 49900449878 | 2000000            | 999999              | true   | 1000000        | greater than | Q022         | 201905         | 201906        | be                 |
      | 49900449878 | 999999             | 2000000             | true   | 1000000        | greater than | Q022         | 201905         | 201906        | be                 |
      | 49900449878 | 2000000            | 1000000             | false  | 1000000        | equal to     | Q022         | 201905         | 201906        | not be             |
      | 49900449878 | 1000000            | 2000000             | false  | 1000000        | equal to     | Q022         | 201905         | 201906        | not be             |
      | 49900449878 | 2000000            | 1000001             | false  | 1000000        | less than    | Q022         | 201905         | 201906        | not be             |
      | 49900449878 | 1000001            | 2000000             | false  | 1000000        | less than    | Q022         | 201905         | 201906        | not be             |
      | 49900449878 | 0                  | 0                   | false  | 1000000        | equal to     | Q022         | 201905         | 201906        | not be             |
      | 49900449878 | blank              | blank               | false  | 1000000        | equal to     | Q022         | 201905         | 201906        | not be             |


  Scenario Outline:  LU-7033 - Period on Period Movement Validation - Deliveries to customer during month - Commons
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the survey "0074" with <reference> for the previous period <previousPeriod>
    And I run the validation process on <questionCode> with <previousPeriodValue>
    When I search for the survey "0074" with <reference> for the current period <currentPeriod>
    And I run the validation process on <questionCode> with <currentPeriodValue>
    Then the validation should return <result> if the "absolute difference between the values are" <operator> threshold value <thresholdValue>
    And the "This has changed significantly since the last submission" message should <isValidationExists> displayed for question code "Q003"

    Examples:
      | reference   | currentPeriodValue | previousPeriodValue | result | thresholdValue | operator     | questionCode | previousPeriod | currentPeriod | isValidationExists |
      | 49900449878 | 2000000            | 999999              | true   | 1000000        | greater than | Q003         | 201905         | 201906        | be                 |
      | 49900449878 | 999999             | 2000000             | true   | 1000000        | greater than | Q003         | 201905         | 201906        | be                 |
      | 49900449878 | 2000000            | 1000000             | false  | 1000000        | equal to     | Q003         | 201905         | 201906        | not be             |
      | 49900449878 | 1000000            | 2000000             | false  | 1000000        | equal to     | Q003         | 201905         | 201906        | not be             |
      | 49900449878 | 2000000            | 1000001             | false  | 1000000        | less than    | Q003         | 201905         | 201906        | not be             |
      | 49900449878 | 1000001            | 2000000             | false  | 1000000        | less than    | Q003         | 201905         | 201906        | not be             |
      | 49900449878 | 0                  | 0                   | false  | 1000000        | equal to     | Q003         | 201905         | 201906        | not be             |
      | 49900449878 | blank              | blank               | false  | 1000000        | equal to     | Q003         | 201905         | 201906        | not be             |


  Scenario Outline:  LU-7033 - Period on Period Movement Validation - Deliveries to customer during month - Facings
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the survey "0074" with <reference> for the previous period <previousPeriod>
    And I run the validation process on <questionCode> with <previousPeriodValue>
    When I search for the survey "0074" with <reference> for the current period <currentPeriod>
    And I run the validation process on <questionCode> with <currentPeriodValue>
    Then the validation should return <result> if the "absolute difference between the values are" <operator> threshold value <thresholdValue>
    And the "This has changed significantly since the last submission" message should <isValidationExists> displayed for question code "Q013"

    Examples:
      | reference   | currentPeriodValue | previousPeriodValue | result | thresholdValue | operator     | questionCode | previousPeriod | currentPeriod | isValidationExists |
      | 49900449878 | 2000000            | 999999              | true   | 1000000        | greater than | Q013         | 201905         | 201906        | be                 |
      | 49900449878 | 999999             | 2000000             | true   | 1000000        | greater than | Q013         | 201905         | 201906        | be                 |
      | 49900449878 | 2000000            | 1000000             | false  | 1000000        | equal to     | Q013         | 201905         | 201906        | not be             |
      | 49900449878 | 1000000            | 2000000             | false  | 1000000        | equal to     | Q013         | 201905         | 201906        | not be             |
      | 49900449878 | 2000000            | 1000001             | false  | 1000000        | less than    | Q013         | 201905         | 201906        | not be             |
      | 49900449878 | 1000001            | 2000000             | false  | 1000000        | less than    | Q013         | 201905         | 201906        | not be             |
      | 49900449878 | 0                  | 0                   | false  | 1000000        | equal to     | Q013         | 201905         | 201906        | not be             |
      | 49900449878 | blank              | blank               | false  | 1000000        | equal to     | Q013         | 201905         | 201906        | not be             |


  Scenario Outline:  LU-7033 - Period on Period Movement Validation - Deliveries to customer during month - Engineering
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the survey "0074" with <reference> for the previous period <previousPeriod>
    And I run the validation process on <questionCode> with <previousPeriodValue>
    When I search for the survey "0074" with <reference> for the current period <currentPeriod>
    And I run the validation process on <questionCode> with <currentPeriodValue>
    Then the validation should return <result> if the "absolute difference between the values are" <operator> threshold value <thresholdValue>
    And the "This has changed significantly since the last submission" message should <isValidationExists> displayed for question code "Q023"

    Examples:
      | reference   | currentPeriodValue | previousPeriodValue | result | thresholdValue | operator     | questionCode | previousPeriod | currentPeriod | isValidationExists |
      | 49900449878 | 2000000            | 999999              | true   | 1000000        | greater than | Q023         | 201905         | 201906        | be                 |
      | 49900449878 | 999999             | 2000000             | true   | 1000000        | greater than | Q023         | 201905         | 201906        | be                 |
      | 49900449878 | 2000000            | 1000000             | false  | 1000000        | equal to     | Q023         | 201905         | 201906        | not be             |
      | 49900449878 | 1000000            | 2000000             | false  | 1000000        | equal to     | Q023         | 201905         | 201906        | not be             |
      | 49900449878 | 2000000            | 1000001             | false  | 1000000        | less than    | Q023         | 201905         | 201906        | not be             |
      | 49900449878 | 1000001            | 2000000             | false  | 1000000        | less than    | Q023         | 201905         | 201906        | not be             |
      | 49900449878 | 0                  | 0                   | false  | 1000000        | equal to     | Q023         | 201905         | 201906        | not be             |
      | 49900449878 | blank              | blank               | false  | 1000000        | equal to     | Q023         | 201905         | 201906        | not be             |
