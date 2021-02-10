Feature: RSI Survey - check the edited response values for date anomalies validation

  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: SPP-827 - check the edited response values for date anomalies validation on form 5
    Given I search for the survey "023" with "12000534932" for the current period "201903"
    And I have the contributor responses returned for <daysReturned> as compared to <actualDaysReturned>
    And the period start date as <periodStartDate> with period end date as <periodEndDate>
    When I edited the contributor response <cValues> on questions <questionCodes>
    And I trigger the validation process
    Then the edited values should change to <editedResponse> as per the <daysReturned>
    And the "validation" message should <isValidationExists> displayed for question code <questionCodes>
    Examples:
      | actualDaysReturned | daysReturned | periodStartDate | periodEndDate | questionCodes | cValues | editedResponse                        | isValidationExists |
      | 25                 | 25           | 20190304        | 20190328      | Q20,Q21       | 100,10  | 100.0,10.0                            | be                 |
      | 25                 | 21           | 20190304        | 20190324      | Q20,Q21       | 100,10  | 119.33333333333331,11.933333333333332 | be                 |
      | 25                 | 1            | 20190304        | 20190304      | Q20,Q21       | 100,10  | 3579.9999999999995,358.0              | be                 |
      | 25                 | 26           | 20190303        | 20190328      | Q20,Q21       | 100,10  | blank                                 | be                 |
      | 25                 | 26           | 20190304        | 20190329      | Q20,Q21       | 100,10  | blank                                 | be                 |

