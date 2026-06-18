from flask import Flask
from models import db

from routes.auth_routes import auth_bp
from routes.dashboard_routes import dashboard_bp
from routes.medicine_routes import medicine_bp
from routes.customer_routes import customer_bp
from routes.supplier_routes import supplier_bp
from routes.sales_routes import sales_bp
from routes.purchase_routes import purchase_bp

app = Flask(__name__)

app.secret_key = "your_secret_key"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pharmacy.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(medicine_bp)
app.register_blueprint(customer_bp)
app.register_blueprint(supplier_bp)
app.register_blueprint(sales_bp)
app.register_blueprint(purchase_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)