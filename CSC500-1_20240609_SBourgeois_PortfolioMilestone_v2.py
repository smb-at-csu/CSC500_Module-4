# CSC500-1 Module 4 Portfolio Milestone
#
# STEP 1: Build ItemToPurchase class with 3 attributes: name, price and quantity.
#         
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
#
# Define a method to print the cost of an item.
#
    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity}")
#
# Prompt user for name, price and quantity of two items:
#
def main():
    print("Item 1")
    item_name = input("Enter ITEM ONE name: ")
    item_price = float(input("Enter ITEM ONE price: "))
    item_quantity = int(input("Enter ITEM ONE quantity: "))
    item1 = ItemToPurchase(item_name, item_price, item_quantity)

    print("\nItem 2")
    item_name = input("Enter ITEM TWO name: ")
    item_price = float(input("Enter ITEM TWO price: "))
    item_quantity = int(input("Enter ITEM TWO quantity: "))
    item2 = ItemToPurchase(item_name, item_price, item_quantity)
#
# Calculate and display the total cost of the two items based on input.
#
    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    print(f"Total: ${item1.item_price * item1.item_quantity + item2.item_price * item2.item_quantity}")
#
#
#
if __name__ == "__main__":
    main()
