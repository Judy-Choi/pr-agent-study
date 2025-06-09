# example_with_todo.py


def empty_function():
    # TODO:
    pass

def calculate_total(price, tax):
    total = price + (price * tax)
    return total

# TODO: Add currency formatting to the total
def display_total():
    total = calculate_total(100, 0.1)
    print(f"Total: {total}")  # just prints raw number for now

# TODO: Refactor to handle discounts
# Refactor this function to handle discounts.
# Consider edge cases where discount > price.
def apply_discount(price, discount):
    return price - discount

# TODO:
# - Write tests for display_total()
# - Consider localization for different currency formats
def format_price(price):
    return f"${price:.2f}"

def main():
    # TODO
    print("Receipt")
    display_total()

    # TODO: mock data
    # Refactor this data to use input data
    # Change print format to use f-string
    print("With discount:", apply_discount(100, 20))
    print("Formatted:", format_price(88.8888))

# TODO: Add CLI interface using argparse
if __name__ == "__main__":
    main()
