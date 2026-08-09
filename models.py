from datetime import datetime

from extensions import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(80))
    price = db.Column(db.Float, nullable=False, default=0)
    cost_price = db.Column(db.Float, default=0)
    stock_qty = db.Column(db.Integer, nullable=False, default=0)
    low_stock_threshold = db.Column(db.Integer, default=5)
    unit = db.Column(db.String(30), default="pcs")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def is_low_stock(self):
        return self.stock_qty <= self.low_stock_threshold

    def __repr__(self):
        return f"<Product {self.name}>"


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(30))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Customer {self.name}>"


class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=True)
    customer = db.relationship("Customer", backref="sales")
    total_amount = db.Column(db.Float, nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    items = db.relationship(
        "SaleItem", backref="sale", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Sale {self.id} - {self.total_amount}>"


class SaleItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sale_id = db.Column(db.Integer, db.ForeignKey("sale.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=True)
    product = db.relationship("Product")
    product_name = db.Column(db.String(150))  # snapshot, survives product deletion
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    line_total = db.Column(db.Float, nullable=False)
