from flask import Blueprint, jsonify, request, redirect, render_template
from models import db
from models.sale import Sale

sales_bp = Blueprint("sales", __name__)
def safe_float(value):
    try:
        return float(value)
    except:
        return 0.0


def safe_int(value):
    try:
        return int(value)
    except:
        return 0

# ---------- PAGE ----------
@sales_bp.route("/sales-page")
def sales_page():
    sales = Sale.query.all()
    return render_template("sales.html", sales=sales)


# ---------- GET API ----------
@sales_bp.route("/sales", methods=["GET"])
def get_sales():
    sales = Sale.query.all()
    return jsonify([s.__dict__ for s in sales])


# ---------- ADD + UPDATE ----------
@sales_bp.route("/sales", methods=["POST"])
def save_sale():
    sale_id = request.form.get("id")

    if sale_id:
        sale = Sale.query.get(sale_id)
    else:
        sale = Sale()

    sale.customer_id = request.form["customer_id"]
    sale.medicine_name = request.form["medicine_name"]

    sale.quantity = safe_int(request.form.get("quantity"))
    sale.unit_price = safe_float(request.form.get("unit_price"))
    sale.discount = safe_float(request.form.get("discount"))
    sale.tax = safe_float(request.form.get("tax"))
    sale.total_amount = safe_float(request.form.get("total_amount"))

    sale.payment_method = request.form.get("payment_method", "")

    db.session.add(sale)
    db.session.commit()

    return redirect("/sales-page")


# ---------- DELETE ----------
@sales_bp.route("/delete-sale/<int:id>")
def delete_sale(id):
    sale = Sale.query.get_or_404(id)
    db.session.delete(sale)
    db.session.commit()
    return redirect("/sales-page")

