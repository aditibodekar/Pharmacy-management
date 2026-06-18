from flask import Blueprint, render_template
from datetime import date
from models.medicine import Medicine
from models.sale import Sale

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard")
def dashboard():
    total_medicines = Medicine.query.count()
    total_sales = Sale.query.count()

    # Low stock medicines
    low_stock = Medicine.query.filter(Medicine.stock < 10).count()

    # Expired medicines
    expired = Medicine.query.filter(Medicine.expiry_date < date.today()).count()

    # Recent sales (latest 5)
    recent_sales = Sale.query.order_by(Sale.id.desc()).limit(5).all()

    return render_template(
        "dashboard.html",
        total_medicines=total_medicines,
        total_sales=total_sales,
        low_stock=low_stock,
        expired=expired,
        recent_sales=recent_sales
    )