class Order:
    def __init__(self, order_id, customer_name, items):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items
        self.status = "Pending"  # Order status (Pending, Prepared, Delivered)

    def __str__(self):
        return f"Order ID: {self.order_id}, Customer: {self.customer_name}, Items: {self.items}, Status: {self.status}"


class FoodOrderSystem:
    def __init__(self):
        self.orders = []  # List to manage orders
        self.order_details = {}  # Hashmap to track order details by order_id

    def place_order(self, customer_name, items):
        order_id = len(self.orders) + 1  # Simple order ID generation
        order = Order(order_id, customer_name, items)
        self.orders.append(order)  # Add order to the list
        self.order_details[order_id] = order  # Store order in the hashmap
        print(f"Order placed: {order}")

    def prepare_order(self):
        if not self.orders:
            print("No orders to prepare.")
            return
        # Prepare the first order in the list
        order_to_prepare = self.orders.pop(0)  # Remove the first order (FIFO)
        order_to_prepare.status = "Prepared"
        print(f"Order prepared: {order_to_prepare}")

    def deliver_order(self):
        if not self.orders:
            print("No orders to deliver.")
            return
        # Prepare and deliver the next order
        order_to_deliver = self.order_details[len(self.orders) + 1]
        order_to_deliver.status = "Delivered"
        print(f"Order delivered: {order_to_deliver}")

# Example usage
if __name__ == "__main__":
    food_order_system = FoodOrderSystem()

    # Placing orders
    food_order_system.place_order("Alice", ["Pizza", "Salad"])
    food_order_system.place_order("Bob", ["Burger", "Fries"])
    food_order_system.place_order("Charlie", ["Sushi", "Tea"])

    # Preparing and delivering orders
    food_order_system.prepare_order()  # Prepare Alice's order
    food_order_system.deliver_order()  # Deliver Alice's order

    food_order_system.prepare_order()  # Prepare Bob's order
    food_order_system.deliver_order()  # Deliver Bob's order

    food_order_system.prepare_order()  # Prepare Charlie's order
    food_order_system.deliver_order()  # Deliver Charlie's order
