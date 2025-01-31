from flask import Flask, render_template, jsonify
from src.database.inventory_db import InventoryDatabase

class WebServer:
    def __init__(self, db):
        self.app = Flask(__name__)
        self.db = db
        
        # Configure routes
        self.app.add_url_rule('/', 'index', self.index)
        self.app.add_url_rule('/api/products', 'products', self.get_products)

    def start(self):
        self.app.run(host='0.0.0.0', port=5000, threaded=True)

    def index(self):
        return render_template('index.html')

    def get_products(self):
        return jsonify(list(self.db.products.values()))
