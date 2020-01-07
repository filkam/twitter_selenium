Feature: tweeting on twitter.com
As a logged user I want to tweet a message from my home page with various types of attachements and lengths.

  Scenario: Tweet a short message
    Given user is logged in as a default user
    When user clicks the tweet button
    And user inputs content into the text box
    And user clicks Tweet button
    Then submitted tweet is published


  Scenario: Tweet a message with picture attachment
    Given user is logged in as a default user
    When user clicks the tweet button
    And inputs content into the text box
    And attaches a picture
    And clicks Tweet button
    Then submitted tweet is published together with the picture


  Scenario: Tweet a message with a poll
    Given user is logged in as a default user
    When user clicks the tweet button
    And inputs content into the text box
    And adds a poll with content
    And clicks Tweet button
    Then submitted tweet is published and poll is visible

  Scenario: Tweet two messages consecutively
    Given user is logged in as a default user
    When user clicks the tweet button
    And inputs content into the text box
    And clicks the plus button
    And user inputs content into the text box
    And clicks Tweet all button
    Then all tweets are published

  Scenario: Tweet a message with a GIF
  Scenario: Tweet a message with emoji
  Scenario: Try to tweet a message that exceeds character limit
  Scenario: Try to tweet a message you already tweeted before
  Scenario: Input a message and discard a tweet


