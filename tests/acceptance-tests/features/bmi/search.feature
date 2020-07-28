Feature: Search function

  Background: Setting the correct url
    Given reference column is 1
    And period column is 2
    And survey column is 3
    And As a BMI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: Using an existing full reference entry
    Given I search for the <survey> with <reference> for the current period <period>
    Then <reference> and <period> and <survey> will be displayed
    Examples:
      | reference   | period | survey |
      | 49900012765 | 201906 | 066   |
      | 49900004791 | 201906 | 076   |
      | 49900138556 | 201905 | 073   |
      | 49900229065 | 201905 | 074   |

  Scenario Outline: Using a non-existing full reference entry
    Given I search for the survey with reference <reference>
    Then no table should appear
    Examples:
      | reference   |
      | 49900000999 |
      | 65900000103 |
      | 4998800105  |


  Scenario Outline: Using an existing Survey id
    Given I search for the <survey> with <reference> for the current period <period>
    Then <reference> and <period> and <survey> will be displayed
    Examples:
      | survey | reference   | period |
      | 066   | 49900000796 | 201903 |
      | 076   | 49900004791 | 201906 |

  Scenario Outline: Using an existing survey Id and reference
    Given I search for the <survey> with reference <reference>
    Then <reference> and <period> and <survey> will be displayed
    Examples:
      | survey | reference   | period |
      | 066   | 49900000796 | 201903 |
      | 076   | 49900004791 | 201906 |