import datetime
import random

user_id_counter = 0

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.created_at = datetime.datetime.now()

    def display_info(self):
        """Displays item information."""
        # TODO: Improve the output format to be more user-friendly
        print(f"Item: {self.name}, Price: {self.price}, Created: {self.created_at}")

    # todo: Add logging functionality when the item price is updated
    def update_price(self, new_price):
        if new_price > 0:
            self.price = new_price
            print(f"The price of {self.name} has been updated to {self.price}.")
        else:
            # Todo: Improve exception handling or warning message for invalid price input
            print("Invalid value")

# FIXME: The function below depends on the current test data. Actual data source connection required.
def generate_sample_report(item_count=5):
    items = []
    for i in range(item_count):
        item_name = f"Sample Item {i+1}"
        item_price = random.randint(1000, 50000)
        items.append(Item(item_name, item_price))

    for item in items:
        item.display_info()

def main():
    item1 = Item("MacBook", 1200000)
    item1.display_info()
    item1.update_price(1150000)
    generate_sample_report(3)

if __name__ == "__main__":
    main()
