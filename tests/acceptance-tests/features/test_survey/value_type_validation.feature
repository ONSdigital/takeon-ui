Feature: Test Survey - Value is (Blank,Zero,Negative,Positive,Invalid) Validation rules

  Background:
    Given As a Business Survey user I set the search criteria options for the forms returned by the contributor


  Scenario Outline: SPP-100 - Value is Blank(VB) Validation on test survey
    Given I search for the survey "999A" with <reference> for the current period <period>
    When I submit the "value" <value> for question <question>
    And I trigger the validation process
    Then the "vb validation" message should <isValidationExists> displayed

    Examples:
      | period | reference   | value | question | isValidationExists |
      | 201712 | 12345678036 | blank | Q2       | be                 |
      | 201712 | 12345678036 | 1     | Q2       | not be             |

  Scenario Outline: SPP-100 - Value is Zero(VZ) Validation on test survey
    Given I search for the survey "999A" with <reference> for the current period <period>
    When I submit the "value" <value> for question <question>
    And I trigger the validation process
    Then the "vz validation" message should <isValidationExists> displayed

    Examples:
      | period | reference   | value | question | isValidationExists |
      | 201712 | 12345678036 | 0     | Q3       | be                 |
      | 201712 | 12345678036 | 1     | Q3       | not be             |
      | 201712 | 12345678036 | blank | Q3       | not be             |

  Scenario Outline: SPP-100 - Value is Negative(VN) Validation on test survey
    Given I search for the survey "999A" with <reference> for the current period <period>
    When I submit the "value" <value> for question <question>
    And I trigger the validation process
    Then the "vn validation" message should <isValidationExists> displayed

    Examples:
      | period | reference   | value | question | isValidationExists |
      | 201712 | 12345678036 | -1    | Q5       | be                 |
      | 201712 | 12345678036 | 1     | Q5       | not be             |
      | 201712 | 12345678036 | blank | Q5       | not be             |

  Scenario Outline: SPP-100 - Value is Present(VP) Validation on test survey
    Given I search for the survey "999A" with <reference> for the current period <period>
    When I submit the "value" <value> for question <question>
    And I trigger the validation process
    Then the "vp validation" message should <isValidationExists> displayed

    Examples:
      | period | reference   | value | question | isValidationExists |
      | 201712 | 12345678036 | 0     | Q1       | be                 |
      | 201712 | 12345678036 | 1     | Q1       | be                 |
      | 201712 | 12345678036 | blank | Q1       | not be             |

  Scenario Outline: SPP-100 - Value is Invalid(VI) Validation on test survey
    Given I search for the survey "999A" with <reference> for the current period <period>
    When I submit the "value" <value> for question <question>
    And I trigger the validation process
    Then the "vi validation" message should <isValidationExists> displayed

    Examples:
      | period | reference   | value | question | isValidationExists |
      | 201712 | 12345678036 | 2     | Q6       | not be             |
      | 201712 | 12345678036 | 3     | Q6       | not be             |
      | 201712 | 12345678036 | 4     | Q6       | not be             |
      | 201712 | 12345678036 | 0     | Q6       | be                 |
      | 201712 | 12345678036 | 1     | Q6       | be                 |
      | 201712 | 12345678036 | blank | Q6       | be                 |