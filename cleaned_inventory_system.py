import json
import logging
from datetime import datetime
from typing import Dict, List

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

stock_data: Dict[str, int] = {}


def add_item(item: str, qty: int = 0, logs: List[str] | None = None) -> None:
    """Add an item and quantity to the inventory."""
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning("Invalid input types for add_item: %s, %s", item, qty)
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info("Added %d of %s", qty, item)


def remove_item(item: str, qty: int) -> None:
    """Remove a specific quantity of an item from the inventory."""
    try:
        if item not in stock_data:
            logging.warning("Attempted to remove non-existent item: %s", item)
            return
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
        logging.info("Removed %d of %s", qty, item)
    except KeyError as e:
        logging.error("Error removing item %s: %s", item, e)
    except Exception as e:  # pylint: disable=broad-exception-caught
        logging.error("Unexpected error: %s", e)


def get_qty(item: str) -> int:
    """Get quantity of an item in inventory."""
    if item not in stock_data:
        logging.warning("Item not found: %s", item)
        return 0
    return stock_data[item]


def load_data(file: str = "inventory.json") -> None:
    """Load inventory data from a JSON file."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
        logging.info("Data loaded from %s", file)
    except FileNotFoundError:
        logging.warning("File %s not found. Starting with empty inventory.", file)
        stock_data = {}
    except json.JSONDecodeError as e:
        logging.error("Error decoding JSON: %s", e)
        stock_data = {}


def save_data(file: str = "inventory.json") -> None:
    """Save inventory data to a JSON file."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4)
        logging.info("Data saved to %s", file)
    except OSError as e:
        logging.error("Error saving data: %s", e)


def print_data() -> None:
    """Print the current inventory report."""
    print("Items Report:")
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")


def check_low_items(threshold: int = 5) -> List[str]:
    """Return list of items below a given quantity threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main() -> None:
    """Main execution block."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item("orange", 3)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
