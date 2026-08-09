import json

from flask import Blueprint, flash, redirect, render_template, request, url_for

from extensions import db
from models import Customer, Product, Sale, SaleItem

billing_bp = Blueprint("billing", __name__, url_prefix="/billing")


@billing_bp.route("/")
def new_sale():
    products = Product.query.order_by(Product.name).all()
    customers = Customer.query.order_by(Customer.name).all()
    return render_template("billing.html", products=products, customers=customers)


@billing_bp.route("/checkout", methods=["POST"])
def checkout():
    try:
        cart = json.loads(request.form.get("cart_json", "[]"))
    except (ValueError, TypeError):
        cart = []

    if not cart:
        flash("Cart is empty — add at least one product before checking out.", "error")
        return redirect(url_for("billing.new_sale"))

    customer_id = request.form.get("customer_id") or None
    new_customer_name = request.form.get("new_customer_name", "").strip()
    new_customer_phone = request.form.get("new_customer_phone", "").strip()

    if not customer_id and new_customer_name:
        customer = Customer(name=new_customer_name, phone=new_customer_phone)
        db.session.add(customer)
        db.session.flush()
        customer_id = customer.id

    sale = Sale(customer_id=customer_id, total_amount=0)
    db.session.add(sale)
    db.session.flush()

    total = 0.0
    for item in cart:
        product = Product.query.get(int(item.get("id", 0)))
        if not product:
            continue
        qty = max(0, int(item.get("qty", 0)))
        if product.stock_qty > 0:
            qty = min(qty, product.stock_qty)
        if qty <= 0:
            continue
        line_total = round(qty * product.price, 2)
        total += line_total
        db.session.add(
            SaleItem(
                sale_id=sale.id,
                product_id=product.id,
                product_name=product.name,
                quantity=qty,
                unit_price=product.price,
                line_total=line_total,
            )
        )
        product.stock_qty = max(0, product.stock_qty - qty)

    if total == 0:
        db.session.rollback()
        flash("Could not complete sale — check product stock and try again.", "error")
        return redirect(url_for("billing.new_sale"))

    sale.total_amount = round(total, 2)
    db.session.commit()
    flash(f"Sale #{sale.id} recorded — total Rs. {sale.total_amount:.2f}", "success")
    return redirect(url_for("billing.receipt", sale_id=sale.id))


@billing_bp.route("/receipt/<int:sale_id>")
def receipt(sale_id):
    sale = Sale.query.get_or_404(sale_id)
    return render_template("receipt.html", sale=sale)
