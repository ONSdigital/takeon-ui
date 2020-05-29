Feature: RSI

  Background:
    Given As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline : LU-6261 - POPMRTZ rule A - Validation Check
    Given the current period sales value is <cpInternetSales>
    And I search for the <survey> with <reference> for the previous period <previousPeriod>
    And has the "internet sales values" as <ppInternetSales>
    And has the "total turnover sales values" as <ppTotalTurnover>
    When I run period on period movement ratio validation on the current period
    Then the validation should return <result> if the <ppInternetSalesToTotalTurnoverRatio> is <operator> threshold value <thresholdValue>

    Examples:
      | survey | reference | cpInternetSales | ppInternetSales | ppTotalTurnover | ppInternetSalesToTotalTurnoverRatio | result | operator     | thresholdValue |
      | 999A   | 1234      | 0               | 99              | 1000            | 9.9%                                | false  | less than    | 10%            |
      | 999A   | 1234      | 0               | 100             | 1000            | 10%                                 | false  | equal to     | 10%            |
      | 999A   | 1234      | 0               | 101             | 1000            | 10.1%                               | true   | greater than | 10%            |
      | 999A   | 1234      | 0               | 0               | 1000            | 0%                                  | false  | less than    | 10%            |
      | 999A   | 1234      | 0               | 0               | 0               | 0%                                  | false  | less than    | 10%            |
