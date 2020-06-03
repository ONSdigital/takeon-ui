Feature: RSI

  Background:
    Given As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: RSI LU-5033 - CPBMI rule A - Validation Check on form 5
    Given I search for the survey "0023" with <reference> for the period <period>
    And has the internet sales value <ppInternetSales> out of total turnover value <ppTotalTurnover>
    When I submit the comment for the survey "0023" with <reference> for the period <currentPeriodValue>
    When I search for the survey "0023" with <reference> for the period <currentPeriodValue>
    And I run the validation process
    Then the validation should return <result> if the turnover ratio is <operator> threshold value <thresholdValue>

    Examples:
      | previousPeriodValue | currentPeriodValue | reference   | cpInternetSales | ppInternetSales | ppTotalTurnover | result | operator     | thresholdValue |
      | 201903              | 201904             | 49900534932 | 0               | 99              | 1000            | false  | less than    | 10%            |
      | 201903              | 201904             | 49900551526 | 0               | 100             | 1000            | false  | equal to     | 10%            |
      | 201903              | 201904             | 49900567891 | 0               | 101             | 1000            | true   | greater than | 10%            |
      | 201903              | 201904             | 49900572358 | 0               | 0               | 1000            | false  | less than    | 10%            |
      | 201903              | 201904             | 49900589234 | 0               | 0               | 0               | false  | less than    | 10%            |

