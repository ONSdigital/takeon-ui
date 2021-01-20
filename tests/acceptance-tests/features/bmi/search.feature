Feature: Search function

  Background: Setting the correct url
    Given "test-user" exists with the password "test-Password123" and roles ["dev"]
    And "test-user" is logged in
    And reference column is 1
    And period column is 2
    And survey column is 3
    And As a BMI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: Using an existing full reference entry
    Given I search for the <survey> with <reference> for the current period <period>
    Then <reference> and <period> and <survey> will be displayed
    Examples:
      | reference   | period | survey |
      | 12000012765 | 201906 | 066   |
      | 12000004791 | 201906 | 076   |
      | 12000138556 | 201905 | 073   |
      | 12000229065 | 201905 | 074   |

  Scenario Outline: Using a non-existing full reference entry
    Given I search for the survey with reference <reference>
    Then no table should appear
    Examples:
      | reference   |
      | 12000000999 |
      | 65900000103 |
      | 1208800105  |

  @smoke
  Scenario Outline: Using an existing Survey id
    Given I search for the <survey> with <reference> for the current period <period>
    Then <reference> and <period> and <survey> will be displayed
    Examples:
      | survey | reference   | period |
      | 066   | 12000000796 | 201903 |
      | 076   | 12000004791 | 201906 |

  Scenario Outline: Using an existing survey Id and reference
    Given I search for the <survey> with reference <reference>
    Then <reference> and <period> and <survey> will be displayed
    Examples:
      | survey | reference   | period |
      | 066   | 12000000796 | 201903 |
      | 076   | 12000004791 | 201906 |