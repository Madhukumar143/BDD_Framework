Feature: Login Feature

  @login
  Scenario: Login With Valid credentials
    Given I navigate to the login page
    When i enter user name and password into the fields
    And I click on Login button
    Then I should be successfully logged in

  @Login
  Scenario: Login With Valid Email and Invalid password
    Given I navigate to the login page
    When i enter valid Email and invalid Password into the fields
    And I click on Login button
    Then I should get a proper warning message

  @Login
  Scenario: Login With Invalid Email and valid password
    Given I navigate to the login page
    When i enter Invalid Email and Valid Password into the fields
    And I click on Login button
    Then I should get a proper warning message
