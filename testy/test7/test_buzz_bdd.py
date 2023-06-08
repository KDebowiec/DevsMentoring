from behave import given, when, then
from buzz import *

@given('a number is {number:d}')
def step_given_a_number(context, number):
    context.number = number

@when('I play the FizzBuzz game')
def step_when_i_play_fizz_buzz_game(context):
    context.result = fizz_buzz(context.number)

@then('the result should be "{expected_result}"')
def step_then_the_result_should_be(context, expected_result):
    assert context.result == expected_result


Feature: FizzBuzz
  As a player
  I want to play FizzBuzz game
  So that I can have fun

  Scenario: Number is divisible by 3 and 5
    Given a number is 15
    When I play the FizzBuzz game
    Then the result should be "FizzBuzz"

  Scenario: Number is divisible by 3
    Given a number is 9
    When I play the FizzBuzz game
    Then the result should be "fizz"

  Scenario: Number is divisible by 5
    Given a number is 10
    When I play the FizzBuzz game
    Then the result should be "buzz"

  Scenario: Number is not divisible by 3 or 5
    Given a number is 7
    When I play the FizzBuzz game
    Then the result should be the number itself