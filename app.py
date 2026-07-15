"""
app.py

Main program for the Inventory Management System.

This application displays the inventory, calculates stock
statistics, and allows users to search for an item.
"""

from inventory import get_inventory
from utils.helpers import (
    highest_stock_item,
    lowest_stock_item,
    total_stock_value,
    total_quantity,
    average_price,
    find_item,
)


def display_inventory(items):
    """
    Displays all inventory items in a formatted table.
    """

    print("=" * 50)
    print("          INVENTORY REPORT")
    print("=" * 50)

    print(f"{'Item':<20}{'Qty':>8}{'Price':>12}{'Value':>15}")
    print("-" * 55)

    for item in items:
        stock_value = item["quantity"] * item["price"]

        print(
            f"{item['item_name']:<20}"
            f"{item['quantity']:>8}"
            f"{item['price']:>12,}"
            f"{stock_value:>15,}"
        )


def display_summary(items):
    """
    Displays inventory statistics.
    """

    highest = highest_stock_item(items)
    lowest = lowest_stock_item(items)
    total = total_stock_value(items)

    total_quantity_value = total_quantity(items)
    average_price_value = average_price(items)

    print()
    print("=" * 50)
    print("SUMMARY")
    print("=" * 50)

    print(
        f"Highest Stock Value : "
        f"{highest['item_name']} "
        f"(₦{highest['quantity'] * highest['price']:,})"
    )

    print(
        f"Lowest Stock Value  : "
        f"{lowest['item_name']} "
        f"(₦{lowest['quantity'] * lowest['price']:,})"
    )

    print(f"Total Stock Value   : ₦{total:,}")
    print(f"Total Quantity      : {total_quantity_value}")
    print(f"Average Item Price  : ₦{average_price_value:,.2f}")
    print(f"Number of Products  : {len(items)}")


def search_inventory(items):
    """
    Searches for an inventory item entered by the user.
    """

    print()
    print("=" * 50)
    print("SEARCH INVENTORY")
    print("=" * 50)

    item_name = input("Enter item name: ")

    item = find_item(items, item_name)

    print("\nItem Found")
    print(f"Item Name : {item['item_name']}")
    print(f"Quantity  : {item['quantity']}")
    print(f"Price     : ₦{item['price']:,}")


def main():
    """
    Main function that controls program execution.
    """

    items = get_inventory()

    display_inventory(items)

    try:
        display_summary(items)
        search_inventory(items)

    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
