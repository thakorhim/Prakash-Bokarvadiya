# Manager module for handling fruit inventory operations
# This module contains the business logic for the manager role

from models import Fruit
from storage import Storage


class FruitManager:
    """Class to handle all manager operations for fruit inventory"""
    def __init__(self):
        # Initialize manager with storage system
        self.storage = Storage()
        self.stock = self.storage.load_data()

    def add_fruit(self):
        """Add new fruit to inventory with validation"""
        while True:
            try:
                # Get and validate fruit name
                name = input("Enter fruit Name : ").strip().capitalize()
                if not name.isalpha():
                    print("Invalid fruit name. Please use only letters.")
                    continue

                # Get and validate quantity
                quantity = input("Enter qty (in kg): ").strip()
                if not quantity.isdigit() or int(quantity) <= 0:
                    print("Invalid quantity. Please enter a positive number.")
                    continue

                # Get and validate price
                price = input("Enter price (for kg): ").strip()
                if not price.isdigit() or int(price) <= 0:
                    print("Invalid price. Please enter a positive number.")
                    continue

                # Create and save fruit object
                fruit = Fruit(name, int(quantity), int(price))
                self.stock[name] = fruit.to_dict()
                self.storage.save_data(self.stock)
                self.storage.log_transaction(f"Added fruit: {name} - Qty: {quantity}kg, Price: ${price}/kg")
                print(f"Successfully added {name} to stock!")
                break
            except Exception as e:
                print("An error occurred. Please try again.")
                self.storage.log_transaction(f"Error adding fruit: {str(e)}")

    def view_stock(self):
        if not self.stock:
            print("No fruits in stock!")
            return

        print("\nCurrent Fruit Stock:")
        print("-" * 40)
        print(f"{'Fruit':<15}{'Quantity(kg)':<15}{'Price/kg':<10}")
        print("-" * 40)
        for name, details in self.stock.items():
            print(f"{name:<15}{details['quantity']:<15}${details['price']:<10}")

    def update_stock(self):
        self.view_stock()
        if not self.stock:
            return

        while True:
            try:
                name = input("\nEnter fruit name to update: ").strip().capitalize()
                if name not in self.stock:
                    print("Fruit not found in stock!")
                    continue

                quantity = input("Enter new quantity (in kg): ").strip()
                if not quantity.isdigit() or int(quantity) < 0:
                    print("Invalid quantity. Please enter a non-negative number.")
                    continue

                price = input("Enter new price (for kg): ").strip()
                if not price.isdigit() or int(price) <= 0:
                    print("Invalid price. Please enter a positive number.")
                    continue

                fruit = Fruit(name, int(quantity), int(price))
                self.stock[name] = fruit.to_dict()
                self.storage.save_data(self.stock)
                self.storage.log_transaction(f"Updated fruit: {name} - Qty: {quantity}kg, Price: ${price}/kg")
                print(f"Successfully updated {name} stock!")
                break
            except Exception as e:
                print("An error occurred. Please try again.")
                self.storage.log_transaction(f"Error updating fruit: {str(e)}")