# Created by mary Barani
Feature: main page test cases

  Scenario:  The user can click on “Connect the company” on the left side of the main page
    Given Open the main page
    When Log in to the page with mary_barani2002@yahoo.com and TestC@reerist
    And Click on “Connect the company”
    And Switch the new tab
    Then Verify the book-presentation tab is open
