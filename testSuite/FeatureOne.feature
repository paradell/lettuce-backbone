Feature: This is a main description of this concrete feature
  As a Tester
  I want to set som test scenarios
  In order to test Feature One automatically

  Scenario: a user can retrireve the README file of a GitHub repositoru
    Given a user not registered in GitHub
    When the user tries to get the repositories of paradell user
    Then the api response is a 200 code
    And the response includes a list with all user repositories
