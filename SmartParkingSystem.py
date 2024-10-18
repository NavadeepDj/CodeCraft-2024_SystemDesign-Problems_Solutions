class ParkingSpot:
    def __init__(self, spot_id, hourly_rate):
        self.spot_id = spot_id
        self.hourly_rate = hourly_rate
        self.is_available = True
        self.booked_hours = 0

    def book(self, hours):
        if self.is_available:
            self.is_available = False
            self.booked_hours = hours
            return True
        return False

    def cancel(self):
        if not self.is_available:
            self.is_available = True
            self.booked_hours = 0
            return True
        return False

    def calculate_price(self):
        return self.hourly_rate * self.booked_hours if not self.is_available else 0


class User:
    def __init__(self, username):
        self.username = username
        self.booked_spots = []

    def book_spot(self, spot, hours):
        if spot.book(hours):
            self.booked_spots.append(spot)
            return True
        return False

    def cancel_spot(self, spot):
        if spot in self.booked_spots and spot.cancel():
            self.booked_spots.remove(spot)
            return True
        return False


class ParkingManagementSystem:
    def __init__(self):
        self.spots = {}
        self.users = {}

    def add_parking_spot(self, spot_id, hourly_rate):
        self.spots[spot_id] = ParkingSpot(spot_id, hourly_rate)

    def register_user(self, username):
        if username not in self.users:
            self.users[username] = User(username)
            return True
        return False

    def login_user(self, username):
        return self.users.get(username)

    def view_available_spots(self):
        return [spot for spot in self.spots.values() if spot.is_available]

    def calculate_total_price(self, spot):
        return spot.calculate_price()


# Example usage
if __name__ == "__main__":
    parking_system = ParkingManagementSystem()

    # Adding parking spots
    parking_system.add_parking_spot("A1", 5)  # Spot A1 costs $5 per hour
    parking_system.add_parking_spot("A2", 4)  # Spot A2 costs $4 per hour

    # Registering a user
    parking_system.register_user("user1")

    # User login
    user = parking_system.login_user("user1")
    if user:
        print(f"{user.username} logged in.")

        # Viewing available spots
        available_spots = parking_system.view_available_spots()
        print("Available parking spots:")
        for spot in available_spots:
            print(f"Spot ID: {spot.spot_id}, Hourly Rate: ${spot.hourly_rate}")

        # Booking a spot
        if user.book_spot(available_spots[0], 3):  # Book for 3 hours
            booked_spot = available_spots[0]
            print(f"Booked Spot: {booked_spot.spot_id} for {booked_spot.booked_hours} hours.")

            # Calculate total price
            total_price = parking_system.calculate_total_price(booked_spot)
            print(f"Total price for booking Spot {booked_spot.spot_id}: ${total_price}")

        # Canceling the booking
        if user.cancel_spot(booked_spot):
            print(f"Cancelled booking for Spot: {booked_spot.spot_id}.")

            # Check if the spot is available again
            print(f"Spot {booked_spot.spot_id} is now available: {booked_spot.is_available}")

        else:
            print("Failed to cancel booking.")
