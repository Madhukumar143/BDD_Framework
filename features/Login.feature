Feature: Login Feature

  @Login @smoke
  Scenario Outline: Login With Valid credentials
    Given I navigate to the login page
    When i enter user name as "<email>" and password as "<password>" into the fields
    And I click on Login button
    Then I should be successfully logged in
    Examples:
      |email|password|
      |madhukumarhm605@gmail.com|Madhu@1234|

  @Login @smoke
  Scenario: Login With Valid Email and Invalid password
    Given I navigate to the login page
    When i enter valid Email and invalid Password into the fields
    And I click on Login button
    Then I should get a proper warning message

  @Login @smoke
  Scenario: Login With Invalid Email and valid password
    Given I navigate to the login page
    When i enter Invalid Email and Valid Password into the fields
    And I click on Login button
    Then I should get a proper warning message
