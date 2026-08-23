Description:
You get a new job working for Eggman Movers. Your first task is to write a method that will allow the admin staff to enter a person’s name and return what that person's role is in the company.

You will be given an array of object literals holding the current employees of the company. You code must find the employee with the matching firstName and lastName and then return the role for that employee or if no employee is not found it should return "Does not work here!"

The array is preloaded and can be referenced using the variable employees ($employees in Ruby). It uses the following structure.

employees = [ {'first_name': "Dipper", 'last_name': "Pines", 'role': "Boss"}, ...... ]
There are no duplicate names in the array and the name passed in will be a single string with a space between the first and last name i.e. Jane Doe or just a name.

Test Cases:
import codewars_test as test
from solution import find_employees_role
from copy import deepcopy

# We have to duplicate the list for employees here to prevent user solution from modifying it before tests can run
employees = [
  {"first_name": "Ollie", "last_name": "Hepburn", "role": "Boss"},
  {"first_name": "Morty", "last_name": "Smith", "role": "Truck Driver"},
  {"first_name": "Peter", "last_name": "Ross", "role": "Warehouse Manager"},
  {"first_name": "Cal", "last_name": "Neil", "role": "Sales Assistant"},
  {"first_name": "Jesse", "last_name": "Saunders", "role": "Admin"},
  {"first_name": "Anna", "last_name": "Jones", "role": "Sales Assistant"},
  {"first_name": "Carmel", "last_name": "Hamm", "role": "Admin"},
  {"first_name": "Tori", "last_name": "Sparks", "role": "Sales Manager"},
  {"first_name": "Peter", "last_name": "Jones", "role": "Warehouse Picker"},
  {"first_name": "Mort", "last_name": "Smith", "role": "Warehouse Picker"},
  {"first_name": "Anna", "last_name": "Bell", "role": "Admin"},
  {"first_name": "Jewel", "last_name": "Bell", "role": "Receptionist"},
  {"first_name": "Colin", "last_name": "Brown", "role": "Trainee"}
]

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(find_employees_role("Dipper Pines"), "Does not work here!")
        test.assert_equals(find_employees_role("Morty Smith"), "Truck Driver")
        test.assert_equals(find_employees_role("Anna Bell"), "Admin")
        test.assert_equals(find_employees_role("Anna"), "Does not work here!", "Should be able to take a single name as input")
        test.assert_equals(find_employees_role("Bell Anna"), "Does not work here!", "Should differentiate surname and name")
        test.assert_not_equals(find_employees_role("Anna Bell"), "Sales Assistant")
        test.assert_not_equals(find_employees_role("Ollie Hepburn"), "Warehouse Manager")
        test.assert_not_equals(find_employees_role("Morty Smith"), "Warehouse Picker") 
        test.assert_equals(find_employees_role("Jewel Bell"), "Receptionist")
        test.assert_equals(find_employees_role("Bell Jewel"), "Does not work here!", "Should differentiate surname and name")
        
@test.describe("Random Tests")
def random_tests():
    from random import choice, uniform, randint
    from string import ascii_lowercase as al, ascii_uppercase as au
    
    sol = lambda name: ((lambda name: [x for x in employees if x["first_name"]==name[0] and x["last_name"]==name[1]])\
                                      ((name+" pippi").split(" ")) or [{"role": "Does not work here!"}])[0]["role"]
    
    for _ in range(100):
        first = [x['first_name'] for x in employees]
        last = [x['last_name'] for x in employees]
        n = [i+' '+j for i,j in zip(first, last)]
        m = uniform(0, 1)
        c = ''
        if m>0.5:
            c = choice(n)
        else:
            x = ''.join(choice(au+al) for _ in range(randint(1, 10)))
            y = ''.join(choice(au+al) for _ in range(randint(1, 10)))
            c = choice([choice(first)+' '+choice(last), x+' '+y])
        @test.it(f"Testing for find_employees_role({repr(c)})")
        def test_case():
            solution = sol(c)
            user = find_employees_role(c)
            test.assert_equals(user, solution, "It should work for random inputs too")