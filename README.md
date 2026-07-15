# Inventory Management System

## Description

This project is a simple inventory management application written in Python.

It demonstrates a modular project structure by separating inventory data, helper functions, and the main application into different files.

## Project Structure

```
inventory_management/
│
├── app.py
├── inventory.py
├── requirements.txt
├── README.md
│
└── utils/
    ├── __init__.py
    └── helpers.py
```

## Features

- Display all inventory items
- Calculate the total stock value
- Display the item with the highest stock value
- Display the item with the lowest stock value
- Modular Python structure
- No external dependencies

## How to Run

Open a terminal in the project folder and run:

```bash
python app.py
```

## Example Output

```
==================================================
          INVENTORY REPORT
==================================================
Item                Qty       Price          Value
--------------------------------------------------
Ballpoint Pen        25       45000        1125000
Stapler              15       10000         150000
Electronics           5      120000         600000
Furniture            30      185000        5550000
Stationery            9       95000         855000

==================================================
SUMMARY
==================================================
Highest Stock Value : Furniture (₦5,550,000)
Lowest Stock Value  : Stapler (₦150,000)
Total Stock Value   : ₦8,280,000
```
