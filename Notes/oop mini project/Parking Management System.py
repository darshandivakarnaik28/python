from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, license_plate, vehicle_type):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

    @abstractmethod
    def calculate_fee(self, hours):
        pass

class Car(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, "Car")

    def calculate_fee(self, hours):
        return hours * 40

class Bike(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, "Bike")

    def calculate_fee(self, hours):
        return hours * 20

class Truck(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, "Truck")

    def calculate_fee(self, hours):
        return hours * 80

class ParkingSlot:
    def __init__(self, slot_id, allowed_type):
        self.slot_id = slot_id
        self.allowed_type = allowed_type
        self.__is_occupied = False
        self.__current_vehicle = None

    def get_status(self):
        return self.__is_occupied

    def get_vehicle(self):
        return self.__current_vehicle

    def occupy(self, vehicle):
        if not self.__is_occupied and vehicle.vehicle_type == self.allowed_type:
            self.__is_occupied = True
            self.__current_vehicle = vehicle
            return True
        return False

    def vacate(self):
        self.__is_occupied = False
        self.__current_vehicle = None

class Ticket:
    ticket_counter = 1001

    def __init__(self, vehicle, slot_id):
        self.ticket_id = Ticket.ticket_counter
        Ticket.ticket_counter += 1
        self.vehicle = vehicle
        self.slot_id = slot_id

class ParkingLot:
    def __init__(self, name):
        self.name = name
        self.slots = []
        self.active_tickets = {}

    def add_parking_slot(self, slot):
        self.slots.append(slot)

    def display_available_slots(self):
        print(f"\n--- Available Slots at {self.name} ---")
        available = [s for s in self.slots if not s.get_status()]
        if not available:
            print("No slots available.")
            return
        for s in available:
            print(f"Slot ID: {s.slot_id} | Type Allowed: {s.allowed_type}")

    def park_vehicle(self, vehicle):
        for slot in self.slots:
            if not slot.get_status() and slot.allowed_type == vehicle.vehicle_type:
                if slot.occupy(vehicle):
                    ticket = Ticket(vehicle, slot.slot_id)
                    self.active_tickets[ticket.ticket_id] = ticket
                    print(f"Vehicle {vehicle.license_plate} parked in Slot {slot.slot_id}. Ticket ID: {ticket.ticket_id}")
                    return ticket
        print(f"No available slot for vehicle type: {vehicle.vehicle_type}")
        return None

    def remove_vehicle(self, ticket_id, hours):
        if ticket_id not in self.active_tickets:
            print("Invalid Ticket ID.")
            return
        
        ticket = self.active_tickets[ticket_id]
        vehicle = ticket.vehicle
        fee = vehicle.calculate_fee(hours)
        
        for slot in self.slots:
            if slot.slot_id == ticket.slot_id:
                slot.vacate()
                break
                
        del self.active_tickets[ticket_id]
        print(f"Vehicle {vehicle.license_plate} removed from Slot {ticket.slot_id}. Total Charge for {hours} hours: INR {fee}")

    def view_parked_vehicles(self):
        print(f"\n--- Parked Vehicles at {self.name} ---")
        occupied_slots = [s for s in self.slots if s.get_status()]
        if not occupied_slots:
            print("No vehicles parked.")
            return
        for s in occupied_slots:
            v = s.get_vehicle()
            print(f"Slot ID: {s.slot_id} | Type: {v.vehicle_type} | License Plate: {v.license_plate}")

    def display_parking_summary(self):
        print(f"\n--- Parking Lot Summary: {self.name} ---")
        total = len(self.slots)
        occupied = len([s for s in self.slots if s.get_status()])
        print(f"Total Slots: {total}")
        print(f"Occupied Slots: {occupied}")
        print(f"Available Slots: {total - occupied}")


my_lot = ParkingLot("Central Parking")

my_lot.add_parking_slot(ParkingSlot("C1", "Car"))
my_lot.add_parking_slot(ParkingSlot("C2", "Car"))
my_lot.add_parking_slot(ParkingSlot("B1", "Bike"))
my_lot.add_parking_slot(ParkingSlot("T1", "Truck"))

my_lot.display_available_slots()

car1 = Car("KA-01-AB-1234")
bike1 = Bike("KA-03-XY-9876")

t1 = my_lot.park_vehicle(car1)
t2 = my_lot.park_vehicle(bike1)

my_lot.view_parked_vehicles()
my_lot.display_parking_summary()

if t1:
    my_lot.remove_vehicle(t1.ticket_id, 4)

my_lot.display_parking_summary()
