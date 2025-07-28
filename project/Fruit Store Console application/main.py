# Main module - Entry point of the application
# This module handles the main menu and program flow

from manager import FruitManager
from customer import Customer
from sys import exit 
from storage import Storage
from datetime import datetime
from models import Fruit
def main():
    """Main function to run the Fruit Market application"""
    # Initialize manager and customer objects
    manager = FruitManager()
    customer = Customer(manager)

    while True:
        # Display main menu
        print("\nWELCOME TO FRUIT MARKET")
        print("1) Manager")
        print("2) Customer")
        print("3) Exit")

        try:
            # Get user role selection
            role = input("\nSelect your Role : ").strip()

            if role == '1':
                # Manager menu loop
                while True:
                    print("\nFruit Market Manager")
                    print("1) Add Fruit Stock")
                    print("2) View Fruit Stock")
                    print("3) Update Fruit stock")
                    print("4) Back to Main Menu")

                    choice = input("\nEnter your choice : ").strip()

                    # Handle manager operations
                    if choice == '1':
                        manager.add_fruit()
                    elif choice == '2':
                        manager.view_stock()
                    elif choice == '3':
                        manager.update_stock()
                    elif choice == '4':
                        break
                    else:
                        print("Invalid choice! Please try again.")

                    # Ask for more operations
                    if choice in ['1', '2', '3']:
                        more = input("\nDo you want to perform more operations : press y for yes and n for no : ").lower().strip()
                        if more != 'y':
                            break

            elif role == '2':
                while True:
                    print("\nCustomer Menu")
                    print("1) View Fruits")
                    print("2) Purchase Fruits")
                    print("3) Back to Main Menu")

                    choice = input("\nEnter your choice : ").strip()

                    if choice == '1':
                        customer.view_fruits()
                    elif choice == '2':
                        customer.purchase_fruits()
                    elif choice == '3':
                        break
                    else:
                        print("Invalid choice! Please try again.")

                    if choice in ['1', '2']:
                        more = input("\nDo you want to perform more operations : press y for yes and n for no : ").lower().strip()
                        if more != 'y':
                            break

            elif role == '3':
                print("Thank you for using Fruit Market! Goodbye!")
                break
            else:
                print("Invalid role! Please try again.")

        except Exception as e:
            print("An error occurred. Please try again.")

if __name__ == '__main__':
    main()