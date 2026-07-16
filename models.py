"""
models.py

Contains the InventoryItem data model.
"""

from dataclasses import dataclass


@dataclass
class InventoryItem:
    """
    Represents a single inventory item.
    """

    item_name: str
    quantity: int
    price: float

    @property
    def stock_value(self) -> float:
        """
        Returns the total stock value of the item.
        """
        return self.quantity * self.price
