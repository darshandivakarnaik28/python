class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Customer(Person):
    def __init__(self, name, email, customer_id):
        super().__init__(name, email)
        self.customer_id = customer_id

class Ticket:
    def __init__(self, seat_number, price, ticket_type="Regular"):
        self.seat_number = seat_number
        self.price = price
        self.ticket_type = ticket_type

    def get_price(self):
        return self.price  

class RegularTicket(Ticket):
    def __init__(self,seat_number, price):
        super().__init__(seat_number, price, ticket_type="Regular"  )
    def get_price(self):
            return self.price 

class PremiumTicket(Ticket):
    def __init__(self, seat_number, price):
        super().__init__(seat_number, price, ticket_type="Premium")
    def get_price(self):
        return self.price * 2  

class Movie:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class Show:
    def __init__(self, show_id, movie, start_time, total_seats):
        self.show_id = show_id
        self.movie = movie
        self.start_time = start_time
        self.__seats = {}
        for i in range(1, total_seats + 1):
            self.__seats[f"Seat-{i}"] = "Available"

    def get_available_seats(self):
        available = []
        for seat, status in self.__seats.items():
            if status == "Available":
                available.append(seat)
        return available

    def book_seat(self, seat_number):
        if self.__seats.get(seat_number) == "Available":
            self.__seats[seat_number] = "Booked"
            return True
        return False

    def free_seat(self, seat_number):
        if seat_number in self.__seats:
            self.__seats[seat_number] = "Available"

class Theater:
    def __init__(self, theater_id, name):
        self.theater_id = theater_id
        self.name = name
        self.shows = []

    def add_show(self, show):
        self.shows.append(show)
        print(f"{show.movie.title} at {show.start_time} added to {self.name}.")


class Booking:
    def __init__(self, booking_id, customer, show, tickets):
        self.booking_id = booking_id
        self.customer = customer
        self.show = show
        self.tickets = tickets
        self.status = "Active"

    def calculate_total(self):
        total = 0.0
        for ticket in self.tickets:
            total += ticket.get_price()
        return total

    def print_booking_details(self):
        print(f"\n--- Booking Receipt Details ---")
        print(f"Booking ID: {self.booking_id}")
        print(f"Customer Name: {self.customer.name}")
        print(f"Movie: {self.show.movie.title}")
        print(f"Time: {self.show.start_time}")
        print(f"Status: {self.status}")
        
        seats = []
        for ticket in self.tickets:
            seats.append(ticket.seat_number)
            
        print(f"Seats Booked: {', '.join(seats)}")
        print(f"Total Price ({', '.join(ticket.ticket_type for ticket in self.tickets)}): ${self.calculate_total():.2f}")

class MovieTicketBookingSystem:
    def __init__(self):
        self.movies = []
        self.bookings = {}
        self.booking_counter = 100

    def add_movie(self, movie):
        self.movies.append(movie)

    def display_movies(self):
        print("\n--- Currently Screening Movies ---")
        for movie in self.movies:
            print(f"- {movie.title} ({movie.duration})")

    def book_ticket(self, customer, show, requested_seats, ticket_type):
        tickets_to_issue = []
        base_cost = 100.0
        for seat in requested_seats:
            if show.book_seat(seat):
                if ticket_type.lower() == "premium":
                    new_ticket = PremiumTicket(seat, base_cost)
                else:
                    new_ticket = RegularTicket(seat, base_cost)
                tickets_to_issue.append(new_ticket)
            else:
                print(f"Booking failed! {seat} is already occupied.")
                for t in tickets_to_issue:
                    show.free_seat(t.seat_number)
                return None

        self.booking_counter += 1
        new_booking = Booking(self.booking_counter, customer, show, tickets_to_issue)
        self.bookings[self.booking_counter] = new_booking
        return new_booking

    def cancel_ticket(self, booking_id):
        if booking_id in self.bookings:
            booking = self.bookings[booking_id]
            if booking.status == "Active":
                booking.status = "Cancelled"
                for ticket in booking.tickets:
                    booking.show.free_seat(ticket.seat_number)
                print(f"\nSuccess: Booking {booking_id} has been cancelled.")
                return
        print("\nError: Invalid Booking ID.")

if __name__ == "__main__":
    system = MovieTicketBookingSystem()
    movie1 = Movie("The Dark Knight", "152 mins")
    system.add_movie(movie1)
    system.display_movies()
    theater1 = Theater(1, "Grand Cinema Room 4")
    evening_show = Show(show_id=55, movie=movie1, start_time="7:00 PM", total_seats=4)
    theater1.add_show(evening_show)
    print(f"\nInitial Open Seats: {evening_show.get_available_seats()}")
    customer1 = Customer(name="John Doe", email="john@test.com", customer_id=987)
    booking1 = system.book_ticket(customer1, evening_show, ["Seat-1", "Seat-2"], "premium")
    if booking1:
        booking1.print_booking_details()
    print(f"\nSeats available after booking: {evening_show.get_available_seats()}")
    system.cancel_ticket(booking1.booking_id)
    print(f"Seats available after cancellation: {evening_show.get_available_seats()}")