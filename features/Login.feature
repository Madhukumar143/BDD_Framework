Feature: Login Feature

  @login1
  Scenario Outline: Login With Valid credentials
    Given I navigate to the login page
    When i enter user name as "<email>" and password as "<password>" into the fields
    And I click on Login button
    Then I should be successfully logged in
    Examples:
    |email                        |password|
    |madhukumarhm605@gmail.com    |Madhu@1234|
    |madhukumarhm123.com@gmail.com|Madhu@1234|
    |madhukar@gmail.com           |Madhu@1234|

  @Login
  Scenario: Login With Valid Email and Invalid password
    Given I navigate to the login page
    When i enter valid Email as "madhukumarhm605@gmail.com" and invalid Password as "Madhu@1324" into the fields
    And I click on Login button
    Then I should get a proper warning message

  @Login
  Scenario: Login With Invalid Email and valid password
    Given I navigate to the login page
    When i enter Invalid Email and Valid Password as "Madhu@1234" into the fields
    And I click on Login button
    Then I should get a proper warning message
