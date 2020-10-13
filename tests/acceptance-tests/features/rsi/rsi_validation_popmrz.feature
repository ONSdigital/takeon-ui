Feature: RSI Survey - Validation PoPMRZ

  Background:
    Given As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: RSI LU-5033 - PoPMRZ rule A - Validation Check on form 5
    Given I search for the survey "023" with <reference> for the previous period <previousPeriodValue>
    And the current period sales value is "0"
    And has the internet sales value <ppInternetSales> out of total turnover value <ppTotalTurnover>
    When I search for the survey "023" with <reference> for the current period <currentPeriodValue>
    And I validate popmrz current period details
    Then the validation should return <result> if the "turnover ratio is" <operator> threshold value <thresholdValue>
    And the "popmrz validation" message should <isValidationExists> displayed for question code "Q21"

    Examples:
      | previousPeriodValue | currentPeriodValue | reference   | ppInternetSales | ppTotalTurnover | result | operator     | thresholdValue | isValidationExists |
      | 201903              | 201904             | 49900534932 | 99              | 1000            | false  | less than    | 10%            | not be             |
      | 201903              | 201904             | 49900551526 | 100             | 1000            | false  | equal to     | 10%            | not be             |
      | 201903              | 201904             | 49900567891 | 101             | 1000            | true   | greater than | 10%            | be                 |
      | 201903              | 201904             | 49900572358 | 0               | 1000            | false  | less than    | 10%            | not be             |
      | 201903              | 201904             | 49900589234 | 0               | 0               | false  | equal to     | 10%            | not be             |

  Scenario Outline: RSI LU-5033 - PoPMRZ rule A - Validation Check on form 6
    Given I search for the survey "023" with <reference> for the previous period <previousPeriodValue>
    And the current period sales value is "0"
    And has the internet sales value <ppInternetSales> out of total turnover value <ppTotalTurnover>
    When I search for the survey "023" with <reference> for the current period <currentPeriodValue>
    And I validate popmrz current period details
    Then the validation should return <result> if the "turnover ratio is" <operator> threshold value <thresholdValue>
    And the "popmrz validation" message should <isValidationExists> displayed for question code "Q21"

    Examples:
      | previousPeriodValue | currentPeriodValue | reference   | ppInternetSales | ppTotalTurnover | result | operator     | thresholdValue | isValidationExists |
      | 201903              | 201904             | 49900613746 | 99              | 1000            | false  | less than    | 10%            | not be             |
      | 201903              | 201904             | 49900617217 | 100             | 1000            | false  | equal to     | 10%            | not be             |
      | 201903              | 201904             | 49900672013 | 101             | 1000            | true   | greater than | 10%            | be                 |
      | 201903              | 201904             | 49900694171 | 0               | 1000            | false  | less than    | 10%            | not be             |
      | 201903              | 201904             | 49900818161 | 0               | 0               | false  | equal to     | 10%            | not be             |

  Scenario Outline: RSI LU-5033 - PoPMRZ rule A - Validation Check on form 7
    Given I search for the survey "023" with <reference> for the previous period <previousPeriodValue>
    And  the current period sales value is "0"
    And has the internet sales value <ppInternetSales> out of total turnover value <ppTotalTurnover>
    When I search for the survey "023" with <reference> for the current period <currentPeriodValue>
    And I validate popmrz current period details
    Then the validation should return <result> if the "turnover ratio is" <operator> threshold value <thresholdValue>
    And the "popmrz validation" message should <isValidationExists> displayed for question code "Q21"

    Examples:
      | previousPeriodValue | currentPeriodValue | reference   | ppInternetSales | ppTotalTurnover | result | operator     | thresholdValue | isValidationExists |
      | 201903              | 201904             | 49900748571 | 99              | 1000            | false  | less than    | 10%            | not be             |
      | 201903              | 201904             | 49900756292 | 100             | 1000            | false  | equal to     | 10%            | not be             |
      | 201903              | 201904             | 49900767172 | 101             | 1000            | true   | greater than | 10%            | be                 |
      | 201903              | 201904             | 49900791240 | 0               | 1000            | false  | less than    | 10%            | not be             |
      | 201903              | 201904             | 49900792013 | 0               | 0               | false  | equal to     | 10%            | not be             |
