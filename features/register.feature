Feature: Register account scenario
  @Register18
  Scenario: Register with mandatory fields
    Given I should navigate to register page
    When I enter details into mandatory fields
         |first_name|last_name|telephone|password|
         |Madhu kumar|HM      |8296798325|Maddy@1234|
    And Click on continue button
    Then Account should get created

  @Register
  Scenario: Register with All fields
    Given I should navigate to register page
    When I enter details into All fields
         |first_name|last_name|telephone|password|
         |Madhu kumar|HM      |8296798325|Maddy@1234|
    And Click on continue button
    Then Account should get created

  @Register
  Scenario: Register with Duplicate email address
    Given I should navigate to register page
    When I enter details into All fields except email field
         |first_name|last_name|telephone|password|
         |Madhu kumar|HM      |8296798325|Maddy@1234|
    And I enter existing email into email field
    And Click on continue button
    Then proper warning message for already register mail should be displayed

  @Register
  Scenario: Register without providing any details
    Given I should navigate to register page
    When I dont enter anything into the fields
    And Click on continue button
    Then proper warning message for every mandatory field should be displayed
