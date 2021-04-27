Feature: RSI Survey - check the date adjusted response values for date anomalies
  No of contributor's returned period days in for Short period parameter(S flag) is 27
  and for Long period parameter(L flag) is 35


  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: SPP-1711 - check the adjusted responses on form 5
    Given I search for the survey "023" with <reference> for the current period <period>
    And the period start date set as <actualStartDate> with period end date as <actualEndDate>
    When I submit the "contributor response values" <cValues> for questions
      | question_codes |
      | Q20            |
      | Q21            |
    And I trigger the validation process
    Then check the adjusted response values for <datesRange> should be <adjustedResponse> with status as <status>
    Examples:
      | reference   | period | datesRange                                | actualStartDate | actualEndDate | cValues     | adjustedResponse | status       |
      | 12000534932 | 201812 | 24 days short period date range           | 20181204        | 20181227      | 100,101     | decreased        | check needed |
      | 12000534932 | 201812 | 1 day short period date range             | 20181204        | 20181204      | 100,101     | increased        | check needed |
      | 12000534932 | 201812 | outside date range                        | 20190304        | 20190328      | 100,101     | blank            | form saved   |
      | 12000534932 | 201812 | start date greater than end date          | 20181228        | 20181204      | 100,101     | blank            | form saved   |
      | 12000534932 | 201812 | date range with blank variables           | 20181204  `     | 20181228      | blank,blank | blank            | form saved   |
      | 12000534932 | 201812 | defaults to expected for blank start date | blank           | 20181220      | 100,101     | decreased        | check needed |
      | 12000534932 | 201812 | defaults to expected for blank end date   | 20190320        | blank         | 100,101     | decreased        | check needed |
      | 12000534932 | 201812 | blank date range                          | blank           | blank         | 200,202     | decreased        | check needed |

  Scenario Outline: SPP-1670 - check the adjusted responses on form 6
    Given I search for the survey "023" with <reference> for the current period <period>
    And the period start date set as <actualStartDate> with period end date as <actualEndDate>
    When I submit the "contributor response values" <values> for questions
      | question_codes |
      | Q20            |
      | Q21            |
      | Q22            |
      | Q23            |
      | Q24            |
      | Q25            |
      | Q26            |
    And I trigger the validation process
    Then check the adjusted response values for <datesRange> should be <adjustedResponse> with status as <status>
    And  check no adjusted response displayed for question code "Q7034"
    Examples:
      | reference   | period | values                                    | datesRange                                | actualStartDate | actualEndDate | adjustedResponse | status       |
      | 12000694171 | 201904 | 100,101,5,4,3,2,1                         | 24 days short period date range           | 20190404        | 20190427      | decreased        | check needed |
      | 12000694171 | 201904 | 100,101,5,4,3,2,1                         | 1 day short period date range             | 20190404        | 20190404      | increased        | check needed |
      | 12000694171 | 201904 | 100,101,5,4,3,2,1                         | defaults to expected for blank start date | blank           | 20190420      | decreased        | check needed |
      | 12000694171 | 201904 | 100,101,5,4,3,2,1                         | defaults to expected for blank end date   | 20190320        | blank         | decreased        | check needed |
      | 12000694171 | 201904 | 100,101,5,4,3,2,1                         | blank date range                          | blank           | blank         | decreased        | check needed |
      | 12000694171 | 201904 | 100,101,5,4,3,2,1                         | outside date range                        | 20190704        | 20190728      | blank            | form saved   |
      | 12000694171 | 201904 | 100,101,5,4,3,2,1                         | start date greater than end date          | 20190428        | 20190404      | blank            | form saved   |
      | 12000694171 | 201904 | blank,blank,blank,blank,blank,blank,blank | date range with blank variables           | 20190404        | 20190428      | blank            | form saved   |

  Scenario Outline: SPP-1670 - check the adjusted responses on form 7
    Given I search for the survey "023" with <reference> for the current period <period>
    And the period start date set as <actualStartDate> with period end date as <actualEndDate>
    When I submit the "contributor response values" <values> for questions
      | question_codes |
      | Q20            |
      | Q21            |
      | Q22            |
      | Q23            |
      | Q24            |
      | Q25            |
      | Q26            |
      | Q27            |
    And I trigger the validation process
    Then check the adjusted response values for <datesRange> should be <adjustedResponse> with status as <status>
    And  check no adjusted response displayed for question code "Q7034"
    Examples:
      | reference   | period | values                                           | datesRange                                | actualStartDate | actualEndDate | adjustedResponse | status       |
      | 12000818161 | 201903 | 100,101,6,5,4,3,2,1                              | 24 days short period date range           | 20190304        | 20190327      | decreased        | check needed |
      | 12000818161 | 201903 | 100,101,6,5,4,3,2,1                              | 1 day short period date range             | 20190304        | 20190304      | increased        | check needed |
      | 12000818161 | 201903 | 100,101,6,5,4,3,2,1                              | defaults to expected for blank start date | blank           | 20190320      | decreased        | check needed |
      | 12000818161 | 201903 | 100,101,6,5,4,3,2,1                              | defaults to expected for blank end date   | 20190320        | blank         | decreased        | check needed |
      | 12000818161 | 201903 | 100,101,6,5,4,3,2,1                              | blank date range                          | blank           | blank         | decreased        | check needed |
      | 12000818161 | 201903 | 100,101,6,5,4,3,2,1                              | outside date range                        | 20190704        | 20190728      | blank            | form saved   |
      | 12000818161 | 201903 | 100,101,6,5,4,3,2,1                              | start date greater than end date          | 20190327        | 20190304      | blank            | form saved   |
      | 12000818161 | 201903 | blank,blank,blank,blank,blank,blank,blank, blank | date range with blank variables           | 20190304        | 20190327      | blank            | form saved   |
