Feature: SubscriptionPage
  Scenario: User can open SubscriptionPage
    Given the user is on the login page
    When the user logs in with valid credentials
    Then the Subscription & payments page should be visible
