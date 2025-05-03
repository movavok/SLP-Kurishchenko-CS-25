class Order:
    """
    Represents a coffee order in the coffee shop.
    Attributes:
        orderId (int): Unique identifier for the order.
        customerName (str): Name of the customer who placed the order.
        coffeeType (str): Type of coffee ordered.
    """
    def __init__(self, orderId, customerName, coffeeType):
        self.orderId = orderId
        self.customerName = customerName
        self.coffeeType = coffeeType

    def __str__(self):
        return f"Order ID: {self.orderId}, Customer: {self.customerName}, Coffee Type: {self.coffeeType}"

    def __del__(self):
        print(f"Order {self.orderId} for {self.customerName} has been deleted.")

class CoffeeShop:
    """
    Represents a coffee shop with order management functionality.
    """
    def __init__(self):
        self.orders = []
        self.order_counter = 0
        self.coffee_types = {
            "1": "Espresso",
            "2": "Latte",
            "3": "Cappuccino",
            "4": "Americano",
            "5": "Mocha"
        }

    def add_order(self):
        """
        Adds a new order to the coffee shop.
        Returns: None
        """
        order_id = self.order_counter
        self.order_counter += 1

        while True:
            customer_name = input("Enter customer name: ")
            if customer_name:
                break
            print("Customer name cannot be empty.")

        while True:
            print("Choose coffee type: ")
            for key, value in self.coffee_types.items():
                print(f"{key}: {value}")
            choice = input("Enter coffee type: ")
            if choice in self.coffee_types:
                coffee_type = self.coffee_types[choice]
                break
            print("Invalid coffee type. Please try again.")

        order = Order(order_id, customer_name, coffee_type)
        self.orders.append(order)
        print(f"Order {order.orderId} for {order.customerName} has been added.")

    def view_orders(self):
        """
        Displays all current orders in the coffee shop.
        Returns: None
        """
        if not self.orders:
            print("No orders found.")
            return
        print("Current orders:")
        for order in self.orders:
            print(order)

    def delete_order(self, order_id):
        """
        Deletes an order from the coffee shop by order ID.
        Returns: None
        """
        for order in self.orders:
            if order.orderId == order_id:
                self.orders.remove(order)
                return
        print(f"Order {order_id} not found.")

    def show_menu(self):
        """
        Displays the coffee shop menu and handles user input for order management.
        Returns: None
        """
        while True:
            print("\n1 -> Add order")
            print("2 -> View orders")
            print("3 -> Delete order")
            print("0 -> Back to main menu")
            
            match input("Enter your choice: "):
                case "1": self.add_order()
                case "2": self.view_orders()
                case "3": 
                    order_id = int(input("Enter order ID to delete: "))
                    self.delete_order(order_id)
                case "0": return
                case _: print("Invalid choice. Please try again.")