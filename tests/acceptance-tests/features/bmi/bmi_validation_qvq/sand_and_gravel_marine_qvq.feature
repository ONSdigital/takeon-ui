Feature: Sand and Gravel Marine Survey - Question vs Derived Question (QvQ) Validation rule

  Background:
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a BMI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: LU-7034 - Question vs Question Validation BMI survey on form 2
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
    When I run the validation process for <SandAndGravelMarineStock> against the <derivedTotal>
      | total_question | derived_question |
      | Q608           | Q9001            |
    Then the validation should return <result> if the "values are not equal"
    And the "qvq validation" message should <isValidationExists> displayed for question code "Q608"
    Examples:
      | period | reference   | values                                    | isValidationExists | result | derivedTotal | SandAndGravelMarineStock |
      | 201903 | 49900004791 | 1,1,1,1,1,1,1                             | be                 | true   | 7            | 10                       |
      | 201903 | 49900004791 | 1,1,0,-1,-3,-5,0                          | be                 | true   | -7           | 7                        |
      | 201903 | 49900004791 | 2,1,1,2,3,1,1                             | not be             | false  | 11           | 11                       |
      | 201903 | 49900004791 | 0,0,0,0,0,0,0                             | not be             | false  | 0            | 0                        |
      | 201903 | 49900004791 | blank,blank,blank,blank,blank,blank,blank | not be             | false  | blank        | blank                    |
