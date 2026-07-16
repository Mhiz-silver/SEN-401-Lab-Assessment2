"""
controllers.py

Contains functions that control the application workflow.
"""

from database import get_inventory
from utils.helpers import (
    highest_stock_item,
    lowest_stock_item,
    total_stock_value,
    total_quantity,
    average_price,
    find_item,
)


def display_inventory() -> None:
    """
    Displays the inventory in a formatted table.
    """

    items = get_inventory()

    print("=" * 60)
    print("                 INVENTORY REPORT")
    print("=" * 60)

    print(f"{'Item':<20}{'Qty':>8}{'Price':>12}{'Value':>15}")
    print("-" * 60)

    for item in items:
        print(
            f"{item.item_name:<20}"
            f"{item.quantity:>8}"
            f"{item.price:>12,.0f}"
            f"{item.stock_value:>15,.0f}"
        )


def display_summary() -> None:
    """
    Displays inventory statistics.
    """

    items = get_inventory()

    highest = highest_stock_item(items)
    lowest = lowest_stock_item(items)

    print()
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)

    print(f"Highest Stock Value : {highest.item_name}")
    print(f"Lowest Stock Value  : {lowest.item_name}")
    print(f"Total Stock Value   : ₦{total_stock_value(items):,.0f}")
    print(f"Total Quantity      : {total_quantity(items)}")
    print(f"Average Item Price  : ₦{average_price(items):,.2f}")
    print(f"Number of Products  : {len(items)}")


def search_inventory() -> None:
    """
    Searches for an inventory item.
    """

    items = get_inventory()

    print()
    print("=" * 60)
    print("SEARCH INVENTORY")
    print("=" * 60)

    name = input("Enter item name: ")

    try:
        item = find_item(items, name)

        print("\nItem Found")
        print(f"Name      : {item.item_name}")
        print(f"Quantity  : {item.quantity}")
        print(f"Price     : ₦{item.price:,.0f}")
        print(f"Value     : ₦{item.stock_value:,.0f}")

    except ValueError as error:
        print(error)
