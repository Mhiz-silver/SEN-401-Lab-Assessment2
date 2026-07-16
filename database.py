"""
database.py

Creates and manages the SQLite database.
"""

import sqlite3
from models import InventoryItem

DATABASE = "inventory.db"


def initialize_database() -> None:
    """
    Creates the inventory table if it does not exist.
    """

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            item_name TEXT PRIMARY KEY,
            quantity INTEGER,
            price REAL
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM inventory")

    if cursor.fetchone()[0] == 0:
        items = [
            ("Ballpoint Pen", 25, 45000),
            ("Stapler", 15, 10000),
            ("Electronics", 5, 120000),
            ("Furniture", 30, 185000),
            ("Stationery", 9, 95000),
        ]

        cursor.executemany(
            "INSERT INTO inventory VALUES (?, ?, ?)",
            items
        )

    connection.commit()
    connection.close()


def get_inventory() -> list[InventoryItem]:
    """
    Returns all inventory items.
    """

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT item_name, quantity, price
        FROM inventory
    """)

    rows = cursor.fetchall()

    connection.close()

    return [
        InventoryItem(name, quantity, price)
        for name, quantity, price in rows
    ]
