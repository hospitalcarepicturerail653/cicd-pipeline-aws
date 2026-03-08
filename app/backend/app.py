import os
import logging
import json
from flask import Flask, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

VERSION = os.environ.get("APP_VERSION", "1.0.0")
ENVIRONMENT = os.environ.get("ENVIRONMENT", "production")

items = [
    {"id": 1, "name": "Item One", "description": "First item"},
    {"id": 2, "name": "Item Two", "description": "Second item"},
    {"id": 3, "name": "Item Three", "description": "Third item"},
]


@app.route("/")
def index():
    return jsonify({
        "message": "Flask API running on ECS Fargate",
        "version": VERSION,
        "environment": ENVIRONMENT
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy", "version": VERSION})


@app.route("/api/items")
def get_items():
    logger.info(json.dumps({"action": "get_items", "count": len(items)}))
    return jsonify({"items": items, "count": len(items)})


@app.route("/api/items/<int:item_id>")
def get_item(item_id):
    item = next((i for i in items if i["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
