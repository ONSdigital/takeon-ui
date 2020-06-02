Feature: Sand And Gravel Land Survey

  Scenario Outline:  Sand and Gravel Land survey -- period on period movement for invalid values
    Given As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the <survey> with <reference> for the period <previousPeriod>
    And I run the validation process on <questionCode> for previous period with <previousPeriodValue>
    When I search for the <survey> with <reference> for the period <currentPeriod>
    And I run the validation process on <questionCode> for current period with <currentPeriodValue>
    Then the validation should return <result> if the absolute difference between the periods doesnt meet the <thresholdValue>
    And the form status should change to <formStatus>

    Examples:
      | survey | reference   | currentPeriodValue | previousPeriodValue | result | thresholdValue | formStatus   | questionCode | previousPeriod | currentPeriod |
      | 0066   | 49900008900 | 30000              | 9999                | true   | 20000          | check needed | 601          | 201903         | 201906        |
