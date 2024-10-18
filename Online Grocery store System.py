# Define the Product class
class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        return False

    def increase_stock(self, quantity):
        self.stock += quantity

# Define the Cart class
class Cart:
    def __init__(self):
        self.items = []  # To store (Product, quantity) tuples

    def add_item(self, product, quantity):
        if product.reduce_stock(quantity):
            self.items.append((product, quantity))
            print(f"Added {quantity} of {product.name} to cart.")
        else:
            print(f"Not enough stock for {product.name}.")

    def remove_item(self, product):
        for item in self.items:
            if item[0] == product:
                product.increase_stock(item[1])  # Revert stock
                self.items.remove(item)
                print(f"Removed {item[1]} of {product.name} from cart.")
                return

    def checkout(self):
        if not self.items:
            print("Cart is empty!")
        else:
            total = sum([item[0].price * item[1] for item in self.items])
            print(f"Order placed. Total cost: ${total:.2f}")
            self.items.clear()

    def cancel_order(self):
        for product, quantity in self.items:
            product.increase_stock(quantity)  # Restore stock
        self.items.clear()
        print("Order canceled, stock restored.")

    def view_cart(self):
        if not self.items:
            print("Cart is empty!")
        else:
            for item in self.items:
                print(f"{item[1]}x {item[0].name} - ${item[0].price} each")


# Define the User class
class User:
    def __init__(self, username):
        self.username = username
        self.cart = Cart()
        self.is_logged_in = False

    def login(self):
        self.is_logged_in = True
        print(f"{self.username} logged in.")

    def logout(self):
        self.is_logged_in = False
        print(f"{self.username} logged out.")

# Main simulation function to demonstrate the system
def main():
    # Create products
    apples = Product(1, "Apples", 3.0, 10)
    bananas = Product(2, "Bananas", 1.5, 5)
    oranges = Product(3, "Oranges", 2.0, 7)

    # Display available products
    print("Available products:")
    for product in [apples, bananas, oranges]:
        print(f"{product.name}: ${product.price}, Stock: {product.stock}")

    # Create a user
    user = User("JohnDoe")

    # User login
    user.login()

    # User can now interact with the cart (only if logged in)
    if user.is_logged_in:
        # Add products to the cart
        user.cart.add_item(apples, 2)
        user.cart.add_item(bananas, 3)

        # View the cart
        user.cart.view_cart()

        # Checkout
        user.cart.checkout()

        # View available stock after checkout
        print("\nStock after checkout:")
        for product in [apples, bananas, oranges]:
            print(f"{product.name}: Stock: {product.stock}")

        # User logout
        user.logout()

if __name__ == "__main__":
    main()
