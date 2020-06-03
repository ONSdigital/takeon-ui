Feature: RSI

  Background:
    Given As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: RSI LU-5033 - POPMRTZ rule A - Validation Check on form 5
    Given I search for the survey "0023" with <reference> for the period <previousPeriodValue>
    And  the current period sales value is <cpInternetSales>
    And has the internet sales value <ppInternetSales> out of total turnover value <ppTotalTurnover>
    When I search for the survey "0023" with <reference> for the period <currentPeriodValue>
    And I validate the current period details
    Then the validation should return <result> if the turnover ratio is <operator> threshold value <thresholdValue>

    Examples:
      | previousPeriodValue | currentPeriodValue | reference   | cpInternetSales | ppInternetSales | ppTotalTurnover | result | operator     | thresholdValue |
      | 201903              | 201904             | 49900534932 | 0               | 99              | 1000            | false  | less than    | 10%            |
      | 201903              | 201904             | 49900551526 | 0               | 100             | 1000            | false  | equal to     | 10%            |
      | 201903              | 201904             | 49900567891 | 0               | 101             | 1000            | true   | greater than | 10%            |
      | 201903              | 201904             | 49900572358 | 0               | 0               | 1000            | false  | less than    | 10%            |
      | 201903              | 201904             | 49900589234 | 0               | 0               | 0               | false  | less than    | 10%            |

  Scenario Outline: RSI LU-5033 - POPMRTZ rule A - Validation Check on form 6
    Given I search for the survey "0023" with <reference> for the period <previousPeriodValue>
    And  the current period sales value is <cpInternetSales>
    And has the internet sales value <ppInternetSales> out of total turnover value <ppTotalTurnover>
    When I search for the survey "0023" with <reference> for the period <currentPeriodValue>
    And I validate the current period details
    Then the validation should return <result> if the turnover ratio is <operator> threshold value <thresholdValue>

    Examples:
      | previousPeriodValue | currentPeriodValue | reference   | cpInternetSales | ppInternetSales | ppTotalTurnover | result | operator     | thresholdValue |
      | 201903              | 201904             | 49900613746 | 0               | 99              | 1000            | false  | less than    | 10%            |
      | 201903              | 201904             | 49900617217 | 0               | 100             | 1000            | false  | equal to     | 10%            |
      | 201903              | 201904             | 49900672013 | 0               | 101             | 1000            | true   | greater than | 10%            |
      | 201903              | 201904             | 49900694171 | 0               | 0               | 1000            | false  | less than    | 10%            |
      | 201903              | 201904             | 49900818161 | 0               | 0               | 0               | false  | less than    | 10%            |

  Scenario Outline: RSI LU-5033 - POPMRTZ rule A - Validation Check on form 7
    Given I search for the survey "0023" with <reference> for the period <previousPeriodValue>
    And  the current period sales value is <cpInternetSales>
    And has the internet sales value <ppInternetSales> out of total turnover value <ppTotalTurnover>
    When I search for the survey "0023" with <reference> for the period <currentPeriodValue>
    And I validate the current period details
    Then the validation should return <result> if the turnover ratio is <operator> threshold value <thresholdValue>

    Examples:
      | previousPeriodValue | currentPeriodValue | reference   | cpInternetSales | ppInternetSales | ppTotalTurnover | result | operator     | thresholdValue |
      | 201903              | 201904             | 49900748571 | 0               | 99              | 1000            | false  | less than    | 10%            |
      | 201903              | 201904             | 49900756292 | 0               | 100             | 1000            | false  | equal to     | 10%            |
      | 201903              | 201904             | 49900767172 | 0               | 101             | 1000            | true   | greater than | 10%            |
      | 201903              | 201904             | 49900791240 | 0               | 0               | 1000            | false  | less than    | 10%            |
      | 201903              | 201904             | 49900792013 | 0               | 0               | 0               | false  | less than    | 10%            |

