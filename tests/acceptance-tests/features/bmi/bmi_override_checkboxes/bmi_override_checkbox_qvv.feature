Feature: BMI Surveys(Blocks,Bricks,Sand Gravel Land and Sand Gravel Marine) - Override checkbox - Fixed Value(FV) Validation rule


  Background:
    Given As a BMI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: LU-6531 - Check Override functionality for Comment Present Validation
    Given I search for the <survey> with <reference> for the current period <period>
    And I submit the "comment" <comment> for question <question>
    And I trigger the validation process
    When I override the validation for the question <question>
    Then the validation message should change to "qvv override message"
    Examples:
      | survey | period | reference   | comment | question |
      | 073    | 201905 | 49900228645 | 2       | Q145     |
      | 074    | 201905 | 49900229065 | 2       | Q145     |
      | 066    | 201903 | 49900000796 | 2       | Q146     |
      | 076    | 201903 | 49900004791 | 2       | Q146     |
