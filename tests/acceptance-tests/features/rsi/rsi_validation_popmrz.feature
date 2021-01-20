Feature: RSI Survey - Validation PoPMRZ

  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a RSI user I set the search criteria options for the forms returned by the contributor

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
      | 201903              | 201904             | 12000534932 | 99              | 1000            | false  | less than    | 10%            | not be             |
      | 201903              | 201904             | 12000551526 | 100             | 1000            | false  | equal to     | 10%            | not be             |
      | 201903              | 201904             | 12000567891 | 101             | 1000            | true   | greater than | 10%            | be                 |
      | 201903              | 201904             | 12000572358 | 0               | 1000            | false  | less than    | 10%            | not be             |
      | 201903              | 201904             | 12000589234 | 0               | 0               | false  | equal to     | 10%            | not be             |

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
      | 201903              | 201904             | 12000613746 | 99              | 1000            | false  | less than    | 10%            | not be             |
      | 201903              | 201904             | 12000617217 | 100             | 1000            | false  | equal to     | 10%            | not be             |
      | 201903              | 201904             | 12000672013 | 101             | 1000            | true   | greater than | 10%            | be                 |
      | 201903              | 201904             | 12000694171 | 0               | 1000            | false  | less than    | 10%            | not be             |
      | 201903              | 201904             | 12000818161 | 0               | 0               | false  | equal to     | 10%            | not be             |

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
      | 201903              | 201904             | 12000748571 | 99              | 1000            | false  | less than    | 10%            | not be             |
      | 201903              | 201904             | 12000756292 | 100             | 1000            | false  | equal to     | 10%            | not be             |
      | 201903              | 201904             | 12000767172 | 101             | 1000            | true   | greater than | 10%            | be                 |
      | 201903              | 201904             | 12000791240 | 0               | 1000            | false  | less than    | 10%            | not be             |
      | 201903              | 201904             | 12000792013 | 0               | 0               | false  | equal to     | 10%            | not be             |
