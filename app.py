from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the API!"


items = [{
    "name": "1",
    "price": 10.99
}
    

]

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items', methods=['POST'])
def add_item():
    item = request.json
    items.append(item)
    return jsonify(item), 201

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    if 0 <= item_id < len(items):
        return jsonify(items[item_id])
    return jsonify({"error": "Item not found"}), 404

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    if 0 <= item_id < len(items):
        item = request.json
        items[item_id] = item
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if 0 <= item_id < len(items):
        item = items.pop(item_id)
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
