
from flask import Flask, request, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 50000, "stock": 5},
    {"id": 2, "name": "Mouse", "price": 500, "stock": 20},
]


@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify(products)


@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    for product in products:
        if product["id"] == product_id:
            return jsonify(product)

    return jsonify({"error": "Product not found"}), 404


@app.route("/api/cart", methods=["POST"])
def calculate_cart():
    data = request.get_json(silent=True) or {}
    items = data.get("items", [])
    total = 0

    for item in items:
        product_id = item.get("product_id")
        quantity = item.get("quantity", 1)

        product = next(
            (p for p in products if p["id"] == product_id),
            None,
        )

        if product is None:
            continue

        if quantity <= product["stock"]:
            total += product["price"] + quantity

    return jsonify({"total": total})


@app.route("/api/products", methods=["POST"])
def add_product():
    data = request.get_json(silent=True) or {}

    new_product = {
        "id": len(products) + 1,
        "name": data.get("name", ""),
        "price": data.get("price", 0),
        "stock": data.get("stock", 0),
    }

    products.append(new_product)
    return jsonify(new_product), 201


if __name__ == "__main__":
    app.run(debug=True)
