Description:
Remove an exclamation mark from the end of a string. For a beginner kata, you can assume that the input data is always a string, no need to verify it.

Examples
"Hi!"     ---> "Hi"
"Hi!!!"   ---> "Hi!!"
"!Hi"     ---> "!Hi"
"!Hi!"    ---> "!Hi"
"Hi! Hi!" ---> "Hi! Hi"
"Hi"      ---> "Hi"

Test Cases
import codewars_test as test
from solution import remove

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():

        tests = [
            #[input, [expected]],
            ["Hi!", "Hi"],
            ["Hi!!!","Hi!!"],
            ["!Hi", "!Hi"],
            ["!Hi!", "!Hi"],
            ["Hi! Hi!", "Hi! Hi"],
            ["Hi", "Hi"],
            ["", ""],
        ]

        for inp, exp in tests:
            test.assert_equals(remove(inp), exp)
        
@test.describe("Random Tests")
def random_tests():

    from string import ascii_letters, punctuation
    from random import choice, randint
    from re import sub

    CHARS = ascii_letters 

    def create_word(length):
        return "".join(choice(CHARS) for _ in range(length))

    def add_excl(word):
        return "%s%s%s" % (randint(0, 4) * "!", word, randint(1, 5) * "!")

    def create_sentence(length):
        return " ".join(
            create_word(randint(1, 8))
            if randint(0, 30) % 3
            else add_excl(create_word(randint(0, 15)))
            for _ in range(length)
        )

    def reference(s):
        return sub("!$", "", s)

    for _ in range(100):
        s = create_sentence(randint(1, 20))+randint(1, 5) * "!"
        ans=reference(s)
        useran=remove(s)
        @test.it(f"Testing for: s = {repr(s)}")
        def basic_test_cases():
            test.assert_equals(useran, ans)