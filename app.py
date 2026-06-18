from flask import Flask, render_template, session, redirect
from config import Config
from models import db
import os

from models.medicine import Medicine
from models.sale import Sale
from models.customer import Customer
from models.supplier import Supplier
from models.purchase import Purchase
from models.user import User

from routes.auth_routes import auth_bp
from routes.medicine_routes import medicine_bp
from routes.customer_routes import customer_bp
from routes.supplier_routes import supplier_bp
from routes.sales_routes import sales_bp
from routes.purchase_routes import purchase_bp
from routes.dashboard_routes import dashboard_bp

# Create app first
app = Flask(__name__)
app.config.from_object(Config)

app.secret_key = "your_secret_key"
app.config["SESSION_PERMANENT"] = False

# Initialize database
db.init_app(app)

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(medicine_bp)
app.register_blueprint(customer_bp)
app.register_blueprint(supplier_bp)
app.register_blueprint(sales_bp)
app.register_blueprint(purchase_bp)
app.register_blueprint(dashboard_bp)

# Create tables
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    session.clear()
    return redirect("/login")

@app.route("/dashboard")
def dashboard():
    session.clear()   # 🔥 logout every refresh
    return redirect("/login")

@app.route("/medicines-page")
def medicines_page():
    medicines = Medicine.query.all()
    return render_template("medicines.html", medicines=medicines)


@app.route("/customers-page")
def customers_page():
    customers = Customer.query.all()
    return render_template("customers.html", customers=customers)


@app.route("/suppliers-page")
def suppliers_page():
    suppliers = Supplier.query.all()
    return render_template("suppliers.html", suppliers=suppliers)


@app.route("/sales-page")
def sales_page():
    sales = Sale.query.all()
    return render_template("sales.html", sales=sales)


@app.route("/purchases-page")
def purchases_page():
    purchases = Purchase.query.all()
    return render_template("purchases.html", purchases=purchases)




if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)