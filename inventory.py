"""
inventory.py

Stores the inventory data.
"""

from models import InventoryItem


ITEMS = [
    InventoryItem("Ballpoint Pen", 25, 45000),
    InventoryItem("Stapler", 15, 10000),
    InventoryItem("Electronics", 5, 120000),
    InventoryItem("Furniture", 30, 185000),
    InventoryItem("Stationery", 9, 95000),
]


def get_inventory() -> list[InventoryItem]:
    """
    Returns a copy of the inventory list.
    """
    return ITEMS.copy()
