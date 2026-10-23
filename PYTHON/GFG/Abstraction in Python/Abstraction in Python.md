Implement the following classes to understand abstraction in Python :
Note: Driver code makes all the function calls and print statements

Class Name: Shape (Abstract Class)
Attributes: color (String)
Constructor: Shape(c) -> assign value of c to color attribute
Methods: get_color() -> returns value of color
         get_area() -> abstract method with float return type
Class Name: Square (extends Shape)
Attributes: side (float)
Constructor: Square(c, side) -> calls super(c) to initialize the color and assigns the value to side.
Methods: get_area() -> returns the area of the square (side * side).
Example:

Input: color = "red", side = 5.0
Output: 
red 25.0