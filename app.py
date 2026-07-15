"""
app.py

Main program for the Inventory Management System.
Displays inventory information and calculates stock statistics.
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

items = get_inventory()

print("=" * 50)
print("          INVENTORY REPORT")
print("=" * 50)

print(f"{'Item':<20}{'Qty':>8}{'Price':>12}{'Value':>15}")
print("-" * 55)

for item in items:
    value = item["quantity"] * item["price"]

    print(
        f"{item['item_name']:<20}"
        f"{item['quantity']:>8}"
        f"{item['price']:>12,}"
        f"{value:>15,}"
    )

print()

try:
    highest = highest_stock_item(items)
    lowest = lowest_stock_item(items)
    total = total_stock_value(items)

    quantity = total_quantity(items)
    average = average_price(items)

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
    print(f"Total Quantity      : {quantity}")
    print(f"Average Item Price  : ₦{average:,.2f}")
    print(f"Number of Products  : {len(items)}")

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

except ValueError as error:
    print(error)
