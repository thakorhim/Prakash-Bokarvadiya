from storage import Storage

class Customer:
    def __init__(self, manager):
        self.manager = manager
        self.storage = Storage()

    def view_fruits(self):
        self.manager.view_stock()

    def purchase_fruits(self):
        self.view_fruits()
        if not self.manager.stock:
            return

        while True:
            try:
                name = input("\nEnter fruit name to purchase: ").strip().capitalize()
                if name not in self.manager.stock:
                    print("Fruit not found in stock!")
                    continue

                available = self.manager.stock[name]['quantity']
                quantity = input(f"Enter quantity to purchase (max {available}kg): ").strip()

                if not quantity.isdigit() or int(quantity) <= 0:
                    print("Invalid quantity. Please enter a positive number.")
                    continue

                quantity = int(quantity)
                if quantity > available:
                    print(f"Sorry, only {available}kg available in stock.")
                    continue

                price = self.manager.stock[name]['price']
                total = quantity * price

                print(f"\nTotal amount: ${total}")
                confirm = input("Confirm purchase? (y/n): ").lower().strip()

                if confirm == 'y':
                    self.manager.stock[name]['quantity'] -= quantity
                    self.manager.storage.save_data(self.manager.stock)
                    self.storage.log_transaction(
                        f"Purchase: {name} - Qty: {quantity}kg, Total: ${total}")
                    print("Purchase successful!")
                    break
                else:
                    print("Purchase cancelled.")
                    break
            except Exception as e:
                print("An error occurred. Please try again.")
                self.storage.log_transaction(f"Error in purchase: {str(e)}")