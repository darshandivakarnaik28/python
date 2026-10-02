Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

Note: The function accepts an integer and returns an integer.

Happy Coding!


Test cases
# New tests for 3.8+
import codewars_test as test
from solution import square_digits

@test.describe("Fixed tests: ")
def fixed_tests():
    
    cases = [(3212, 9414), (2112, 4114), (0,0)]
    
    for input, expected in cases:
        @test.it(f"testing for square_digits({input})")
        def basic_test_cases():
            test.assert_equals(square_digits(input), expected)
            
@test.describe("Random Tests: ")
def random_tests():
    
    from random import randint
    
    def square_digits_test(number):
    	new_number = ""
    	for digit in str(number):
    		digit = int(digit) ** 2
    		new_number += str(digit)
    	return int(new_number)
           
    for item in range(1, 101):
        randomtest = randint(1, 10000000)
        @test.it(f"testing for square_digits({randomtest})")
        def test_case():
            test.assert_equals(square_digits(randomtest), square_digits_test(randomtest))