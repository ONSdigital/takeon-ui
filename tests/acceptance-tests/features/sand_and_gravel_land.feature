Feature: Sand And Gravel Land Survey

  Scenario Outline:  Sand and Gravel Land survey -- period on period movement for invalid values
    Given As a BMI user I search for the form returned by the contributor with <reference> number
    And I run the validation process on <questionCode> for the "previous period" <previousPeriod> with <previousPeriodValue>
    When I run the validation process on <questionCode> for the "current period" <currentPeriod> with <currentPeriodValue>
    Then the validation should return <result> if the absolute difference between the periods doesnt meet the <threshold> value
    And the form status should change to <formStatus>

    Examples:
      | reference   | currentPeriodValue | previousPeriodValue | result | threshold | formStatus   | questionCode | previousPeriod | currentPeriod |
      | 10000000005 | 30000              | 9999                | true   | 20000     | check needed | 601          | 201806         | 201809        |
