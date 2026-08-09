from flask import Blueprint, flash, redirect, render_template, request, url_for

from extensions import db
from models import Product

inventory_bp = Blueprint("inventory", __name__, url_prefix="/inventory")


def _read_product_form(form):
    return dict(
        name=form["name"].strip(),
        category=form.get("category", "").strip(),
        price=float(form.get("price") or 0),
        cost_price=float(form.get("cost_price") or 0),
        stock_qty=int(form.get("stock_qty") or 0),
        low_stock_threshold=int(form.get("low_stock_threshold") or 5),
        unit=(form.get("unit") or "pcs").strip() or "pcs",
    )


@inventory_bp.route("/")
def list_products():
    q = request.args.get("q", "").strip()
    query = Product.query
    if q:
        query = query.filter(Product.name.ilike(f"%{q}%"))
    products = query.order_by(Product.name).all()
    return render_template("inventory/list.html", products=products, q=q)


@inventory_bp.route("/add", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        if not request.form.get("name", "").strip():
            flash("Product name is required.", "error")
            return render_template("inventory/form.html", product=None)
        p = Product(**_read_product_form(request.form))
        db.session.add(p)
        db.session.commit()
        flash(f'"{p.name}" added to inventory.', "success")
        return redirect(url_for("inventory.list_products"))
    return render_template("inventory/form.html", product=None)


@inventory_bp.route("/<int:product_id>/edit", methods=["GET", "POST"])
def edit_product(product_id):
    p = Product.query.get_or_404(product_id)
    if request.method == "POST":
        if not request.form.get("name", "").strip():
            flash("Product name is required.", "error")
            return render_template("inventory/form.html", product=p)
        for key, value in _read_product_form(request.form).items():
            setattr(p, key, value)
        db.session.commit()
        flash(f'"{p.name}" updated.', "success")
        return redirect(url_for("inventory.list_products"))
    return render_template("inventory/form.html", product=p)


@inventory_bp.route("/<int:product_id>/delete", methods=["POST"])
def delete_product(product_id):
    p = Product.query.get_or_404(product_id)
    name = p.name
    db.session.delete(p)
    db.session.commit()
    flash(f'"{name}" removed from inventory.', "info")
    return redirect(url_for("inventory.list_products"))
