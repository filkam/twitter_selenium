Feature: Logging to twitter.com
As a user I want to log in to twitter.com

  Scenario: Log in with valid credentials
    Given user is on Twitter login page
    When user fills credentials in the form and submits
    Then user is logged in and can see the Home page

