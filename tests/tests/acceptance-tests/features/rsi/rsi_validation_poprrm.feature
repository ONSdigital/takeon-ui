Feature: RSI Survey - Validation PoPRRM

  Background:
    Given As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: RSI LU-6733 - PoPRRM Validation for RSI survey on form 5
    Given I search for the survey "0023" with <reference> for the previous period <previousPeriodValue>
    And has the internet sales value <ppInternetSales> out of total turnover value <ppTotalTurnover>
    When I search for the survey "0023" with <reference> for the current period <currentPeriodValue>
    And  has the internet sales value <cpInternetSales> out of total turnover value <cpTotalTurnover>
    And I validate the current period details for <factor> factor type
    Then the validation should return <result> if the "period on period ratio of ratios movement is" <operator> threshold value <thresholdValue>
    And the "The ratio of ratios between values has changed significantly since the last submission" message should <isValidationExists> displayed for question code "Q21"

    Examples:
      | previousPeriodValue | currentPeriodValue | reference   | ppInternetSales | ppTotalTurnover | cpInternetSales | cpTotalTurnover | factor         | result | operator     | thresholdValue | isValidationExists |
      | 201903              | 201904             | 49900589234 | 10              | 400             | 10              | 100             | increase       | true   | equal to     | 4              | be                 |
      | 201903              | 201904             | 49900589234 | 10              | 100             | 10              | 400             | decrease       | true   | equal to     | 4              | be                 |
      | 201903              | 201904             | 49900589234 | 10              | 400             | 11              | 100             | increase       | true   | greater than | 4              | be                 |
      | 201903              | 201904             | 49900589234 | 10              | 100             | 11              | 400             | decrease       | false  | less than    | 4              | not be             |
      | 201903              | 201904             | 49900589234 | 10              | 400             | 9               | 100             | increase       | false  | less than    | 4              | not be             |
      | 201903              | 201904             | 49900589234 | 10              | 100             | 9               | 400             | decrease       | true   | greater than | 4              | be                 |
      | 201903              | 201904             | 49900589234 | 0               | 0               | 0               | 0               | not-applicable | false  | all zeros    | 4              | not be             |
      | 201903              | 201904             | 49900589234 | blank           | blank           | blank           | blank           | not-applicable | false  | all blanks   | 4              | not be             |

  Scenario Outline: RSI LU-6733 - PoPRRM Validation for RSI survey on form 6
    Given I search for the survey "0023" with <reference> for the previous period <previousPeriodValue>
    And has the internet sales value <ppInternetSales> out of total turnover value <ppTotalTurnover>
    When I search for the survey "0023" with <reference> for the current period <currentPeriodValue>
    And  has the internet sales value <cpInternetSales> out of total turnover value <cpTotalTurnover>
    And I validate the current period details for <factor> factor type
    Then the validation should return <result> if the "period on period ratio of ratios movement is" <operator> threshold value <thresholdValue>
    And the "The ratio of ratios between values has changed significantly since the last submission" message should <isValidationExists> displayed for question code "Q21"

    Examples:
      | previousPeriodValue | currentPeriodValue | reference   | ppInternetSales | ppTotalTurnover | cpInternetSales | cpTotalTurnover | factor         | result | operator     | thresholdValue | isValidationExists |
      | 201903              | 201904             | 49900672013 | 10              | 400             | 10              | 100             | increase       | true   | equal to     | 4              | be                 |
      | 201903              | 201904             | 49900672013 | 10              | 100             | 10              | 400             | decrease       | true   | equal to     | 4              | be                 |
      | 201903              | 201904             | 49900672013 | 10              | 400             | 11              | 100             | increase       | true   | greater than | 4              | be                 |
      | 201903              | 201904             | 49900672013 | 10              | 100             | 11              | 400             | decrease       | false  | less than    | 4              | not be             |
      | 201903              | 201904             | 49900672013 | 10              | 400             | 9               | 100             | increase       | false  | less than    | 4              | not be             |
      | 201903              | 201904             | 49900672013 | 10              | 100             | 9               | 400             | decrease       | true   | greater than | 4              | be                 |
      | 201903              | 201904             | 49900672013 | 0               | 0               | 0               | 0               | not-applicable | false  | all zeros    | 4              | not be             |
      | 201903              | 201904             | 49900672013 | blank           | blank           | blank           | blank           | not-applicable | false  | all blanks   | 4              | not be             |

  Scenario Outline: RSI LU-6733 - PoPRRM Validation for RSI survey on form 7
    Given I search for the survey "0023" with <reference> for the previous period <previousPeriodValue>
    And has the internet sales value <ppInternetSales> out of total turnover value <ppTotalTurnover>
    When I search for the survey "0023" with <reference> for the current period <currentPeriodValue>
    And  has the internet sales value <cpInternetSales> out of total turnover value <cpTotalTurnover>
    And I validate the current period details for <factor> factor type
    Then the validation should return <result> if the "period on period ratio of ratios movement is" <operator> threshold value <thresholdValue>
    And the "The ratio of ratios between values has changed significantly since the last submission" message should <isValidationExists> displayed for question code "Q21"

    Examples:
      | previousPeriodValue | currentPeriodValue | reference   | ppInternetSales | ppTotalTurnover | cpInternetSales | cpTotalTurnover | factor         | result | operator     | thresholdValue | isValidationExists |
      | 201903              | 201904             | 49900748571 | 10              | 400             | 10              | 100             | increase       | true   | equal to     | 4              | be                 |
      | 201903              | 201904             | 49900748571 | 10              | 100             | 10              | 400             | decrease       | true   | equal to     | 4              | be                 |
      | 201903              | 201904             | 49900748571 | 10              | 400             | 11              | 100             | increase       | true   | greater than | 4              | be                 |
      | 201903              | 201904             | 49900748571 | 10              | 100             | 11              | 400             | decrease       | false  | less than    | 4              | not be             |
      | 201903              | 201904             | 49900748571 | 10              | 400             | 9               | 100             | increase       | false  | less than    | 4              | not be             |
      | 201903              | 201904             | 49900748571 | 10              | 100             | 9               | 400             | decrease       | true   | greater than | 4              | be                 |
      | 201903              | 201904             | 49900748571 | 0               | 0               | 0               | 0               | not-applicable | false  | all zeros    | 4              | not be             |
      | 201903              | 201904             | 49900748571 | blank           | blank           | blank           | blank           | not-applicable | false  | all blanks   | 4              | not be             |
