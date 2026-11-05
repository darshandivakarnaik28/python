class Car:
    def __init__(self, brand, model, year):
        # Initialize brand, model, and year
        self.brand=brand
        self.model=model
        self.year=year
        

    def displayDetails(self):
        # Print car details in the specified format
        print("Car Details:")
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Year:",self.year)
        

class Solution:
    def fun(self, brand, model, year):
        
        # Create Car class and call displayDetails() method
        car = Car(brand, model, year)
        car.displayDetails()