from flask import Flask
from login import login_bp
from inventory import inventory_bp

app = Flask(__name__)
app.register_blueprint(login_bp)
app.register_blueprint(inventory_bp)

@app.route('/')
def home():
    return "Welcome to TechNova Inventory Management System!"
