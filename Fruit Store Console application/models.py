# Models module for storing data structures and basic operations
# This module defines the core data structure for fruits in the system

class Fruit:
    """Class to represent a fruit item with its properties"""
    def __init__(self, name, quantity, price):
        # Initialize fruit properties
        self.name = name          # Name of the fruit
        self.quantity = quantity  # Quantity in kg
        self.price = price        # Price per kg

    def to_dict(self):
        """Convert fruit object to dictionary for storage"""
        return {
            'name': self.name,
            'quantity': self.quantity,
            'price': self.price
        }

    @classmethod
    def from_dict(cls, data):
        """Create fruit object from dictionary data"""
        return cls(data['name'], data['quantity'], data['price'])