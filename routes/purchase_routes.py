from flask import Blueprint, jsonify, request, redirect, render_template
from models import db
from models.purchase import Purchase

purchase_bp = Blueprint("purchase", __name__)


# Safe conversion
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
@purchase_bp.route("/purchases-page")
def purchases_page():
    purchases = Purchase.query.all()
    return render_template("purchases.html", purchases=purchases)


# ---------- GET API ----------
@purchase_bp.route("/purchases", methods=["GET"])
def get_purchases():
    purchases = Purchase.query.all()
    return jsonify([p.__dict__ for p in purchases])


# ---------- ADD + UPDATE ----------
@purchase_bp.route("/purchases", methods=["POST"])
def save_purchase():
    purchase_id = request.form.get("id")

    if purchase_id:
        purchase = Purchase.query.get(purchase_id)
    else:
        purchase = Purchase()

    purchase.supplier_id = request.form["supplier_id"]
    purchase.medicine_name = request.form["medicine_name"]
    purchase.quantity = safe_int(request.form.get("quantity"))
    purchase.purchase_price = safe_float(request.form.get("purchase_price"))
    purchase.total_amount = safe_float(request.form.get("total_amount"))
    purchase.purchase_date = request.form["purchase_date"]

    db.session.add(purchase)
    db.session.commit()

    return redirect("/purchases-page")


# ---------- DELETE ----------
@purchase_bp.route("/delete-purchase/<int:id>")
def delete_purchase(id):
    purchase = Purchase.query.get_or_404(id)
    db.session.delete(purchase)
    db.session.commit()
    return redirect("/purchases-page")