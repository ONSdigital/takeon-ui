Feature: RSI Survey - check Override Checkboxes validation

  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: LU-7171 - Check Override functionality for Value Present SIC (VPSIC) Validation for RSI Survey form 7
    Given I search for the survey "023" with <reference> for the current period <period> with SIC code <SIC>
    And I submit the "SICValue" <SICValue> for question <question>
    And I trigger the validation process
    When I override the validation for the question <question>
    Then the validation message should change to "vpsic override message"

    Examples:
      | period | reference   | SIC   | SICValue | question |
      | 201903 | 12000818161 | 47300 | 1        | Q21      |


  Scenario Outline: LU-7171 - Check Override functionality for Value is Blank (VB) Validation for Total Turnover
    Given I search for the survey "023" with <reference> for the current period <period>
    And I submit the "total turnover" <value> for question <question>
    And I trigger the validation process
    When I override the validation for the question <question>
    Then the validation message should change to "vb override message"

    Examples:
      | period | reference   | value | question |
      | 201903 | 12000534932 | blank | Q20      |
      | 201903 | 12000694171 | blank | Q20      |
      | 201904 | 12000756292 | blank | Q20      |


  Scenario Outline: LU-7171 - Check Override functionality for Value is Zero (VZ) Validation for Total Turnover
    Given I search for the survey "023" with <reference> for the current period <period>
    And I submit the "total turnover" <value> for question <question>
    And I trigger the validation process
    When I override the validation for the question <question>
    Then the validation message should change to "vz override message"

    Examples:
      | period | reference   | value | question |
      | 201903 | 12000534932 | 0     | Q20      |
      | 201903 | 12000694171 | 0     | Q20      |
      | 201904 | 12000756292 | 0     | Q20      |


  Scenario Outline: LU-7171 - Check Override functionality for Comment Present Validation RSI survey on form 5,6 and 7
    Given I search for the survey "023" with <reference> for the current period <period>
    And I submit the "comment" <comment> for question <question>
    And I trigger the validation process
    When I override the validation for the question <question>
    Then the validation message should change to "qvv override message"
    Examples:
      | period | reference   | comment | question |
      | 201903 | 12000534932 | 12345   | Q146     |
      | 201903 | 12000694171 | 12345   | Q146     |
      | 201904 | 12000756292 | 12345   | Q146     |


  Scenario Outline: LU-7171 - Check Override functionality for Previous Period Value Blank Validation on forms 5,6 and 7
    Given I search for the survey "023" with <reference> for the previous period <PPeriod>
    And has the internet sales value <ppInternetSales> out of total turnover value <ppTotalTurnover>
    And I search for the survey "023" with <reference> for the current period <CPeriod>
    And has the internet sales value <cpInternetSales> out of total turnover value <cpTotalTurnover>
    When I override the validation for the question <question>
    Then the validation message should change to <overrideMessage>

    Examples:
      | PPeriod | CPeriod | reference   | ppInternetSales | ppTotalTurnover | cpInternetSales | cpTotalTurnover | question | overrideMessage                      |
      | 201903  | 201904  | 12000534932 | blank           | blank           | 1               | 2               | Q20      | ppvb total turnover override message |
      | 201903  | 201904  | 12000534932 | blank           | blank           | 1               | 2               | Q21      | ppvb internet sales override message |


  Scenario Outline: LU-7171 - Check Override functionality for PoPRRM Validation for RSI survey on form 5,6 and 7
    Given I search for the survey "023" with <reference> for the previous period <PPeriodValue>
    And has the internet sales value <ppInternetSales> out of total turnover value <ppTotalTurnover>
    And I search for the survey "023" with <reference> for the current period <CPeriodValue>
    And  has the internet sales value <cpInternetSales> out of total turnover value <cpTotalTurnover>
    When I override the validation for the question <question>
    Then the validation message should change to "poprrm override message"

    Examples:
      | PPeriodValue | CPeriodValue | reference   | ppInternetSales | ppTotalTurnover | cpInternetSales | cpTotalTurnover | question |
      | 201903       | 201904       | 12000589234 | 10              | 400             | 10              | 100             | Q21      |
      | 201903       | 201904       | 12000672013 | 10              | 400             | 10              | 100             | Q21      |
      | 201903       | 201904       | 12000748571 | 10              | 400             | 10              | 100             | Q21      |


  Scenario Outline: LU-7171 - Check Override functionality for PoPMRZ Validation RSI survey on form 5
    Given I search for the survey "023" with <reference> for the previous period <PPeriod>
    And the current period sales value is "0"
    And has the internet sales value <ppInternetSales> out of total turnover value <ppTotalTurnover>
    When I search for the survey "023" with <reference> for the current period <CPeriod>
    And I validate popmrz current period details
    Then the override checkbox should not be displayed for <question>

    Examples:
      | PPeriod | CPeriod | reference   | ppInternetSales | ppTotalTurnover | question |
      | 201903  | 201904  | 12000551526 | 101             | 1000            | Q21      |
      | 201903  | 201904  | 12000672013 | 101             | 1000            | Q21      |
      | 201903  | 201904  | 12000767172 | 101             | 1000            | Q21      |
