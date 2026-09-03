Description
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.

Don't forget the space after the closing parentheses!

Test Cases
import codewars_test as test 
from solution import create_phone_number

@test.describe("Create Phone Number")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
        test.assert_equals(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
        test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
        test.assert_equals(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
        test.assert_equals(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")

    @test.it("Random tests")
    def _():
        
        from random import randint
        
        create_sol=lambda n: "(%s) %s-%s" %("".join(map(str, n[:3])), "".join(map(str, n[3:6])), "".join(map(str, n[6:])))

        for _ in range(40):
            n=[randint(0,9) for qu in range(10)]    
            expected = create_sol(n)
            test.assert_equals(create_phone_number(n),expected, f'Testing for {repr(n)}')