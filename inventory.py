"""
inventory.py

Stores inventory items and provides
a function to retrieve the inventory.
"""

ITEMS = [
    {"item_name": "Ballpoint Pen", "quantity": 25, "price": 45000},
    {"item_name": "Stapler", "quantity": 15, "price": 10000},
    {"item_name": "Electronics", "quantity": 5, "price": 120000},
    {"item_name": "Furniture", "quantity": 30, "price": 185000},
    {"item_name": "Stationery", "quantity": 9, "price": 95000}
]


def get_inventory():
    """
    Returns a copy of the inventory list.

    Raises:
        ValueError: If the inventory list is empty.
    """

    if not ITEMS:
        raise ValueError("Inventory is empty.")

    return ITEMS.copy()
