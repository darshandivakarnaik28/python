# Implement the Person class
class Person:
    def __init__(self):
        self.name=None
        self.age=10
    def get_name(self,name="Geeks"):
        if self.name is None:
            return name
        return self.name
    def set_name(self,name):
        self.name=name
        return self.name
    def set_age(self,age):
        self.age=age
        return self.age
    def get_age(self):
        return self.age