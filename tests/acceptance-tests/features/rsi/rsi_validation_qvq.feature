Feature: RSI Survey - Question vs Question Validation rule

  Background:
    Given As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: LU-6831 - Comment Present Validation RSI survey on form 5
    Given I search for the survey "0023" with <reference> for the period <period>
    When I submit the "total turnover" <TotalTurnover> for question <turnoverQuestion>
    And I submit the "internet sales" <InternetSales> for question <internetSalesQuestion>
    And I trigger the validation process
    Then the <validation> message should <isValidationExists> displayed
    Examples:
      | period | reference   | validation                                               | InternetSales | TotalTurnover | isValidationExists | turnoverQuestion | internetSalesQuestion |
      | 201903 | 49900551526 | This is greater than the question we compare it to       | 100           | 99            | be                 | Q20              | Q21                   |
      | 201903 | 49900551526 | This is greater than the question we compare it to       | 99            | 100           | not be             | Q20              | Q21                   |
      | 201903 | 49900551526 | This is greater than the question we compare it to       | 999999        | 100           | be                 | Q20              | Q21                   |

  Scenario Outline: LU-6831 - Comment Present Validation RSI survey on form 6
    Given I search for the survey "0023" with <reference> for the period <period>
    When I submit the "total turnover" <TotalTurnover> for question <turnoverQuestion>
    And I submit the "internet sales" <InternetSales> for question <internetSalesQuestion>
    And I trigger the validation process
    Then the <validation> message should <isValidationExists> displayed
    Examples:
      | period | reference   | validation                                               | InternetSales | TotalTurnover | isValidationExists | turnoverQuestion | internetSalesQuestion |
      | 201903 | 49900617217 | This is greater than the question we compare it to       | 100           | 99            | be                 | Q20              | Q21                   |
      | 201903 | 49900617217 | This is greater than the question we compare it to       | 99            | 100           | not be             | Q20              | Q21                   |
      | 201903 | 49900617217 | This is greater than the question we compare it to       | 999999        | 100           | be                 | Q20              | Q21                   |

  Scenario Outline: LU-6831 - Comment Present Validation RSI survey on form 7
    Given I search for the survey "0023" with <reference> for the period <period>
    When I submit the "total turnover" <TotalTurnover> for question <turnoverQuestion>
    And I submit the "internet sales" <InternetSales> for question <internetSalesQuestion>
    And I trigger the validation process
    Then the <validation> message should <isValidationExists> displayed
    Examples:
      | period | reference   | validation                                               | InternetSales | TotalTurnover | isValidationExists | turnoverQuestion | internetSalesQuestion |
      | 201904 | 49900756292 | This is greater than the question we compare it to       | 100           | 99            | be                 | Q20              | Q21                   |
      | 201904 | 49900756292 | This is greater than the question we compare it to       | 99            | 100           | not be             | Q20              | Q21                   |
      | 201904 | 49900756292 | This is greater than the question we compare it to       | 999999        | 100           | be                 | Q20              | Q21                   |
