Feature: BMI Surveys(Bricks) - Override checkbox - Invalid Value(IV) Validation rule


  Background:
    Given As a BMI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline:  LU-7170 - Check Override functionality for Invalid Value Validation
    Given I search for the <survey> with <reference> for the current period <period>
    And I submit the "brick type material" <value> for question <question>
    And I trigger the validation process
    When I override the validation for the question <question>
    Then the validation message should change to <overrideMessage>
    Examples:
      | survey | reference   | period | value | question | overrideMessage                                                                                |
      | 074    | 49900229065 | 201905 | 1     | Q8000    | Override 'This is not a valid brick type. It should be 2 (clay), 3 (concrete) or 4 (sandlime)' |
