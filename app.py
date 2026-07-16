"""
app.py

Entry point for the Inventory Management System.
"""

from database import initialize_database
from controllers import (
    display_inventory,
    display_summary,
    search_inventory,
)


def main() -> None:
    """
    Runs the Inventory Management System.
    """

    initialize_database()

    try:
        display_inventory()
        display_summary()
        search_inventory()

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
