Feature: Bricks Survey - Invalid Value(IV) Validation rule


  Scenario Outline:  LU-7306 - Invalid Value Validation - Brick type (2 - clay, 3 - concrete or 4 - sandlime)
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And As a BMI user I set the search criteria options for the forms returned by the contributor
    And I search for the survey "074" with <reference> for the current period <period>
    When I submit the "brick type" <brickTypeValue> for question <question>
    And I trigger the validation process
    Then the "iv validation" message should <isValidationExists> displayed
    Examples:
      | reference   | period | brickTypeValue | question | isValidationExists |
      | 12000229065 | 201905 | 2              | Q8000    | not be             |
      | 12000229065 | 201905 | 3              | Q8000    | not be             |
      | 12000229065 | 201905 | 4              | Q8000    | not be             |
      | 12000229065 | 201905 | 0              | Q8000    | be                 |
      | 12000229065 | 201905 | 1              | Q8000    | be                 |
      | 12000229065 | 201905 | blank          | Q8000    | be                 |

