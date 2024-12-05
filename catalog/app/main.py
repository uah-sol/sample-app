from flask import Flask, jsonify
import os
import model.fake_products as products
from uuid import UUID

app = Flask(__name__)


@app.route('/products')
def get_products():
    return jsonify(products.get_all_products())

@app.route('/products/<uuid:product_id>')
def get_product(product_id):
    product = products.get_product_by_sku(product_id)
    if product:
        return jsonify(product)
    else:
        return jsonify({"error": f"Product {product_id} not found"}), 404

@app.route('/products', methods=['POST'])
def create_product():
    new_product = None
    return jsonify(new_product), 201

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    return jsonify({"error": "Product not found"}), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ["PORT"])
