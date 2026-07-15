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
)

items = get_inventory()

print("=" * 50)
print("          INVENTORY REPORT")
print("=" * 50)

print(f"{'Item':<15}{'Qty':>8}{'Price':>12}{'Value':>15}")
print("-" * 50)

for item in items:
    value = item["quantity"] * item["price"]

    print(
        f"{item['item_name']:<15}"
        f"{item['quantity']:>8}"
        f"{item['price']:>12}"
        f"{value:>15}"
    )

print()

try:
    highest = highest_stock_item(items)
    lowest = lowest_stock_item(items)
    total = total_stock_value(items)

    print("=" * 50)
    print("SUMMARY")
    print("=" * 50)

    print(
        f"Highest Stock Value : {highest['item_name']} "
        f"(₦{highest['quantity'] * highest['price']:,})"
    )

    print(
        f"Lowest Stock Value  : {lowest['item_name']} "
        f"(₦{lowest['quantity'] * lowest['price']:,})"
    )

    print(f"Total Stock Value   : ₦{total:,}")

except ValueError as error:
    print(error)
