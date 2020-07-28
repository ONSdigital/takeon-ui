Feature: Sand and Gravel Land Survey - Question vs Derived Question (QvQ) Validation rule

  Background:
    Given As a BMI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: LU-7034 - Question vs Question Validation BMI survey on form 1
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
    When I run the validation process for <SandAndGravelLandStock> against the <derivedTotal>
      | total_question | derived_question |
      | Q608           | Q9001            |
    Then the validation should return <result> if the "values are not equal"
    And the <validation> message should <isValidationExists> displayed for question code "Q608"
    Examples:
      | period | reference   | validation                                   | values                                    | isValidationExists | result | derivedTotal | SandAndGravelLandStock |
      | 201906 | 49900000796 | This total is not equal to the derived total | 1,1,1,1,1,1,1                             | be                 | true   | 7            | 10                     |
      | 201906 | 49900000796 | This total is not equal to the derived total | 1,1,0,-1,-3,-5,0                            | be                 | true   | -7           | 7                      |
      | 201906 | 49900000796 | This total is not equal to the derived total | 2,1,1,2,3,1,1                             | not be             | false  | 11           | 11                     |
      | 201906 | 49900000796 | This total is not equal to the derived total | 0,0,0,0,0,0,0                             | not be             | false  | 0            | 0                      |
      | 201906 | 49900000796 | This total is not equal to the derived total | blank,blank,blank,blank,blank,blank,blank | not be             | false  | blank        | blank                  |
