from flask import Blueprint, jsonify, request, redirect, render_template
from models import db
from models.supplier import Supplier

supplier_bp = Blueprint("supplier", __name__)

# ---------- PAGE ----------
@supplier_bp.route("/suppliers-page")
def suppliers_page():
    suppliers = Supplier.query.all()
    return render_template("suppliers.html", suppliers=suppliers)


# ---------- GET API ----------
@supplier_bp.route("/suppliers", methods=["GET"])
def get_suppliers():
    suppliers = Supplier.query.all()
    return jsonify([s.__dict__ for s in suppliers])


# ---------- ADD + UPDATE ----------
@supplier_bp.route("/suppliers", methods=["POST"])
def save_supplier():
    supplier_id = request.form.get("id")

    if supplier_id:
        supplier = Supplier.query.get(supplier_id)
    else:
        supplier = Supplier()

    supplier.name = request.form["name"]
    supplier.company = request.form["company"]
    supplier.phone = request.form["phone"]
    supplier.email = request.form["email"]
    supplier.gst_no = request.form["gst_no"]
    supplier.address = request.form["address"]

    db.session.add(supplier)
    db.session.commit()

    return redirect("/suppliers-page")


# ---------- DELETE ----------
@supplier_bp.route("/delete-supplier/<int:id>")
def delete_supplier(id):
    supplier = Supplier.query.get_or_404(id)
    db.session.delete(supplier)
    db.session.commit()
    return redirect("/suppliers-page")