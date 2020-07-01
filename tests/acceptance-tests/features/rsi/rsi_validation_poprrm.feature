Feature: RSI Survey - Validation PoPRRM

  Background:
    Given As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: RSI LU-6733 - PoPRRM Validation for RSI survey on form 5
    Given I search for the survey "0023" with <reference> for the period <previousPeriodValue>
    And has the previous internet sales value <ppInternetSales> out of total turnover value <ppTotalTurnover>
    When I search for the survey "0023" with <reference> for the period <currentPeriodValue>
    And  has the current internet sales value <cpInternetSales> out of total turnover value <cpTotalTurnover>
    And I validate the current period details for <factor> factor type
    Then the validation should return <result> if the "period on period ratio of ratios movement is" <operator> threshold value <thresholdValue>

    Examples:
      | previousPeriodValue | currentPeriodValue | reference   | cpInternetSales | cpTotalTurnover | ppInternetSales | ppTotalTurnover | factor         | result | operator     | thresholdValue |
      | 201712              | 201801             | 12345678011 | 10              | 100             | 10              | 400             | increase       | true   | equal to     | 4              |
      | 201712              | 201801             | 12345678011 | 10              | 400             | 10              | 100             | decrease       | true   | equal to     | 4              |
      | 201712              | 201801             | 12345678011 | 11              | 100             | 10              | 400             | increase       | true   | greater than | 4              |
      | 201712              | 201801             | 12345678011 | 11              | 400             | 10              | 100             | decrease       | false  | less than    | 4              |
      | 201712              | 201801             | 12345678011 | 9               | 100             | 10              | 400             | increase       | false  | less than    | 4              |
      | 201712              | 201801             | 12345678011 | 9               | 400             | 10              | 100             | decrease       | true   | greater than | 4              |
      | 201712              | 201801             | 12345678011 | 0               | 0               | 0               | 0               | not-applicable | false  | all zeros    | 4              |
      | 201712              | 201801             | 12345678011 | blank           | blank           | blank           | blank           | not-applicable | false  | all blanks   | 4              |
