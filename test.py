from flask import Flask, request, jsonify

PRODUCT_CATALOG = {
    "Apples":3.99,
    "Bananas":1.99,
    "Chicken":5.99,
    "Chocolates":11.99,
    "Olive Oil":23.99
    }

shoppingCart = {product:0 for product in PRODUCT_CATALOG}

app = Flask(__name__)

@app.route('/menu', methods=['GET'])
def get_items():
    return jsonify(PRODUCT_CATALOG)

@app.route('/cart', methods=['GET'])
def get_cart():
    return jsonify(shoppingCart)

@app.route('/cart', methods=['POST'])
def add_to_cart():
    item = request.json['item']
    quantity = request.json['quantity']
    if item in PRODUCT_CATALOG:
        shoppingCart[item] += quantity
        return jsonify(shoppingCart)
    else:
        return jsonify({"error": "Item not in menu"})

@app.route('/checkout', methods=['GET'])
def checkout():
    total = sum([shoppingCart[item] * PRODUCT_CATALOG[item] for item in shoppingCart])
    basket = {product:quantity for product,quantity in shoppingCart.items() if quantity > 0}
    return jsonify({"basket": basket, "total": total})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
