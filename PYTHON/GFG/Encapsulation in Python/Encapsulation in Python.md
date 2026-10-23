Implement a Person class in Python that demonstrates encapsulation. This class should have two "private" attributes:

name (String) with a default value of "Geeks".
age (int) with a default value of 10.
The class should provide public methods to access and modify these private attributes:

Getter Methods: get_name() and get_age()
Setter Methods: set_name(name) and set_age(age)
Example:

Input: Funtion calls: [Person(), get_name(), set_name("John"), set_age(21), get_name(), get_age()] 
Output: Geeks John 21
Explanation: 
person = Person() // Person Object Created
person.get_name() // Default value "Geeks" returned
person.set_name("John") // name value set to "John"
person.set_age(21) // age value set to 21
person.get_name() // "John" returned
person.get_age() // 21 returned