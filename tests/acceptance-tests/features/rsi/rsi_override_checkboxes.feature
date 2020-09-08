Feature: RSI Survey - Override Checkboxes - Validation Value Present SIC (VPSIC)

  Background:
    Given As a RSI user I set the search criteria options for the forms returned by the contributor

  Scenario Outline: LU-7171 - Check Override functionality for Value Present SIC (VPSIC) Validation for RSI Survey form 7
    Given I search for the survey "023" with <reference> for the current period <period> with SIC code <SIC>
    And I submit the "SICValue" <SICValue> for question <question>
    And I trigger the validation process
    When I override the validation for the question <question>
    Then the validation message should change to <overrideMessage>

    Examples:
      | period | reference   | SIC   | SICValue | question | overrideMessage                                                             |
      | 201903 | 49900818161 | 47300 | 1        | Q21      | Override 'SIC is petrol and internet sales(Q21) value is greater than zero' |


  Scenario Outline: LU-7171 - Check Override functionality for Value is Blank (VB) Validation for RSI Survey form 5,6 and 7
    Given I search for the survey "023" with <reference> for the current period <period>
    And I submit the "total turnover" <value> for question <question>
    And I trigger the validation process
    When I override the validation for the question <question>
    Then the validation message should change to <overrideMessage>

    Examples:
      | period | reference   | value | question | overrideMessage                         |
      | 201903 | 49900534932 | blank | Q20      | Override 'Total turnover(Q20) is blank' |
      | 201903 | 49900694171 | blank | Q20      | Override 'Total turnover(Q20) is blank' |
      | 201904 | 49900756292 | blank | Q20      | Override 'Total turnover(Q20) is blank' |


  Scenario Outline: LU-7171 - Check Override functionality for Value is Zero (VZ) Validation for RSI Survey form 5,6 and 7
    Given I search for the survey "023" with <reference> for the current period <period>
    And I submit the "total turnover" <value> for question <question>
    And I trigger the validation process
    When I override the validation for the question <question>
    Then the validation message should change to <overrideMessage>

    Examples:
      | period | reference   | value | question | overrideMessage                        |
      | 201903 | 49900534932 | 0     | Q20      | Override 'Total turnover(Q20) is zero' |
      | 201903 | 49900694171 | 0     | Q20      | Override 'Total turnover(Q20) is zero' |
      | 201904 | 49900756292 | 0     | Q20      | Override 'Total turnover(Q20) is zero' |


  Scenario Outline: LU-7171 - Check Override functionality for Comment Present Validation RSI survey on form 5,6 and 7
    Given I search for the survey "023" with <reference> for the current period <period>
    And I submit the "comment" <comment> for question <question>
    And I trigger the validation process
    When I override the validation for the question <question>
    Then the validation message should change to <overrideMessage>
    Examples:
      | period | reference   | comment | question | overrideMessage                         |
      | 201903 | 49900534932 | 12345   | Q146     | Override 'Respondent entered a comment' |
      | 201903 | 49900694171 | 12345   | Q146     | Override 'Respondent entered a comment' |
      | 201904 | 49900756292 | 12345   | Q146     | Override 'Respondent entered a comment' |
