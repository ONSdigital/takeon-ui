Feature: RSI

  Background:
    Given As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: LU-6261 - POPMRTZ rule A - Validation Check
    Given I search for the survey "999A" with <reference> for the period <previousPeriodValue>
    And  the current period sales value is <cpInternetSales>
    And has the internet sales value <ppInternetSales> out of total turnover value <ppTotalTurnover>
    When I search for the survey "999A" with <reference> for the period <currentPeriodValue>
    And I run the validation process
    Then the validation should return <result> if the turnover ratio is <operator> threshold value <thresholdValue>

    Examples:
      | previousPeriodValue | currentPeriodValue | reference   | cpInternetSales | ppInternetSales | ppTotalTurnover | result | operator     | thresholdValue |
      | 201712              | 201801             | 12345678011 | 0               | 99              | 1000            | false  | less than    | 10%            |
      | 201712              | 201801             | 12345678011 | 0               | 100             | 1000            | false  | equal to     | 10%            |
      | 201712              | 201801             | 12345678011 | 0               | 101             | 1000            | true   | greater than | 10%            |
      | 201712              | 201801             | 12345678011 | 0               | 0               | 1000            | false  | less than    | 10%            |
      | 201712              | 201801             | 12345678011 | 0               | 0               | 0               | false  | less than    | 10%            |
