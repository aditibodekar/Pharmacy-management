from models import db

class Purchase(db.Model):
    __tablename__ = "purchases"

    id = db.Column(db.Integer, primary_key=True)
    supplier_id = db.Column(db.Integer)
    medicine_name = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    purchase_price = db.Column(db.Float)
    total_amount = db.Column(db.Float)
    purchase_date = db.Column(db.String(20))