from flask import Blueprint, jsonify, request, redirect, render_template
from models import db
from models.medicine import Medicine

medicine_bp = Blueprint("medicine", __name__)

# ---------- SAFE HELPERS ----------
def safe_float(value):
    return float(value) if value not in ["", None] else 0.0

def safe_int(value):
    return int(value) if value not in ["", None] else 0


# ---------- PAGE ROUTE (IMPORTANT) ----------
@medicine_bp.route("/medicines-page")
def medicines_page():
    medicines = Medicine.query.all()
    return render_template("medicines.html", medicines=medicines)


# ---------- GET ALL (API OPTIONAL) ----------
@medicine_bp.route("/medicines", methods=["GET"])
def get_medicines():
    medicines = Medicine.query.all()
    return jsonify([m.__dict__ for m in medicines])


# ---------- ADD + UPDATE (SAME ROUTE) ----------
@medicine_bp.route("/medicines", methods=["POST"])
def save_medicine():
    medicine_id = request.form.get("id")

    # UPDATE MODE
    if medicine_id:
        medicine = Medicine.query.get(medicine_id)
    else:
        medicine = Medicine()

    medicine.name = request.form["name"]
    medicine.category = request.form["category"]
    medicine.supplier = request.form["supplier"]
    medicine.batch_no = request.form["batch_no"]

    medicine.purchase_price = safe_float(request.form.get("purchase_price"))
    medicine.selling_price = safe_float(request.form.get("selling_price"))
    medicine.stock = safe_int(request.form.get("stock"))

    medicine.manufacture_date = request.form.get("manufacture_date")
    medicine.expiry_date = request.form.get("expiry_date")
    medicine.barcode = request.form.get("barcode")

    db.session.add(medicine)
    db.session.commit()

    return redirect("/medicines-page")


# ---------- DELETE ----------
@medicine_bp.route("/delete-medicine/<int:id>")
def delete_medicine(id):
    medicine = Medicine.query.get_or_404(id)
    db.session.delete(medicine)
    db.session.commit()
    return redirect("/medicines-page")