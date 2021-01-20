Feature: BMI Surveys(Blocks,Bricks,Sand Gravel Land and Sand Gravel Marine) - Override checkboxes - Question vs Derived Question (QvQ) Validation rule

  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a BMI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: LU-7170 - Check Override functionality for Question vs Question Validation BMI - Blocks survey
    Given I search for the survey "073" with <reference> for the current period <period>
    And I submit the "blocks opening stock dense aggregate" <values> for questions
      | question_codes |
      | Q101           |
      | Q102           |
      | Q103           |
    And I run the validation process for <blocksClosingStock> against the <derivedTotal>
      | closing_stock_question | derived_question |
      | Q104                   | Q9001            |
    When I override the validation for the question <question>
    Then the validation message should change to "qvq override message"
    Examples:
      | period | reference   | values | derivedTotal | blocksClosingStock | question |
      | 201905 | 12000138556 | 1,1,1  | 1            | 2                  | Q104     |


  Scenario Outline: LU-7170 - Check Override functionality for Question vs Question Validation - Bricks survey
    Given I search for the survey "074" with <reference> for the current period <period>
    And I submit the "blocks opening stock dense aggregate" <values> for questions
      | question_codes |
      | Q001           |
      | Q002           |
      | Q003           |
    And I run the validation process for <blocksClosingStock> against the <derivedTotal>
      | closing_stock_question | derived_question |
      | Q004                   | Q9204            |
    When I override the validation for the question <question>
    Then the validation message should change to "qvq override message"
    Examples:
      | period | reference   | values | derivedTotal | blocksClosingStock | question |
      | 201905 | 12000356828 | 1,1,1  | 1            | 2                  | Q004     |


  Scenario Outline: LU-7170 - Check Override functionality for Question vs Question Validation BMI - Sand Gravel Land Survey
    Given I search for the survey "066" with <reference> for the current period <period>
    And I submit the "sand and gravel land material stock" <values> for questions
      | question_codes |
      | Q601           |
      | Q602           |
      | Q603           |
      | Q604           |
      | Q605           |
      | Q606           |
      | Q607           |
    And I run the validation process for <SandAndGravelLandStock> against the <derivedTotal>
      | total_question | derived_question |
      | Q608           | Q9001            |
    When I override the validation for the question <question>
    Then the validation message should change to "qvq override message"
    Examples:
      | period | reference   | values        | question | derivedTotal | SandAndGravelLandStock |
      | 201906 | 12000000796 | 1,1,1,1,1,1,1 | Q608     | 7            | 10                     |


  Scenario Outline: LU-7170 - Check Override functionality for Question vs Question Validation BMI - Sand Gravel Marine Survey
    Given I search for the survey "076" with <reference> for the current period <period>
    And I submit the "sand and gravel marine material stock" <values> for questions
      | question_codes |
      | Q601           |
      | Q602           |
      | Q603           |
      | Q604           |
      | Q605           |
      | Q606           |
      | Q607           |
    And I run the validation process for <SandAndGravelMarineStock> against the <derivedTotal>
      | total_question | derived_question |
      | Q608           | Q9001            |
    When I override the validation for the question <question>
    Then the validation message should change to "qvq override message"
    Examples:
      | period | reference   | values        | question | derivedTotal | SandAndGravelMarineStock |
      | 201903 | 12000004791 | 1,1,1,1,1,1,1 | Q608     | 7            | 10                       |
