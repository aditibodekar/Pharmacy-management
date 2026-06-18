from flask import Blueprint, jsonify, request, redirect, render_template
from models import db
from models.customer import Customer

customer_bp = Blueprint("customer", __name__)

# ---------- PAGE ----------
@customer_bp.route("/customers-page")
def customers_page():
    customers = Customer.query.all()
    return render_template("customers.html", customers=customers)


# ---------- GET API ----------
@customer_bp.route("/customers", methods=["GET"])
def get_customers():
    customers = Customer.query.all()
    return jsonify([c.__dict__ for c in customers])


# ---------- ADD + UPDATE (SAME ROUTE) ----------
@customer_bp.route("/customers", methods=["POST"])
def save_customer():
    customer_id = request.form.get("id")

    if customer_id:
        customer = Customer.query.get(customer_id)
    else:
        customer = Customer()

    customer.name = request.form["name"]
    customer.age = request.form["age"]
    customer.gender = request.form["gender"]
    customer.phone = request.form["phone"]
    customer.email = request.form["email"]
    customer.address = request.form["address"]

    db.session.add(customer)
    db.session.commit()

    return redirect("/customers-page")


# ---------- DELETE ----------
@customer_bp.route("/delete-customer/<int:id>")
def delete_customer(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    return redirect("/customers-page")