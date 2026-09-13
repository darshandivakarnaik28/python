DESCRIPTION
The wide-mouth frog is particularly interested in the eating habits of other creatures.

He just can't stop asking the creatures he encounters what they like to eat. But, then he meets the alligator who just LOVES to eat wide-mouthed frogs!

When he meets the alligator, it then makes a tiny mouth.

Your goal in this kata is to create complete the mouth_size method this method takes one argument animal which corresponds to the animal encountered by the frog. If this one is an alligator (case-insensitive) return small otherwise return wide.

import codewars_test as test
from solution import mouth_size

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(mouth_size("toucan"),"wide")
        test.assert_equals(mouth_size("ant bear"),"wide")
        test.assert_equals(mouth_size("alligator"),"small")

@test.describe("Random Tests")
def random_tests():
    
    from random import randint, sample
    import re
    
    def mouth_size_sol(animal):
        return 'small' if re.match(animal, 'alligator', re.IGNORECASE) else 'wide'
    
    for i in range(40):
        animal = "".join([letter.upper() if randint(0,1) else letter for letter in sample(['alligator', 'alligator', 'alligator', 'alligator', 'alligator', 'alligator', 'ant bear', 'toucan', 'tiger', 'lion', 'giraffe', 'longer than an alli'], 1)[0]])
        @test.it(f'Should work for mouth_size("{animal}")!')
        def test_case():
            test.assert_equals(mouth_size(animal),mouth_size_sol(animal))