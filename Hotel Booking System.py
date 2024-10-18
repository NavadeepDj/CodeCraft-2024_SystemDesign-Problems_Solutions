class Room:
    def __init__(self, room_id, room_type, base_price):
        self.room_id = room_id
        self.room_type = room_type
        self.base_price = base_price
        self.is_available = True
        self.bookings = []  # List to track bookings (start_day, end_day)

    def book(self, start_day, end_day):
        self.is_available = False
        self.bookings.append((start_day, end_day))

    def cancel(self, start_day):
        self.is_available = True
        self.bookings = [booking for booking in self.bookings if booking[0] != start_day]

    def check_availability(self, start_day, end_day):
        if not self.is_available:
            for booking in self.bookings:
                if (start_day < booking[1] and end_day > booking[0]):  # Overlapping dates
                    return False
        return True

    def calculate_price(self, start_day, end_day):
        total_days = end_day - start_day
        total_price = self.base_price * total_days
        
        # Apply discounts for long stays (more than 5 days)
        if total_days > 5:
            total_price *= 0.9  # 10% discount
        
        return total_price


class User:
    def __init__(self, username):
        self.username = username
        self.bookings = []  # List to track user's bookings

    def add_booking(self, room_id, start_day, end_day):
        self.bookings.append((room_id, start_day, end_day))

    def cancel_booking(self, room_id, start_day):
        self.bookings = [booking for booking in self.bookings if booking[0] != room_id or booking[1] != start_day]


class Hotel:
    def __init__(self):
        self.rooms = {}
        self.users = {}

    def add_room(self, room_id, room_type, base_price):
        self.rooms[room_id] = Room(room_id, room_type, base_price)

    def add_user(self, username):
        self.users[username] = User(username)

    def check_availability(self, room_id, start_day, end_day):
        room = self.rooms.get(room_id)
        if room:
            return room.check_availability(start_day, end_day)
        return False

    def book_room(self, username, room_id, start_day, end_day):
        room = self.rooms.get(room_id)
        user = self.users.get(username)
        if room and room.check_availability(start_day, end_day):
            room.book(start_day, end_day)
            total_price = room.calculate_price(start_day, end_day)
            print(f"{username} booked room {room_id} from day {start_day} to day {end_day}. Total price: ${total_price:.2f}")
            user.add_booking(room_id, start_day, end_day)  # Add booking to user's list
            return total_price
        else:
            print("Room not available for the selected dates.")
            return None

    def cancel_booking(self, username, room_id, start_day):
        room = self.rooms.get(room_id)
        user = self.users.get(username)
        if room and user:
            cancellation_charge = self.calculate_cancellation_charge(start_day)
            room.cancel(start_day)
            user.cancel_booking(room_id, start_day)  # Remove booking from user's list
            print(f"{username}'s booking for room {room_id} on day {start_day} cancelled. Cancellation charge: ${cancellation_charge:.2f}")

    def calculate_cancellation_charge(self, start_day):
        # Simple logic for cancellation charges
        days_until_checkin = start_day  # Assuming today is day 0
        if days_until_checkin < 1:
            return 100  # No refund if canceled on the same day
        elif 1 <= days_until_checkin <= 3:
            return 50  # 50% charge if canceled within 3 days
        return 0  # No charge for cancellations more than 3 days in advance


# Example usage
if __name__ == "__main__":
    hotel = Hotel()
    hotel.add_room("101", "Single", 100)
    hotel.add_room("102", "Double", 150)
    hotel.add_room("103", "Suite", 250)

    # Adding users
    hotel.add_user("Alice")
    hotel.add_user("Bob")

    # Booking a room for Alice
    start_day = 1  # Book starting tomorrow (day 1)
    end_day = 5    # Book for 4 days
    hotel.book_room("Alice", "101", start_day, end_day)

    # Check availability for Bob
    is_available = hotel.check_availability("101", start_day, end_day)
    print(f"Room 101 availability: {is_available}")

    # Cancel booking for Alice
    hotel.cancel_booking("Alice", "101", start_day)
