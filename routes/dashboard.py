from datetime import date

from flask import Blueprint, render_template

from extensions import db
from models import Product, Sale

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
def index():
    total_products = Product.query.count()
    low_stock = Product.query.filter(
        Product.stock_qty <= Product.low_stock_threshold
    ).order_by(Product.stock_qty).all()

    today = date.today()
    todays_sales = Sale.query.filter(db.func.date(Sale.created_at) == today).all()
    revenue_today = sum(s.total_amount for s in todays_sales)

    recent_sales = Sale.query.order_by(Sale.created_at.desc()).limit(6).all()

    return render_template(
        "dashboard.html",
        total_products=total_products,
        low_stock=low_stock,
        sales_count_today=len(todays_sales),
        revenue_today=revenue_today,
        recent_sales=recent_sales,
    )
