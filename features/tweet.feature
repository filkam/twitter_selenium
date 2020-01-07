Feature: tweeting on twitter.com
As a logged user I want to tweet a message from my home page

  Scenario: Tweet a message
    Given user is logged in
    When user clicks the tweet button
    And user inputs the content into the text box
    And user clicks Tweet button
    Then submitted tweet is published

