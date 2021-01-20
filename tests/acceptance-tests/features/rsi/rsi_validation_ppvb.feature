Feature: RSI Survey - Validation Previous Period Value Blank (PPVB)

  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: RSI LU-6757 - Previous Period Value Blank Validation on forms 5,6 and 7
    Given I search for the survey "023" with <reference> for the previous period <PPeriod>
    And has the internet sales value <ppInternetSales> out of total turnover value <ppTotalTurnover>
    When I search for the survey "023" with <reference> for the current period <CPeriod>
    And has the internet sales value <cpInternetSales> out of total turnover value <cpTotalTurnover>
    Then the "ppvb total turnover validation" message should <isValidationExists> displayed for question code "Q20"

    Examples:
      | PPeriod | CPeriod | reference   | ppInternetSales | ppTotalTurnover | cpInternetSales | cpTotalTurnover | isValidationExists |
      | 201903  | 201904  | 12000534932 | blank           | blank           | 1               | 2               | be                 |
      | 201903  | 201904  | 12000613746 | blank           | blank           | 1               | 2               | be                 |
      | 201903  | 201904  | 12000767172 | blank           | blank           | 1               | 2               | be                 |
      | 201903  | 201904  | 12000534932 | 0               | 0               | 1               | 2               | not be             |
      | 201903  | 201904  | 12000534932 | 1               | 1               | 1               | 2               | not be             |
      | 201903  | 201904  | 12000613746 | 0               | 0               | 1               | 2               | not be             |
      | 201903  | 201904  | 12000613746 | 1               | 1               | 1               | 2               | not be             |
      | 201903  | 201904  | 12000767172 | 0               | 0               | 1               | 2               | not be             |
      | 201903  | 201904  | 12000767172 | 1               | 1               | 1               | 2               | not be             |


  Scenario Outline: RSI LU-6757 - Previous Period Value Blank Validation on forms 5,6 and 7
    Given I search for the survey "023" with <reference> for the previous period <PPeriod>
    And has the internet sales value <ppInternetSales> out of total turnover value <ppTotalTurnover>
    When I search for the survey "023" with <reference> for the current period <CPeriod>
    And has the internet sales value <cpInternetSales> out of total turnover value <cpTotalTurnover>
    Then the "ppvb internet sales validation" message should <isValidationExists> displayed for question code "Q21"

    Examples:
      | PPeriod | CPeriod | reference   | ppInternetSales | ppTotalTurnover | cpInternetSales | cpTotalTurnover | isValidationExists |
      | 201903  | 201904  | 12000534932 | blank           | blank           | 1               | 2               | be                 |
      | 201903  | 201904  | 12000613746 | blank           | blank           | 1               | 2               | be                 |
      | 201903  | 201904  | 12000767172 | blank           | blank           | 1               | 2               | be                 |
      | 201903  | 201904  | 12000534932 | 0               | 0               | 1               | 2               | not be             |
      | 201903  | 201904  | 12000534932 | 1               | 1               | 1               | 2               | not be             |
      | 201903  | 201904  | 12000613746 | 0               | 0               | 1               | 2               | not be             |
      | 201903  | 201904  | 12000613746 | 1               | 1               | 1               | 2               | not be             |
      | 201903  | 201904  | 12000767172 | 0               | 0               | 1               | 2               | not be             |
      | 201903  | 201904  | 12000767172 | 1               | 1               | 1               | 2               | not be             |


  Scenario Outline: RSI LU-6757 - Previous Period Value Blank Validation if no previous period exists for forms 5, 6 and 7
    Given I search for the survey "023" with <reference> for the current period <CPeriod>
    And has the internet sales value <cpInternetSales> out of total turnover value <cpTotalTurnover>
    Then the "ppvb total turnover validation" message should <isValidationExists> displayed for question code "Q20"

    Examples:
      | CPeriod | reference   | cpInternetSales | cpTotalTurnover | isValidationExists |
      | 201903  | 12000534932 | 1               | 1               | be                 |
      | 201903  | 12000613746 | 1               | 1               | be                 |
      | 201903  | 12000767172 | 1               | 1               | be                 |


  Scenario Outline: RSI LU-6757 - Previous Period Value Blank Validation if no previous period exists for forms 5, 6 and 7
    Given I search for the survey "023" with <reference> for the current period <CPeriod>
    And has the internet sales value <cpInternetSales> out of total turnover value <cpTotalTurnover>
    Then the "ppvb internet sales validation" message should <isValidationExists> displayed for question code "Q21"

    Examples:
      | CPeriod | reference   | cpInternetSales | cpTotalTurnover | isValidationExists |
      | 201903  | 12000534932 | 1               | 1               | be                 |
      | 201903  | 12000613746 | 1               | 1               | be                 |
      | 201903  | 12000767172 | 1               | 1               | be                 |
