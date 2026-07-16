"""
app.py

Entry point for the Inventory Management System.
"""

from controllers import (
    display_inventory,
    display_summary,
    search_inventory,
)


def main() -> None:
    """
    Runs the Inventory Management System.
    """

    display_inventory()
    display_summary()
    search_inventory()


if __name__ == "__main__":
    main()
