Feature: Blocks Survey - Override checkbox - Fixed Value(FV) Validation rule


  Background:
    Given As a BMI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline:  LU-7170 - Check Override functionality for Fixed Value Validation - Blocks Survey
    Given I search for the survey "073" with <reference> for the current period <period>
    And I submit the "brick stock material" <value> for question <question>
    And the "fv validation" message is displayed for the validation been triggered
    When I override the validation for the question <question>
    Then the validation message should change to <overrideMessage>
    Examples:
      | reference   | period | value       | question | overrideMessage                               |
      | 49900138556 | 201906 | 99999999999 | Q101     | Override 'Value set to default, please check' |
