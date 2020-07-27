Feature: RSI Survey - Validation Previous Period Value Blank (PPVB)

  Background:
    Given As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: RSI LU-6757 - Previous Period Value Blank Validation on forms 5
    Given I search for the survey "023" with <reference> for the previous period <PPeriod>
    And has the internet sales value <ppInternetSales> out of total turnover value <ppTotalTurnover>
    When I search for the survey "023" with <reference> for the current period <CPeriod>
    And has the internet sales value <cpInternetSales> out of total turnover value <cpTotalTurnover>
    Then the <validation> message should <isValidationExists> displayed for question codes
      | question_codes |
      | Q20            |
      | Q21            |
    Examples:
      | PPeriod | CPeriod | reference   | ppInternetSales | ppTotalTurnover | cpInternetSales | cpTotalTurnover | validation                                  | isValidationExists |
      | 201903  | 201904  | 49900534932 | blank           | blank           | 1               | 2               | This value was blank in the previous period | be                 |
      | 201903  | 201904  | 49900534932 | 0               | 0               | 1               | 2               | This value was blank in the previous period | not be             |
      | 201903  | 201904  | 49900534932 | 1               | 1               | 1               | 2               | This value was blank in the previous period | not be             |


  Scenario Outline: RSI LU-6757 - Previous Period Value Blank Validation on forms 6
    Given I search for the survey "023" with <reference> for the previous period <PPeriod>
    And has the internet sales value <ppInternetSales> out of total turnover value <ppTotalTurnover>
    When I search for the survey "023" with <reference> for the current period <CPeriod>
    And has the internet sales value <cpInternetSales> out of total turnover value <cpTotalTurnover>
    Then the <validation> message should <isValidationExists> displayed for question codes
      | question_codes |
      | Q20            |
      | Q21            |
    Examples:
      | PPeriod | CPeriod | reference   | ppInternetSales | ppTotalTurnover | cpInternetSales | cpTotalTurnover | validation                                  | isValidationExists |
      | 201903  | 201904  | 49900613746 | blank           | blank           | 1               | 2               | This value was blank in the previous period | be                 |
      | 201903  | 201904  | 49900613746 | 0               | 0               | 1               | 2               | This value was blank in the previous period | not be             |
      | 201903  | 201904  | 49900613746 | 1               | 1               | 1               | 2               | This value was blank in the previous period | not be             |


  Scenario Outline: RSI LU-6757 - Previous Period Value Blank Validation on forms 7
    Given I search for the survey "023" with <reference> for the previous period <PPeriod>
    And has the internet sales value <ppInternetSales> out of total turnover value <ppTotalTurnover>
    When I search for the survey "023" with <reference> for the current period <CPeriod>
    And has the internet sales value <cpInternetSales> out of total turnover value <cpTotalTurnover>
    Then the <validation> message should <isValidationExists> displayed for question codes
      | question_codes |
      | Q20            |
      | Q21            |
    Examples:
      | PPeriod | CPeriod | reference   | ppInternetSales | ppTotalTurnover | cpInternetSales | cpTotalTurnover | validation                                  | isValidationExists |
      | 201903  | 201904  | 49900767172 | blank           | blank           | 1               | 2               | This value was blank in the previous period | be                 |
      | 201903  | 201904  | 49900767172 | 0               | 0               | 1               | 2               | This value was blank in the previous period | not be             |
      | 201903  | 201904  | 49900767172 | 1               | 1               | 1               | 2               | This value was blank in the previous period | not be             |


  Scenario Outline: RSI LU-6757 - Previous Period Value Blank Validation if no previous period exists for forms 5, 6 and 7
    Given I search for the survey "023" with <reference> for the current period <CPeriod>
    And has the internet sales value <cpInternetSales> out of total turnover value <cpTotalTurnover>
    Then the <validation> message should <isValidationExists> displayed for question codes
      | question_codes |
      | Q20            |
      | Q21            |
    Examples:
      | CPeriod | reference   | cpInternetSales | cpTotalTurnover | validation                                  | isValidationExists |
      | 201903  | 49900534932 | 1               | 1               | This value was blank in the previous period | be                 |
      | 201903  | 49900613746 | 1               | 1               | This value was blank in the previous period | be                 |
      | 201903  | 49900767172 | 1               | 1               | This value was blank in the previous period | be                 |
