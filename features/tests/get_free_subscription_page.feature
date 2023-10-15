# Created by Gheethvijay at 10/14/23
Feature: Test to verify Get a free subscription button functionality & see the right number of UI elements

    Scenario Outline: The user clicks on Get a free subscription button and sees the right number of UI elements
        Given Open the login page
        When login to the page
        Then Click on Get a free subscription
        Then Switch to the new tab
        Then Verify there are <n> steps to connect your company
        Then Verify Subscription plans button is clickable
        Examples:
        |n|
       |4|
