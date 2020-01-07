Feature: Logging to twitter.com
As a user I want to log in to twitter.com using different credentials.

  Scenario Outline: Log in with credentials
    Given non-logged user is on Twitter login page
    When user fills credentials "<email>" "<password>" in the form and submits
    Then user is logged in and can see the Home page
    Examples:
    | email | password |
    |       |          |
