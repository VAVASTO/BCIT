Feature: Test Sort Function
    Scenario: Abs Sort default
        When I sort data [4, -30, 100, -100, 123, 1, 0, -1, -4]
        Then I get result [123, 100, -100, -30, 4, -4, 1, -1, 0] 

    Scenario: Abs Sort one number
        When I sort data [4]
        Then I get result [4]

    Scenario: Abs Sort with lambda default
        When I lambda sort data [4, -30, 100, -100, 123, 1, 0, -1, -4]
        Then I lambda get result [123, 100, -100, -30, 4, -4, 1, -1, 0] 

    Scenario: Abs Sort with lambda one number
        When I lambda sort data [4]
        Then I lambda get result [4]