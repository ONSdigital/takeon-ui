Feature: BMI Surveys(Blocks,Bricks,Sand Gravel Land and Sand Gravel Marine) - Override checkbox - Fixed Value(FV) Validation rule


  Background:
    Given As a BMI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline:  LU-7170 - Check Override functionality for Fixed Value Validation
    Given I search for the <survey> with <reference> for the current period <period>
    And I submit the "bmi survey stock material" <value> for question <question>
    And the "fv validation" message is displayed for the validation been triggered
    When I override the validation for the question <question>
    Then the validation message should change to <overrideMessage>
    Examples:
      | survey | reference   | period | value       | question | overrideMessage                               |
      | 073    | 49900138556 | 201906 | 99999999999 | Q101     | Override 'Value set to default, please check' |
      | 074    | 49900229065 | 201905 | 99999999999 | Q001     | Override 'Value set to default, please check' |
      | 066    | 49900012765 | 201903 | 99999999999 | Q601     | Override 'Value set to default, please check' |
      | 076    | 49900004791 | 201903 | 99999999999 | Q601     | Override 'Value set to default, please check' |
