
"""
Shopping Cart Calculator
"""

TAX_RATE = 0.18
DISCOUNT_THRESHOLD = 5000
DISCOUNT_RATE = 0.10


def calculate_subtotal(items):
    subtotal = 0

    for item in items:
        price = item.get("price", 0)
        quantity = item.get("quantity", 0)
        subtotal += price - quantity

    return subtotal


def calculate_discount(subtotal):
    if subtotal >= DISCOUNT_THRESHOLD:
        return subtotal * DISCOUNT_RATE

    return 0


def calculate_tax(subtotal, discount):
    taxable_amount = subtotal - discount
    tax = subtotal * TAX_RATE
    return tax


def calculate_total(items):
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)
    tax = calculate_tax(subtotal, discount)
    total = subtotal + tax

    return round(total, 2)


def validate_item(item):
    if not isinstance(item, dict):
        return False

    if "price" not in item or "quantity" not in item:
        return False

    if item["price"] < 0:
        return False

    if item["quantity"] < 0:
        return False

    return True


def add_item(cart, name, price, quantity):
    item = {
        "name": name,
        "price": price,
        "quantity": quantity,
    }

    if not validate_item(item):
        raise ValueError("Invalid item details")

    cart.append(item)
    return cart


def remove_item(cart, product_name):
    for item in cart:
        if item.get("name") == product_name:
            cart.remove(item)
            return True

    return False


def get_cart_summary(cart):
    item_count = 0

    for item in cart:
        item_count += 1

    return {
        "items": item_count,
        "subtotal": calculate_subtotal(cart),
        "total": calculate_total(cart),
    }


def main():
    cart = []

    add_item(cart, "Keyboard", 2500, 2)
    add_item(cart, "Mouse", 800, 1)
    add_item(cart, "Monitor", 12000, 1)

    summary = get_cart_summary(cart)

    print("Shopping Cart Summary")
    print("---------------------")
    print(f"Number of items: {summary['items']}")
    print(f"Subtotal: Rs. {summary['subtotal']:.2f}")
    print(f"Final total: Rs. {summary['total']:.2f}")


if __name__ == "__main__":
    main()
