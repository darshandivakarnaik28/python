# Food Delivery System using OOP concepts in Python
from abc import ABC, abstractmethod
class DeliveryType(ABC):
    @abstractmethod
    def get_fee(self):
        pass

    @abstractmethod
    def get_time(self):
        pass

class NormalDelivery(DeliveryType):
    def get_fee(self):
        return 40

    def get_time(self):
        return "45-60 mins"

class ExpressDelivery(DeliveryType):
    def get_fee(self):
        return 90

    def get_time(self):
        return "20-30 mins"

class FoodItem:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

class Restaurant:
    def __init__(self, restaurant_id, name):
        self.restaurant_id = restaurant_id
        self.name = name
        self.menu = []

    def add_food_item(self, food_item):
        self.menu.append(food_item)

    def display_menu(self):
        print(f"\nMenu for {self.name}:")
        for item in self.menu:
            print(f"ID: {item.item_id} | {item.name} | INR {item.price}")

class User:
    def __init__(self, user_id, name, phone):
        self.user_id = user_id
        self.name = name
        self.phone = phone

class Customer(User):
    def __init__(self, user_id, name, phone, address):
        super().__init__(user_id, name, phone)
        self.address = address

class Order:
    id_counter = 101

    def __init__(self, customer, restaurant, delivery_type):
        self.__order_id = Order.id_counter
        Order.id_counter += 1
        self.__customer = customer
        self.__restaurant = restaurant
        self.__delivery_type = delivery_type
        self.__items = {}
        self.__status = "Pending"

    def add_food_item(self, food_item, quantity):
        if food_item in self.__restaurant.menu:
            if food_item in self.__items:
                self.__items[food_item] += quantity
            else:
                self.__items[food_item] = quantity
            print(f"Added {quantity} x {food_item.name}")
        else:
            print("Item not found in this restaurant menu")

    def calculate_total(self):
        subtotal = sum(item.price * qty for item, qty in self.__items.items())
        delivery_fee = self.__delivery_type.get_fee()
        return subtotal + delivery_fee

    def place_order(self):
        if not self.__items:
            print("Cannot place an empty order")
            return
        self.__status = "Placed"
        print(f"Order {self.__order_id} has been placed!")

    def track_status(self):
        return self.__status

    def update_status(self, new_status):
        self.__status = new_status

    def view_order_details(self):
        print(f"\n--- Order Details (ID: {self.__order_id}) ---")
        print(f"Customer: {self.__customer.name}")
        print(f"Restaurant: {self.__restaurant.name}")
        print(f"Delivery Address: {self.__customer.address}")
        print(f"Delivery Mode: {type(self.__delivery_type).__name__}")
        print(f"Estimated Time: {self.__delivery_type.get_time()}")
        print(f"Status: {self.__status}")
        print("Items Ordered:")
        for item, qty in self.__items.items():
            print(f" - {item.name} x {qty} : INR {item.price * qty}")
        print(f"Total Bill: INR {self.calculate_total()}")


restaurants_database = []

r1 = Restaurant(1, "Pizza House")
f1 = FoodItem(10, "Margherita Pizza", 250)
f2 = FoodItem(11, "Garlic Bread", 120)
r1.add_food_item(f1)
r1.add_food_item(f2)
restaurants_database.append(r1)

r2 = Restaurant(2, "Burger Zone")
f3 = FoodItem(20, "Cheese Burger", 150)
r2.add_food_item(f3)
restaurants_database.append(r2)

for r in restaurants_database:
    r.display_menu()

c1 = Customer(501, "John Doe", "9876543210", "123 Main Street")

delivery_mode = ExpressDelivery()
order1 = Order(c1, r1, delivery_mode)

order1.add_food_item(f1, 2)
order1.add_food_item(f2, 1)

order1.place_order()

order1.view_order_details()

print(f"\nCurrent Status: {order1.track_status()}")
order1.update_status("Out for Delivery")
print(f"Updated Status: {order1.track_status()}")
