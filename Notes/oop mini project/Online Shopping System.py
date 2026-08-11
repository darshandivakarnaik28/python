# Online Shopping System using OOP concepts in Python
from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
class CreditCardPayment(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def process_payment(self, amount):
        print(f"Paid INR {amount} using Credit Card ending in {self.card_number[-4:]}.")
        return True

class UPIPayment(PaymentMethod):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def process_payment(self, amount):
        print(f"Paid INR {amount} via UPI ID {self.upi_id}.")
        return True

class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.__price = price
        self.__stock = stock

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def reduce_stock(self, quantity):
        if quantity <= self.__stock:
            self.__stock -= quantity
            return True
        return False

    def restore_stock(self, quantity):
        self.__stock += quantity

    def display_details(self):
        print(f"ID: {self.product_id} | Name: {self.name} | Price: INR {self.__price} | Stock: {self.__stock}")

class Electronics(Product):
    def __init__(self, product_id, name, price, stock, warranty_months):
        super().__init__(product_id, name, price, stock)
        self.warranty_months = warranty_months

    def display_details(self):
        super().display_details()
        print(f"Warranty: {self.warranty_months} months")

class Clothing(Product):
    def __init__(self, product_id, name, price, stock, size):
        super().__init__(product_id, name, price, stock)
        self.size = size

    def display_details(self):
        super().display_details()
        print(f"Size: {self.size}")

class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if product.get_stock() < quantity:
            print(f"Cannot add {quantity} of {product.name}. Only {product.get_stock()} available.")
            return False
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity
        print(f"Added {quantity} x {product.name} to cart.")
        return True

    def remove_item(self, product, quantity):
        if product not in self.items:
            print(f"{product.name} is not in the cart.")
            return False
        if quantity >= self.items[product]:
            del self.items[product]
        else:
            self.items[product] -= quantity
        print(f"Removed {quantity} x {product.name} from cart.")
        return True

    def calculate_total(self):
        total = 0
        for product, quantity in self.items.items():
            total += product.get_price() * quantity
        return total

    def clear_cart(self):
        self.items.clear()

class Order:
    order_id_counter = 1001

    def __init__(self, customer, cart_items, total_amount):
        self.order_id = Order.order_id_counter
        Order.order_id_counter += 1
        self.customer = customer
        self.items = dict(cart_items)
        self.total_amount = total_amount
        self.status = "Placed"

    def display_order(self):
        print(f"\n--- Order Details (ID: {self.order_id}) ---")
        print(f"Customer: {self.customer.name}")
        print(f"Status: {self.status}")
        print("Items:")
        for product, quantity in self.items.items():
            print(f" - {product.name} x {quantity} : INR {product.get_price() * quantity}")
        print(f"Total Paid: INR {self.total_amount}")

class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.cart = Cart()
        self.order_history = []

    def checkout(self, payment_method):
        total = self.cart.calculate_total()
        if total == 0:
            print("Cart is empty. Cannot place order.")
            return None

        for product, quantity in self.cart.items.items():
            if product.get_stock() < quantity:
                print(f"Checkout failed. {product.name} went out of stock.")
                return None

        if payment_method.process_payment(total):
            for product, quantity in self.cart.items.items():
                product.reduce_stock(quantity)
            
            new_order = Order(self, self.cart.items, total)
            self.order_history.append(new_order)
            self.cart.clear_cart()
            print("Order placed successfully.")
            return new_order
        else:
            print("Payment failed. Order aborted.")
            return None

class OnlineStore:
    def __init__(self):
        self.inventory = []

    def add_product(self, product):
        self.inventory.append(product)

    def display_products(self):
        print("\n--- Store Inventory ---")
        if not self.inventory:
            print("No products available.")
            return
        for product in self.inventory:
            product.display_details()
            print("-" * 20)

    def search_products(self, query):
        print(f"\n--- Search Results for '{query}' ---")
        found = False
        for product in self.inventory:
            if query.lower() in product.name.lower():
                product.display_details()
                print("-" * 20)
                found = True
        if not found:
            print("No matching products found.")


store = OnlineStore()

laptop = Electronics(1, "Gaming Laptop", 75000, 5, 24)
shirt = Clothing(2, "Cotton Casual Shirt", 1500, 10, "L")
headphones = Electronics(3, "Wireless Headphones", 4500, 8, 12)

store.add_product(laptop)
store.add_product(shirt)
store.add_product(headphones)

store.display_products()

store.search_products("Laptop")

alice = Customer(101, "Alice")

alice.cart.add_item(laptop, 1)
alice.cart.add_item(shirt, 2)

print(f"Current Cart Total: INR {alice.cart.calculate_total()}")

alice.cart.remove_item(shirt, 1)

print(f"Updated Cart Total: INR {alice.cart.calculate_total()}")

card_payment = CreditCardPayment("1234-5678-9876-5432")
order1 = alice.checkout(card_payment)

if order1:
    order1.display_order()

store.display_products()

alice.cart.add_item(headphones, 1)
upi_payment = UPIPayment("alice@upi")
order2 = alice.checkout(upi_payment)

if order2:
    order2.display_order()
