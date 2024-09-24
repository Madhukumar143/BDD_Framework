Feature: Search Feature

  @Search
  Scenario: Search for a valid product
    Given I got navigated to home page
    When I enter valid product say "HP" into search box field
    And I click on search button
    Then valid product should be displayed in the search results

  @Search
  Scenario: Search for an Invalid product
    Given I got navigated to home page
    When I enter Invalid product say "honda" into search box field
    And I click on search button
    Then proper error message should be displayed in the search results page

  @Search
  Scenario: without providing any product details
    Given I got navigated to home page
    When I dont enter any product into search box field
    And I click on search button
    Then proper error message should be displayed in the search results page