Feature: RSI Validation Value Present SIC (VPSIC)

    Background:
        Given As a RSI user I set the search criteria options for the forms returned by the contributor

    Scenario Outline: LU-6829 - Value Present SIC(VPSIC) Validation for RSI Survey form 7
        Given I search for the survey "0023" with <reference> for the period <period>
        And has the sic code <SIC>
        When I submit the "SICValue" <SICValue> for question <question>
        And I trigger the validation process
        Then the <validation> message should <isValidationExists> displayed

        Examples:

            | period | reference   | SIC   | SICValue | question | validation                          | isValidationExists |
            | 201903 | 49900748571 | 43700 | blank    | Q13      | Check the response to this question | not be             |
            | 201903 | 49900756292 | 43700 | 0        | Q13      | Check the response to this question | not be             |
            | 201904 | 49900767172 | 43700 | 1        | Q13      | Check the response to this question | be                 |

