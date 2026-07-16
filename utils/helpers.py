"""
helpers.py

Contains helper functions for inventory calculations.
"""

from models import InventoryItem


def validate_inventory(items: list[InventoryItem]) -> None:
    """
    Validates that the inventory is not empty.
    """

    if not items:
        raise ValueError("Inventory is empty.")


def total_stock_value(items: list[InventoryItem]) -> float:
    """
    Calculates the total stock value.
    """

    validate_inventory(items)

    return sum(item.stock_value for item in items)


def highest_stock_item(items: list[InventoryItem]) -> InventoryItem:
    """
    Returns the item with the highest stock value.
    """

    validate_inventory(items)

    return max(items, key=lambda item: item.stock_value)


def lowest_stock_item(items: list[InventoryItem]) -> InventoryItem:
    """
    Returns the item with the lowest stock value.
    """

    validate_inventory(items)

    return min(items, key=lambda item: item.stock_value)


def total_quantity(items: list[InventoryItem]) -> int:
    """
    Calculates the total quantity.
    """

    validate_inventory(items)

    return sum(item.quantity for item in items)


def average_price(items: list[InventoryItem]) -> float:
    """
    Calculates the average item price.
    """

    validate_inventory(items)

    return sum(item.price for item in items) / len(items)


def find_item(items: list[InventoryItem], name: str) -> InventoryItem:
    """
    Searches for an inventory item by name.
    """

    validate_inventory(items)

    for item in items:
        if item.item_name.lower() == name.lower():
            return item

    raise ValueError(f"{name} was not found in the inventory.")
