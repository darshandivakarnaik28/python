Implement a Python class ComplexNumber to demonstrate operator overloading for adding two complex numbers.

Class Name: ComplexNumber

Attributes:

real (float): The real part of the complex number.
imaginary (float): The imaginary part of the complex number.
Constructor:

__init__(self, real, imaginary): Initializes the real and imaginary attributes with the given values.
Methods/Functions:

__add__(self, other):

Parameters: other (another ComplexNumber object)
Task: Overload the + operator to add two complex numbers. The addition of two complex numbers (a + bi) and (c + di) is calculated as:
Real part: a + c
Imaginary part: b + d
Return: A new ComplexNumber object representing the sum of the two complex numbers.
__str__(self):

Parameters: None
Task: Overload the string representation of the object to return the complex number in the format "a + bi", where a is the real part and b is the imaginary part.
Examples:

Input: real1 = 3, imaginary1 = 2, real2 = 1, imaginary2 = 7
Output: 4 + 8i