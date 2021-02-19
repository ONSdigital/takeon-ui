Feature: RSI Survey - check the edited response values for date anomalies validation

  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: SPP-827 - check the adjusted response values for date anomalies validation on form 5
    Given I search for the survey "023" with "12000534932" for the current period "201903"
    And I have the contributor responses returned for <daysReturned> as compared to <actualDaysReturned>
    And the period start date set as <periodStartDate> with period end date as <periodEndDate>
    When I edited the contributor response <cValues> on questions <questionCodes>
    And I trigger the validation process
    Then the adjusted response values <datesRange> should be <adjustedResponse> compared to <cValues>
    And the "validation" message should <isValidationExists> displayed for question codes <questionCodes>
    Examples:
      | actualDaysReturned | daysReturned | datesRange           | periodStartDate | periodEndDate | questionCodes | cValues | adjustedResponse    | isValidationExists |
      | 25                 | 25           | exact date range     | 20190304        | 20190328      | Q20,Q21       | 100,101 | same,same           | be                 |
      | 25                 | 21           | within date range    | 20190304        | 20190324      | Q20,Q21       | 100,101 | increased,increased | be                 |
      | 25                 | 1            | within date range    | 20190304        | 20190304      | Q20,Q21       | 100,101 | increased,increased | be                 |
      | 25                 | 26           | outside date range   | 20190303        | 20190328      | Q20,Q21       | 100,101 | blank,blank         | be                 |
      | 25                 | 26           | outside date range   | 20190304        | 20190329      | Q20,Q21       | 100,101 | blank,blank         | be                 |
      | 25                 | 25           | different date range | 20190404        | 20190428      | Q20,Q21       | 100,101 | blank,blank         | be                 |
      | 25                 | 25           | missing date range   | blank           | blank         | Q20,Q21       | 100,101 | same,same           | be                 |
