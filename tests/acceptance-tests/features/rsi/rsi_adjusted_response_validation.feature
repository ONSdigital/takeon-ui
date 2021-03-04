Feature: RSI Survey - check the date adjusted response values for date anomalies
  No of contributor's returned period days in for Short period parameter(S flag) is 27
  and for Long period parameter(L flag) is 35


  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: SPP-1711 - check the adjusted response values for date anomalies validation on form 5
    Given I search for the survey "023" with <reference> for the current period <period>
    And the period start date set as <actualStartDate> with period end date as <actualEndDate>
    When I submit the "contributor response values" <cValues> for questions
      | question_codes |
      | Q20            |
      | Q21            |
    And I trigger the validation process
    Then check the adjusted response values for <datesRange> should be <adjustedResponse> as expected response
    Examples:
      | reference   | period | datesRange                      | actualStartDate | actualEndDate | cValues | adjustedResponse |
      | 12000534932 | 201903 | 25 days short period date range | 20190304        | 20190328      | 100,101 | same             |
      | 12000534932 | 201903 | 24 days short period date range | 20190304        | 20190327      | 100,101 | increased        |
      | 12000534932 | 201903 | 1 day short period date range   | 20190304        | 20190304      | 100,101 | increased        |

  Scenario Outline: SPP-1711 - check the adjusted response return blank values for date anomalies validation on form 5
    Given I search for the survey "023" with <reference> for the current period <period>
    And the period start date set as <actualStartDate> with period end date as <actualEndDate>
    When I submit the "contributor response values" <cValues> for questions
      | question_codes |
      | Q20            |
      | Q21            |
    And I trigger the validation process
    Then check the adjusted response values for <datesRange> should be <adjustedResponse> as expected response
    Examples:
      | reference   | period | datesRange                                | actualStartDate | actualEndDate | cValues     | adjustedResponse |
      | 12000534932 | 201903 | outside date range                        | 20190404        | 20190428      | 100,101     | blank            |
      | 12000534932 | 201903 | start date greater than end date          | 20190328        | 20190304      | 100,101     | blank            |
      | 12000534932 | 201903 | date range with blank variables           | 20190304        | 20190328      | blank,blank | blank            |
      | 12000534932 | 201903 | defaults to expected for blank start date | blank           | 20190428      | 100,101     | same             |
      | 12000534932 | 201903 | defaults to expected for blank end date   | 20190320        | blank         | 100,101     | increased        |
      | 12000534932 | 201903 | blank date range                          | blank           | blank         | 100,101     | same             |



