from models import db

class Medicine(db.Model):
    __tablename__ = "medicines"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100))
    supplier = db.Column(db.String(100))
    batch_no = db.Column(db.String(50))
    purchase_price = db.Column(db.Float)
    selling_price = db.Column(db.Float)
    stock = db.Column(db.Integer)
    manufacture_date = db.Column(db.String(20))
    expiry_date = db.Column(db.String(20))
    barcode = db.Column(db.String(100))