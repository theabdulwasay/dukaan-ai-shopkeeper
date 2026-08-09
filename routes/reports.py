from datetime import datetime, timedelta

from flask import Blueprint, render_template, request
from sqlalchemy import func

from extensions import db
from models import Product, Sale, SaleItem

reports_bp = Blueprint("reports", __name__, url_prefix="/reports")


@reports_bp.route("/")
def index():
    range_days = int(request.args.get("days", 7))
    since = datetime.utcnow() - timedelta(days=range_days)

    sales_in_range = Sale.query.filter(Sale.created_at >= since).all()
    total_revenue = sum(s.total_amount for s in sales_in_range)
    total_sales = len(sales_in_range)
    avg_sale = (total_revenue / total_sales) if total_sales else 0

    top_items = (
        db.session.query(
            SaleItem.product_name,
            func.sum(SaleItem.quantity).label("qty"),
            func.sum(SaleItem.line_total).label("revenue"),
        )
        .join(Sale)
        .filter(Sale.created_at >= since)
        .group_by(SaleItem.product_name)
        .order_by(func.sum(SaleItem.line_total).desc())
        .limit(6)
        .all()
    )

    low_stock = (
        Product.query.filter(Product.stock_qty <= Product.low_stock_threshold)
        .order_by(Product.stock_qty)
        .all()
    )

    daily = (
        db.session.query(
            func.date(Sale.created_at).label("day"),
            func.sum(Sale.total_amount).label("revenue"),
            func.count(Sale.id).label("count"),
        )
        .filter(Sale.created_at >= since)
        .group_by(func.date(Sale.created_at))
        .order_by(func.date(Sale.created_at))
        .all()
    )
    max_daily_revenue = max([d.revenue for d in daily], default=0) or 1

    return render_template(
        "reports.html",
        total_revenue=total_revenue,
        total_sales=total_sales,
        avg_sale=avg_sale,
        top_items=top_items,
        low_stock=low_stock,
        daily=daily,
        max_daily_revenue=max_daily_revenue,
        range_days=range_days,
    )
