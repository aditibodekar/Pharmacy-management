from models import db

class Sale(db.Model):
    __tablename__ = "sales"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer)
    medicine_name = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    unit_price = db.Column(db.Float)
    discount = db.Column(db.Float)
    tax = db.Column(db.Float)
    total_amount = db.Column(db.Float)
    payment_method = db.Column(db.String(50))