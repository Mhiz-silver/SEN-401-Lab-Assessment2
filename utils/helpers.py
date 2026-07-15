"""
helpers.py

This module contains helper functions for
inventory calculations.
"""


def total_stock_value(items):
    """
    Calculates the total value of all inventory items.

    Raises:
        ValueError: If the inventory is empty or contains
        invalid quantity or price values.
    """

    if not items:
        raise ValueError("Inventory is empty.")

    total = 0

    for item in items:
        if item["quantity"] < 0:
            raise ValueError(f"Invalid quantity for {item['item_name']}.")

        if item["price"] < 0:
            raise ValueError(f"Invalid price for {item['item_name']}.")

        total += item["quantity"] * item["price"]

    return total


def highest_stock_item(items):
    """
    Returns the item with the highest stock value.
    """

    if not items:
        raise ValueError("Inventory is empty.")

    highest = items[0]

    for item in items:
        if item["quantity"] < 0 or item["price"] < 0:
            raise ValueError(f"Invalid data for {item['item_name']}.")

        highest_value = highest["quantity"] * highest["price"]
        current_value = item["quantity"] * item["price"]

        if current_value > highest_value:
            highest = item

    return highest


def lowest_stock_item(items):
    """
    Returns the item with the lowest stock value.
    """

    if not items:
        raise ValueError("Inventory is empty.")

    lowest = items[0]

    for item in items:
        if item["quantity"] < 0 or item["price"] < 0:
            raise ValueError(f"Invalid data for {item['item_name']}.")

        lowest_value = lowest["quantity"] * lowest["price"]
        current_value = item["quantity"] * item["price"]

        if current_value < lowest_value:
            lowest = item

    return lowest
