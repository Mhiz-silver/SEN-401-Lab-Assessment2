"""
Helper functions for inventory calculations.
"""


def highest_stock_item(items):
    """Returns the item with the highest stock value."""
    if not items:
        raise ValueError("Inventory is empty.")

    highest = items[0]

    for item in items:
        current_value = item["quantity"] * item["price"]
        highest_value = highest["quantity"] * highest["price"]

        if current_value > highest_value:
            highest = item

    return highest


def lowest_stock_item(items):
    """Returns the item with the lowest stock value."""
    if not items:
        raise ValueError("Inventory is empty.")

    lowest = items[0]

    for item in items:
        current_value = item["quantity"] * item["price"]
        lowest_value = lowest["quantity"] * lowest["price"]

        if current_value < lowest_value:
            lowest = item

    return lowest


def total_stock_value(items):
    """Returns the total value of all stock."""

    total = 0

    for item in items:
        total += item["quantity"] * item["price"]

    return total
